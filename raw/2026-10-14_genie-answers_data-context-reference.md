Source: Databricks Genie output, pasted by Bastien in the project thread on 2026-10-14 16:47 UTC.
Genie produced it from the copy-pasted questions in open-questions.md (section E), plus a "comprehensive context on the data and its ecosystem" Bastien asked for.
Content below is unchanged.

---

%md
## APPENDIX — Renovate Project: Full Data Context Reference

*Copy-paste this entire cell to provide full context to any agent working on the Renovate project.*

---

# 1. DDX DATA MODEL ARCHITECTURE

## 1.1 PII vs Non-PII Split

The DDX data platform is split into two worlds:

| Layer | Catalog | Schema | Contains | IDs are |
|---|---|---|---|---|
| **PII (crm_base)** | `stg_canada_catalog` | `crm_base` | Cleartext names, emails, phones, addresses, mastering/dedup | **Unhashed** |
| **Analytical (crm_reporting)** | `prod_canada_catalog` | `crm_reporting`, `crm_analytics` | Transactions, segments, snapshots, KPIs | **MD5-hashed** |

**Hashing rule (Golden Rule):**
```
crm_reporting.brand_customer_id = md5(concat(crm_base.brand_customer_id, '_222'))
crm_reporting.brand_mdm_id      = md5(concat(crm_base.brand_mdm_id, '_222'))
crm_reporting.source_customer_id = md5(concat(crm_base.source_customer_id, '_222'))
```
This applies to ALL identifiers when joining crm_base ↔ crm_reporting/crm_analytics.

## 1.2 Identity Resolution

Queried from `stg_canada_catalog.crm_base.dim_customer_bridge` (18.4M rows):

| Relationship | Ratio | Meaning |
|---|---|---|
| `brand_customer_id` : `brand_mdm_id` | **1:1** (10.5M each) | Same cardinality — two names for the same concept |
| `brand_mdm_id` : `global_mdm_id` | **1.32:1** (10.5M → 8.0M) | Cross-brand identity resolution (a person with 2 brands = 2 brand_mdm_ids → 1 global_mdm_id) |

**Naming mismatch (SuperGold vs current):**
- Current DDX / Liveramp uses: `brand_mdm_id`, `global_mdm_id`
- SuperGold (target Gold Layer) uses: `brand_customer_id`, `global_customer_id`
- These are the same IDs with different names.

---

# 2. KEY TABLES — CURRENT STATE

## 2.1 Core Snapshot Table: `fact_customer_segment_by_brand`

**Location:** `prod_canada_catalog.crm_reporting.fact_customer_segment_by_brand`
**Grain:** One row per `brand_customer_id` × `snapshot_year_month`
**History:** Jan 2022 → Oct 2026 (58 monthly snapshots)
**Refresh:** Monthly

This is the backbone of all executive reporting. Key columns:

| Column | Purpose | Example Values |
|---|---|---|
| `snapshot_year_month` | Month identifier (INT) | 202610 |
| `snapshot_date_key` | Full date key (INT, yyyyMMdd) | 20261031 |
| `brand_customer_id` | Hashed customer ID | md5 hash |
| `brand_code` | Brand identifier | KIE, LAN, ITC, KER, AEO, SKIN... |
| `division_code` | Division | LUXE, LDB, PPD, CPD, ACD (=LDB alias), CORP |
| `pref_language` | Preferred language | EN, FR, en_CA, fr_CA, UNKNOWN (29% UNKNOWN — badly standardized) |
| `email_contactability_key` | Email contactable flag | 'Y' or other |
| `sms_double_optin` | SMS opt-in status | 'SSOI' = opted in |
| `last_engagement_date_key` | Last click/open date key | 20260815 (yyyyMMdd INT) |
| `churn_status_key` | Churn/lapsed classification | See below |
| **Buyer status keys (all L12M):** | | |
| `12_months_buyer_status_key` | Active buyer L12M | 'DDM_12B_AB' |
| `12_months_new_buyer_key` | New buyer L12M | 'DDM_12NB_NB' |
| `12_months_repeat_buyer_status_key` | Repeat buyer L12M | 'DDM_12REPTB_RB' |
| `12_months_retained_buyer_status_key` | Retained buyer L12M | 'DDM_12RETNB_RB' |
| `12_months_reactivated_buyer_status_key` | Reactivated buyer L12M | 'DDM_12REACB_RB' |
| `ytd_new_buyer_status_key` | New buyer YTD | 'DDM_YTDNB_NB' |
| `1_month_new_buyer_key` | New buyer 1M | 'DDM_1NB_NB' |
| **Consumer status keys:** | | |
| `1_month_new_consumer_status_key` | New name 1M | 'DDM_1NC_NC' |
| `12_months_new_consumer_status_key` | New name L12M | 'DDM_12NC_NC' |
| `ytd_new_consumer_status_key` | New name YTD | 'DDM_YTDNC_NC' |
| `unique_orders` | Order count this snapshot | INT |

### churn_status_key distribution (Oct 2026 snapshot):

| Value | Customers | Meaning |
|---|---|---|
| `DDM_CHRN_NA` | 6.07M | Not applicable (never purchased or prospect) |
| `DDM_CHRN_L12M` | 514K | Active — purchased within last 12 months |
| `DDM_CHRN_L12_24M` | 383K | Lapsed 12-24 months |
| `DDM_CHRN_L24M_PLUS` | 1.09M | Lapsed 24+ months |

Note: The Liveramp view's `churn_12_24_flag` and `churn_24plus_flag` are **derived** from this key in the view definition, not stored columns. Damien (LiveRamp owner) has requested a new `Is_Churn_12M_36M` flag (12-36M window) that does not exist today and would require splitting `DDM_CHRN_L24M_PLUS` using `last_purchase_date`.

## 2.2 Scorecard Analytics Table: `pbix_2bc_scorecard`

**Location:** `prod_canada_catalog.crm_analytics.pbix_2bc_scorecard`
**Grain:** One row per `brand_code` × `snapshot_month`
**History:** Jan 2022 → Oct 2026 (58 months)
**Refresh:** Monthly (DDX Executive Report job, Mondays 7AM UTC)
**Built from:** Aggregation of `fact_customer_segment_by_brand` + `dim_customer_brand_profile`

Pre-aggregated KPI columns:

| Column | Definition |
|---|---|
| `Total_DDX_Contacts` | COUNT(DISTINCT brand_customer_id) |
| `DDX_Contactable_Contacts` | WHERE email_contactability_key = 'Y' OR sms_double_optin = 'SSOI' |
| `DDX_Email_Contactable_Contacts` | WHERE email_contactability_key = 'Y' |
| `DDX_SMS_Contactable_Contacts` | WHERE sms_double_optin = 'SSOI' |
| `DDX_Active_Buyers` | WHERE 12_months_buyer_status_key = 'DDM_12B_AB' |
| `DDX_Active_Buyers_1M` | WHERE unique_orders > 0 (snapshot month) |
| `DDX_Active_Buyers_3M` | WHERE last_purchase_date_key >= snapshot - 3 months |
| `DDX_Active_Buyers_YTD` | WHERE ytd_buyer_status_key = 'DDM_YTDB_AB' |
| `New_Contacts_1M` / `_12M` / `_YTD` | WHERE new_consumer_status_key variants |
| `Email_Optin_1M` / `_12M` / `_YTD` | WHERE first_email_opt_in_date_key in window |
| `Email_Unsubscribe_1M` / `_12M` / `_YTD` | WHERE email_unsubscribe_date in window |
| `New_Contacts_Contactable_1M` / `_12M` / `_YTD` | New consumer + contactable |
| `New_Buyers_1M` / `_3M` / `_12M` / `_YTD` | New buyer status keys |
| `Repeat_Buyers_1M` / `_YTD` / `_12M` | Repeat buyer status keys |
| `New_Repeat_Buyers_1M` / `_3M` / `_12M` / `_YTD` | New + repeat in same window |
| `Retained_buyer_12M` | WHERE 12_months_retained_buyer_status_key = 'DDM_12RETNB_RB' |
| `Reactivated_buyer_12M` | WHERE 12_months_reactivated_buyer_status_key = 'DDM_12REACB_RB' |
| `Media_addressable` | COUNT(DISTINCT brand_customer_id) from dim_customer_brand_profile WHERE created_dt <= snapshot_month |
| `Click_or_open_12` | Contactable + last_engagement_date in L12M (= engagement) |

## 2.3 Order Sales: `vw_fact_order_sales`

**Location:** `prod_canada_catalog.crm_reporting.vw_fact_order_sales`
**Grain:** One row per order line
**Refresh:** Daily (latest data: Oct 12, 2026)
**Key columns:** `brand_customer_id` (hashed), `brand_code`, `division`, `order_dt`, `order_num`, `net_sales`, `order_total_after_discount`, `purchase_channel` (NULL = D2C online), `is_guest_order`, `order_status`, `shipping_status`, `order_hier_type` ('HEADER' for order-level)

**Standard filters for D2C revenue:**
```sql
WHERE order_status NOT IN ('CANCELLED', 'RETURNED')
  AND brand_code NOT IN ('SHUUS', 'BIOUS')
  AND purchase_channel IS NULL          -- D2C online only
  AND is_guest_order = 'N'              -- identified customers only
```

## 2.4 Campaign Data: `fact_message_tracker`

**Location:** `prod_canada_catalog.crm_base.fact_message_tracker`
**Grain:** One row per email event
**Refresh:** Daily (latest: Oct 14, 2026)
**Key columns:** `brand_code`, `email_address`, `msg_dispatch_id`, `campaign_name`, `msg_channel` ('EMAIL'), `event_type` ('Sent', 'Open', 'Click'), `event_dt`

## 2.5 Customer360 (PII): `customer360`

**Location:** `stg_canada_catalog.crm_base.customer360`
**Grain:** One row per `brand_customer_id` (unhashed)
**Refresh:** Monthly (ETL job in workspace 6981223385930033)
**Key columns:** `brand_customer_id`, `brand_mdm_id`, `global_mdm_id`, `brand_code`, `division_code`, `churn_status_key`, `segment_type`, `segment_value`, plus many CRM fields
**Note:** `preferred_language` does NOT exist in this table. The field is `pref_language` in `fact_customer_segment_by_brand`.

## 2.6 Liveramp View: `vw_customer360_liveramp`

**Location:** `stg_canada_catalog.crm_base.vw_customer360_liveramp`
**Type:** View (INNER JOIN of customer360 + customer360_contacts)
**Refresh:** Reflects customer360 refresh (monthly)
**Filters:** segment_type IN ('CHURN PREDICTION 12M', 'RFMT', 'LIKELY TO CONVERT 3 MONTHS', 'PRODUCT AFFINITY - BUYER', 'PRODUCT AFFINITY - PROSPECT') OR NULL
**Key columns used in Liveramp dashboard:** `brand_mdm_id`, `global_mdm_id`, `email1`, `loyalty_status`, `engaged_prospects_l12m`, `churn_12_24_flag` (derived), `churn_24plus_flag` (derived), `segment_type`, `brand`, `division`

## 2.7 CLV Table: `pbi_b2c_CLV`

**Location:** `prod_canada_catalog.crm_analytics.pbi_b2c_CLV`
**Grain:** One row per `brand_code` × `Segment` × `Segment_Category` × `Snapshot`
**History:** Dec 2022 → Sep 2026 (16 quarterly snapshots)
**Refresh:** Quarterly (Mar, Jun, Sep, Dec)
**Key columns:** `CLV`, `RetentionRate`, `SegmentSize`, `R12Frequency`, `R12AOV`, `OrdersByPeriod_R12`, `NetSpendByPeriod_R12`, plus LY and LY2 variants

---

# 3. KPI DEFINITIONS WITH SQL FORMULAS

## 3.1 Derived KPIs Used in 2+ Reports (highest priority for Gold standardization)

### Retention Rate
```sql
-- Used in: DDX Scorecard, Buyer Analysis
-- Definition: % of last year's active buyers who bought again this year
Retained_buyer_12M(CY) / DDX_Active_Buyers(LY same snapshot month)
-- Typically excludes AEO (Aesop) brand
```

### AOV (Average Order Value)
```sql
-- Used in: DDX Scorecard, CLV Deepdive, Buyer Analysis
DDX_Identified_Sales / DDX_Orders
-- Where DDX_Identified_Sales = SUM(net_sales) WHERE is_guest_order = 'N' AND purchase_channel IS NULL
```

### Engagement Rate
```sql
-- Used in: DDX Scorecard, Engagement KPIs
-- Definition: contactable customers who clicked or opened in L12M
COUNT(DISTINCT CASE
  WHEN (email_contactability_key = 'Y' OR sms_double_optin = 'SSOI')
  AND last_engagement_date_key >= snapshot_date - 12 months
  THEN brand_customer_id END)
/ COUNT(DISTINCT CASE
  WHEN (email_contactability_key = 'Y' OR sms_double_optin = 'SSOI')
  THEN brand_customer_id END)
```

### New Repeat Rate
```sql
-- Used in: Buyer Analysis, BAR
-- Definition: % of new buyers who made a repeat purchase in the same window
New_Repeat_Buyers_YTD / New_Buyers_YTD
-- Typically excludes AEO and BO brands
```

### DDX Revenue
```sql
-- Used in: DDX Scorecard, Buyer Analysis
SUM(net_sales)
FROM vw_fact_order_sales
WHERE purchase_channel IS NULL
  AND is_guest_order = 'N'
  AND order_status NOT IN ('CANCELLED','RETURNED')
  AND brand_code NOT IN ('SHUUS','BIOUS')
```

## 3.2 Derived KPIs Used in 1 Report

### CLV (Customer Lifetime Value)
```sql
-- Used in: CLV Deepdive only
-- Formula: RetentionRate × AOV × Frequency (3-year discounted model)
-- Computed quarterly from vw_fact_order_sales with R12, LY, LY2 purchase windows
-- Segments: Overall, Acquisition Source, Purchase Channel
```

### In/Out Flow
```sql
-- Used in: DDX Scorecard only
Email_Optin_1M - Email_Unsubscribe_1M  -- (also _12M, _YTD variants)
-- Relies on first_email_opt_in_date_key and email_unsubscribe_date
```

### Media Addressable
```sql
-- Used in: DDX Scorecard only
COUNT(DISTINCT brand_customer_id)
FROM dim_customer_brand_profile
WHERE brand_code NOT IN ('DER','BIOUS','SHUUS')
  AND mdm_record_status = 'ACTIVE'
  AND brand_country = 'CAN'
  AND created_dt <= snapshot_month
```

### Campaign Attribution (3/5/7 day lookback)
```sql
-- Used in: Campaign Performance Report only
-- Logic: match email Open (non-iOS) OR Click → purchase within N days
-- Lookback windows: 3, 5, 7 days stored as days_between for PBI slicer
```

### Churn Rate
```sql
-- Used in: Liveramp Dashboard only
-- Currently derived in vw_customer360_liveramp from churn_status_key
(COUNT WHERE churn_12_24_flag = 'Y' OR churn_24plus_flag = 'Y') / total_profiles
```

---

# 4. CURRENT COUNTS (Oct 2026 snapshot)

| Metric | Count |
|---|---|
| Total customers (fact_customer_segment_by_brand) | 8,034,882 |
| Contactable (email OR SMS) | 4,945,619 (61.6%) |
| Email contactable | 4,621,106 |
| SMS contactable | 794,383 |
| Engaged (scorecard def: contactable + click/open L12M) | 4,134,644 |
| Active buyers L12M | 514,260 |
| New buyers L12M | 283,346 |
| New buyers YTD | 163,339 |
| Repeat buyers L12M | 137,160 |
| Retained buyers L12M | 169,688 |
| Reactivated buyers L12M | 64,655 |

---

# 5. REPORT INVENTORY → SOURCE TABLES

| Report | Purpose | Tables Read |
|---|---|---|
| DDX Scorecard (Executive Report) | Main executive KPI dashboard | `crm_analytics.pbix_2bc_scorecard`, `crm_reporting.fact_customer_segment_by_brand`, `crm_reporting.vw_fact_order_sales`, `crm_reporting.dim_customer_brand_profile` |
| DDX Engagement KPIs | Engagement metrics by brand | `crm_analytics.pbi_b2c_DDX_Scorecard_Engagement_KPIs`, `crm_reporting.fact_customer_segment_by_brand`, `crm_base.fact_message_tracker` |
| CLV Deepdive | Customer lifetime value quarterly | `crm_analytics.pbi_b2c_CLV`, `crm_reporting.vw_fact_order_sales`, `crm_reporting.dim_customer_brand_profile` |
| Campaign Performance | Email campaign metrics + attribution | `crm_analytics.PBIX_Email_Performance_Report`, `crm_base.fact_message_tracker`, `crm_reporting.vw_fact_order_sales` |
| Liveramp Customer 360 | Liveramp export dashboard | `crm_base.vw_customer360_liveramp` (= customer360 + customer360_contacts) |
| DDX Quarterly Figures | Division-level quarterly slide | `crm_analytics.pbix_2bc_scorecard`, `crm_reporting.vw_fact_order_sales` |

---

# 6. REFRESH FREQUENCIES

| Table | Latest Data | Cadence |
|---|---|---|
| `fact_message_tracker` | Oct 14, 2026 | Daily |
| `vw_fact_order_sales` | Oct 12, 2026 | Daily |
| `fact_customer_segment_by_brand` | Oct 2026 | Monthly |
| `pbix_2bc_scorecard` | Oct 2026 | Monthly (job runs Mondays 7AM UTC) |
| `pbi_b2c_CLV` | Sep 2026 | Quarterly |
| `customer360` (crm_base) | Monthly | ETL job in different workspace (830921102389847 in ws 6981223385930033) |

---

# 7. SUPERGOLD (TARGET GOLD LAYER) — STRUCTURE

The SuperGold is the US-built target schema for the Americas Gold Layer. 479 fields across 21 `cdp__` tables:

| Domain | Fields | Key Tables |
|---|---|---|
| Customer (Identity) | 13 | `cdp__identity_v` |
| Customer (Contactability) | 11 | `cdp__contactability_v` |
| Customer (Loyalty) | 26 | `cdp__loyalty_v` |
| Customer (Beauty Profile/BMDM) | 54 | `cdp__beauty_profile_v` |
| Customer (Acquisition/Interaction KPIs) | 21 | `cdp__acquisition_interaction_data_v` |
| Customer (Transactional KPIs) | 22 | `cdp__transactional_kpis_v` |
| Customer (BAR KPIs) | 52 | `cdp__bar_kpi_v` |
| Customer (3P Demographic) | 46 | `cdp__3p_demographic_v` |
| Customer (Predictive Models) | 8 | `cdp__bar_customer_models_v` |
| Customer (Contact Info) | 27 | `cdp__contact_info_v` |
| Transactions (Header) | 30 | `cdp__order_header_v` |
| Transactions (Line) | 27 | `cdp__order_lineitem_v` |
| Transactions (Adjustments) | 19 | `cdp__order_lineitem_price_adjustments_v` |
| Campaign (Master) | 26 | `cdp__campaign_master_v` |
| Campaign (Interactions) | 28 | `cdp__campaign_int_metrics_v` |
| Interactions (Loyalty Events) | 10 | `cdp__loyalty_event_v` |
| Interactions (Tracking) | 11 | `cdp__acquisition_interaction_level_data_v` |
| Website/GA4 (User view) | 10 | `cdp__fact_ga4_users_v` |
| Website/GA4 (Daily events) | 11 | `cdp__fact_ga4_daily_events_v` |
| Product | 27 | `cdp__dim_product_hierarchy_v` |

---

# 8. IDENTIFIED GAPS — SUPERGOLD vs CANADA REPORTS

| # | Gap | Impact | Priority |
|---|---|---|---|
| 1 | **Snapshot / Time Dimension** — SuperGold is current-state only; reports need 58 months of monthly snapshots | All executive trending KPIs break | Critical |
| 2 | **New Consumer Status Keys** — `1_month_new_consumer_status_key`, `12_months_new_consumer_status_key`, `ytd_new_consumer_status_key` not in SuperGold | "New Contacts" family (1M, 12M, YTD) breaks | Critical |
| 3 | **Email Opt-in/Unsub Dates** — SuperGold has status + modified date, not `first_email_opt_in_date_key` or `email_unsubscribe_date` | In/Out flow KPI breaks | High |
| 4 | **CLV** — Computed metric not pre-stored | CLV Deepdive report breaks | High |
| 5 | **Churn Flags** — `churn_status_key` values don't map 1:1 to Liveramp's `churn_12_24_flag` + `churn_24plus_flag`. Damien requests new `Is_Churn_12M_36M` = 3rd definition | Liveramp segmentation breaks | Critical |
| 6 | **Segment Type** — C360 uses `segment_type` (RFMT, Churn Prediction, etc.); SuperGold uses `cdp__bar_customer_models_v` with `model_name`/`segment_value` | Liveramp audience filtering breaks | Medium |
| 7 | **ID Naming** — `brand_mdm_id`/`global_mdm_id` (current) vs `brand_customer_id`/`global_customer_id` (SuperGold) | All downstream ID mapping | Critical |
| 8 | **Contactability field names** — `email_contactability_key` (reports) vs `email_perm_status` (SuperGold) | Contactable count may differ | Medium |
| 9 | **AOV Bucketed vs Exact** — SuperGold has `AOV_last_12_months_bucket` (bucket); CLV needs exact numeric | CLV computation breaks | Medium |
| 10 | **Customer-level product sub-categories** — LiveRamp needs customer affinity (anti-aging, suncare); SuperGold has product-level hierarchy only | LiveRamp targeting breaks | High |
| 11 | **PII accessibility** — LiveRamp/SFMC/Attentive need cleartext PII; Gold Layer must include PII or have export layer | All activation platforms break | Critical |

---

# 9. CANADA-SPECIFIC CONSIDERATIONS

- **Bilingual market:** `pref_language` has 18 distinct values, badly standardized (EN, en_CA, en-CA, en-ca all mean English). 29% is UNKNOWN. Critical for FR/EN campaign targeting.
- **Excluded brands:** `SHUUS`, `BIOUS` always excluded. `DER`, `BO` excluded in some contexts (Liveramp). `AEO` (Aesop) excluded from retention and new repeat rate calculations.
- **Division code mapping:** `ACD` in some tables = `LDB` (L'Oréal Dermatological Beauty). Always map: `CASE WHEN division_code = 'ACD' THEN 'LDB' ELSE division_code END`.
- **Canada-only brands:** BIOCA (Biotherm Canada), GAB (Giorgio Armani Beauty Canada) — may not exist in US SuperGold.
- **Currency:** CAD throughout.

---

# 10. STAKEHOLDERS

| Person | Scope | Key Request |
|---|---|---|
| **Bastien & Mezyan** | Canada PMs & Business Owners | Overall gap analysis, KPI workshops |
| **Shabri** | USA PM & SuperGold owner | Schema design authority |
| **Sandra** | SFMC & Attentive | Email/SMS activation KPIs (feedback pending) |
| **Damien** | LiveRamp | Requests: sub-categories + Is_Churn_12M_36M |
| **Thomas & Olivier** | Genie / Reporting | Reporting KPIs (feedback pending) |

---

# 11. KEY FILES & ASSETS

| Asset | Location |
|---|---|
| Gold Layer Domain Requirements (Excel) | Attached to project — 43 sheets, key: "All Domains - SuperGold" |
| DDX-Elevate PDF | Architecture roadmap — 14 pages |
| DDX Scorecard notebook | `/Analytics Team Shared/[Reporting - PowerBI Queries]/Executive Report/DDX - CA - B2C - Executive Report (DDX SCORECARD).sql` (ID: 4222721905342658) |
| CLV Deepdive notebook | `/Analytics Team Shared/[Reporting - PowerBI Queries]/Executive Report/DDX - CA - B2C - Executive Report (CLV DEEPDIVE).sql` (ID: 3968408009586477) |
| Campaign Performance notebook | `/Analytics Team Shared/[Reporting - PowerBI Queries]/DDX - CA - B2C - Campaign Performance Report.sql` (ID: 1514137779915369) |
| Liveramp Dashboard | Dashboard UUID: 01f1b2ad10251c959e4e8855a56ffe84 |
| Renovate analysis notebook | `/Users/bastien.duthu@loreal.com/RENOVATE` (ID: 1161983296513598) |
| DDX Quarterly figures notebook | `/Users/bastien.duthu@loreal.com/DDX Quarterly figures update` (ID: 1106086832669612) |
