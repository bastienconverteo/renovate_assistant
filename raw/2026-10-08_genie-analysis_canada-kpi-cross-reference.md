<!-- Raw paste. Source: Bastien pasted the output of a Databricks Genie notebook on 2026-10-08 19:43 UTC (Genie compared Canada reporting tables with the SuperGold sheet of the US workbook). Unmodified except that HTML escapes (&amp; &#34; &#39;) were decoded. -->

%md
# Renovate — Gold Layer KPI Cross-Reference & Workshop Preparation

This notebook analyzes whether the KPIs and dimensions currently used in Canada's reporting are covered by the SuperGold layer definition (from the US-built Excel workbook). It also surfaces key questions and potential issues for the upcoming KPI catalog workshop.


%md
## Part 1 — Cross-Reference: Report KPIs vs SuperGold Fields

I reviewed the following Canada reporting assets and cross-referenced them against the **All Domains - SuperGold** sheet (479 fields across 21 `cdp__` tables):

**Reports analyzed:**
* DDX - CA - B2C - Executive Report (DDX SCORECARD) — main executive KPIs
* DDX - CA - B2C - Executive Report (CLV DEEPDIVE) — customer lifetime value
* DDX - CA - B2C - Campaign Performance Report — email campaign metrics
* Liveramp Customer 360 — Canada dashboard — Liveramp extract KPIs

---

### 1.1 Executive Scorecard KPIs (source: `fact_customer_segment_by_brand`)

| Report KPI | SuperGold Field(s) | Status |
|---|---|---|
| Total DDX Contacts | `brand_customer_id` in `cdp__identity_v` | ✅ Present |
| DDX Contactable (Email+SMS) | `email_perm_status` + `sms_double_optin` in `cdp__contactability_v` | ⚠️ Name mismatch — report uses `email_contactability_key` |
| Engagement Rate (12M) | `last_engagement_date_key` in `cdp__acquisition_interaction_data_v` | ✅ Present |
| Active Buyers (1M/3M/YTD/12M) | `buyer_status_key` in `cdp__transactional_kpis_v` | ✅ Present |
| New Contacts (1M/12M/YTD) | Uses `1_month_new_consumer_status_key`, etc. | ❌ **GAP** — these snapshot-level status keys are NOT in SuperGold |
| Email Optin / Unsub dates | Uses `first_email_opt_in_date_key`, `email_unsubscribe_date` | ❌ **GAP** — SuperGold only has `email_perm_status_modified_dt`, not optin/unsub event dates |
| New Contacts Contactable | Combines new consumer status + contactability | ❌ Same gap as new consumer status |
| In-Out Change (Optins − Unsubs) | Derived from optin/unsub counts | ❌ Same gap |
| New Buyers (1M/3M/12M/YTD) | `new_buyer_status_key` in `cdp__transactional_kpis_v` | ✅ Present |
| Repeat Buyers | `repeat_buyer_status_key` in `cdp__transactional_kpis_v` | ✅ Present |
| Retained / Reactivated Buyers | `retained_buyer_status_key`, `reactivated_buyer_status_key` | ✅ Present |
| Media Addressable | Derived from `dim_customer_brand_profile.created_dt` + MDM status | ⚠️ Partial — requires date filtering logic not captured in SuperGold |
| **Snapshot month / snapshot_date_key** | **Not a concept in SuperGold** | ❌ **CRITICAL GAP** — reports are snapshot-based; SuperGold is current-state only |

---

### 1.2 CLV Deepdive KPIs (source: `vw_fact_order_sales`)

| Report KPI | SuperGold Field(s) | Status |
|---|---|---|
| CLV (Customer Lifetime Value) | Not a pre-computed field | ❌ **GAP** — computed formula (retention × AOV × frequency) |
| Retention Rate | Computed from YoY buyer matching | ❌ **GAP** — no pre-computed retention metric |
| AOV (Average Order Value) | `AOV_last_12_months_bucket` in `cdp__bar_kpi_v` | ⚠️ **Bucket only** — report needs exact value, SuperGold has buckets |
| Order Frequency | `order_frequency` in `cdp__transactional_kpis_v` + `cdp__bar_kpi_v` | ✅ Present |
| Net Spend by Period (R12, LY, LY2) | `last_12mnths_net_sales`, `life_time_total_sales` | ⚠️ Partial — only L12M + lifetime; no LY/LY2 window |
| Acquisition Source breakdown | `source_name`, `acquisition_channel_key` | ✅ Present |
| Purchase Channel breakdown | `order_channel` in `cdp__order_header_v` | ✅ Present |

---

### 1.3 Campaign Performance KPIs (source: `fact_message_tracker`)

| Report KPI | SuperGold Field(s) | Status |
|---|---|---|
| Unique Send / Open / Click | `sent_cnt`, `unique_open_cnt`, `unique_click_cnt` in `cdp__campaign_int_metrics_v` | ✅ Present |
| Campaign Name, Type, Channel | `cdp__campaign_master_v` — full campaign metadata | ✅ Present |
| Campaign Attribution (lookback) | `order_num`, `order_dt`, `net_sales` in `cdp__campaign_int_metrics_v` | ⚠️ Building blocks present, but the 3/5/7-day lookback logic is report-side |
| Campaign Revenue | `attributed_revenue` in `cdp__campaign_master_v` | ✅ Present |
| iOS open filtering | Not in SuperGold | ⚠️ Report-side logic (device_id-based iOS exclusion for open rate) |

---

### 1.4 Liveramp Dashboard KPIs (source: `vw_customer360_liveramp`)

| Report KPI | SuperGold Field(s) | Status |
|---|---|---|
| Total Profiles (`brand_mdm_id`) | `brand_customer_id` in SuperGold | ⚠️ **ID mismatch** — C360 uses `brand_mdm_id`, SuperGold uses `brand_customer_id` |
| Global Profiles (`global_mdm_id`) | `global_customer_id` | ⚠️ Name mismatch (mdm_id vs customer_id) |
| Email Coverage % | `email_perm_status` / contact_value in `cdp__contact_info_v` | ✅ Present |
| Loyalty Active % | `is_loyalty` / `loyalty_status_key` in `cdp__loyalty_v` | ✅ Present |
| Engaged Prospects L12M % | `engaged_prospects_l12m` flag | ❌ **GAP** — this derived flag is not in SuperGold |
| Churn Rate % (12-24M, 24M+) | `churn_12_24_flag`, `churn_24plus_flag` | ❌ **GAP** — churn flags not mapped; likely derivable from `lapsed_buyer_status_key` |
| Segment Type distribution | `segment_type` from C360 | ❌ **GAP** — segment_type not in SuperGold; models exist in `cdp__bar_customer_models_v` but different structure |


%md
## Part 2 — Summary of Gaps

### 🚨 Critical Gaps (fields/concepts missing from SuperGold)

1. **Snapshot / Time Dimension** — The executive reports are fundamentally snapshot-based (`fact_customer_segment_by_brand` with `snapshot_year_month`). SuperGold is designed as a "current state" model. This is the single biggest architectural question: **will the Gold Layer support historical snapshots, or only the latest view?** If only the latest, many MoM/YoY trending KPIs cannot be reproduced from the Gold Layer alone.

2. **New Consumer Status Keys** — The `1_month_new_consumer_status_key`, `12_months_new_consumer_status_key`, `ytd_new_consumer_status_key` are core to measuring new name acquisition. These are not in SuperGold. Without them, the "New Contacts" family of KPIs (1M, 12M, YTD) breaks.

3. **Email Opt-in / Unsubscribe Event Dates** — `first_email_opt_in_date_key` and `email_unsubscribe_date` drive the In/Out flow analysis and optin rate calculations. SuperGold only has the current status and the last-modified timestamp, not the original optin or explicit unsub event dates.

4. **CLV (Customer Lifetime Value)** — A computed metric (retention × AOV × frequency). Not a simple field. Needs either: (a) a pre-computed CLV in the Gold Layer, or (b) the building blocks with agreed-upon formula.

5. **Churn & Engaged Prospects Flags** — `churn_12_24_flag`, `churn_24plus_flag`, `engaged_prospects_l12m` used in Liveramp exports are not in SuperGold. They may be derivable from `lapsed_buyer_status_key` and engagement data, but the derivation logic needs to be documented.

6. **Segment Type** — The C360/Liveramp view surfaces `segment_type` (RFMT, Churn Prediction 12M, Likely to Convert 3 Months, Product Affinity, etc.). SuperGold has `cdp__bar_customer_models_v` with `model_name`/`segment_value` but the mapping is not explicit.

### ⚠️ Naming / Mapping Mismatches

7. **ID Column Names** — `brand_mdm_id` (Canada C360/Liveramp) vs `brand_customer_id` (SuperGold). Same for `global_mdm_id` vs `global_customer_id`. Need to confirm whether these are the same IDs with different names, or different identity resolution stages.

8. **Contactability Field Names** — Reports use `email_contactability_key` (from `fact_customer_segment_by_brand`), SuperGold uses `email_perm_status` (from `cdp__contactability_v`). Same underlying concept, different field names.

9. **AOV Bucketed vs Exact** — SuperGold has AOV in buckets (`AOV_last_12_months_bucket`), but CLV and some reports need exact numeric values.

### ✅ Well-Covered Areas

* **Transaction data** — Order headers, line items, and price adjustments are comprehensive
* **Campaign data** — Full campaign master and interaction metrics are covered
* **Loyalty data** — Detailed loyalty program fields (tiers, points, events)
* **Beauty profile / BMDM** — Rich with 54 fields
* **3P Demographic data** — TransUnion enrichment fully mapped
* **BAR KPIs** — 52 fields covering buyer types, engagement, spend buckets, CTR
* **GA4 Website data** — User-level and daily event tables present
* **Product hierarchy** — Full product dimension table



%md
## Part 3 — Key Questions & Discussion Points for the KPI Workshop

### A. Architectural Questions (Priority — answer these first)

**Q1. Will the Gold Layer support historical snapshots or only current state?**
The executive scorecard fundamentally depends on monthly snapshots from `fact_customer_segment_by_brand`. If the Gold Layer is current-state only, we lose:
* MoM / YoY trending for all consumer KPIs
* Time-window metrics (New Contacts 1M, 12M, YTD)
* The ability to reproduce past reports

➡️ **Recommendation:** Clarify whether `cdp__transactional_kpis_v` and similar tables will include snapshot history, or whether a separate snapshot/fact table is planned alongside the Gold entity tables.

**Q2. Where do computed / derived KPIs live?**
SuperGold defines ~479 raw fields (attributes). But many report KPIs are **derived** (CLV, Retention Rate, Engagement Rate, Churn Rate, New Repeat Rate, In/Out flow). Two options:
* Option A: Pre-compute and store them as fields in Gold (e.g., add `clv_score`, `retention_rate`, `churn_flag` to `cdp__transactional_kpis_v`)
* Option B: Define them as standardized calculation logic applied on top of Gold building blocks

➡️ **Recommendation:** For KPIs that appear in multiple reports (CLV, churn, engagement), pre-compute them. For ad-hoc analysis metrics, document the formula.

**Q3. Identity resolution: brand_mdm_id vs brand_customer_id?**
Canada's C360 and Liveramp exports use `brand_mdm_id` and `global_mdm_id` (from Reltio MDM). SuperGold uses `brand_customer_id` and `global_customer_id`. Are these:
* The same IDs with different names?
* Different stages of identity resolution (pre-MDM vs post-MDM)?
* Will the Gold Layer use one or both?

➡️ **Critical for Liveramp, SFMC, and Attentive** — all downstream systems need to know which ID they receive.

---

### B. Specific Gap Questions for Each Team

**For Sandra (SFMC & Attentive):**
* B1. Does SFMC need `new_consumer_status_key` variants to identify new contacts for welcome journeys? If so, these must be added to Gold.
* B2. What email opt-in/unsub event data does SFMC consume? The Gold Layer currently only has status + last modified date, not the original optin date or explicit unsub event date.
* B3. Does Attentive receive engagement flags (e.g., `engaged_prospects_l12m`)? These are absent from SuperGold.
* B4. How does SFMC handle the iOS open tracking issue? Is this handled in the Gold Layer or downstream?

**For Damien (LiveRamp):**
* B5. LiveRamp currently consumes `vw_customer360_liveramp` which includes `segment_type` (RFMT, Churn Prediction, Product Affinity, etc.). How should these segments be represented in the Gold Layer? Currently `cdp__bar_customer_models_v` uses a different structure (`model_name`/`segment_value`).
* B6. Churn flags (`churn_12_24_flag`, `churn_24plus_flag`) are used for audience exclusions. Should these be pre-computed Gold fields or derived from `lapsed_buyer_status_key`?
* B7. LiveRamp receives `brand_mdm_id` — confirm this maps to which Gold Layer ID.

**For Thomas & Oli (Genie):**
* B8. Does Genie/reporting need snapshot-level data for trending dashboards? This is the most impactful question for the data model.
* B9. The BAR dashboard (PowerBI) uses 52 pre-computed KPIs from `cdp__bar_kpi_v`. Is this table staying as-is in Gold, or being refactored?
* B10. CLV is computed quarterly from `vw_fact_order_sales`. Should the Gold Layer include a pre-computed CLV, or should Genie compute it on-the-fly?

---

### C. Definition Alignment Questions

**Q4. What is a "contactable" customer?**
Current DDX Scorecard definition: `email_contactability_key = 'Y' OR sms_double_optin = 'SSOI'`
SuperGold fields: `email_perm_status`, `sms_double_optin` in `cdp__contactability_v`
➡️ Need to confirm: does `email_perm_status` map exactly to `email_contactability_key`? What values does it take?

**Q5. How is "engagement" defined?**
DDX Scorecard uses: click or open in the last 12 months (from `last_engagement_date_key`)
BAR KPIs use: `active_engaged_last_12_months`, `email_active_and_engaged_last_12_months`
Liveramp uses: `engaged_prospects_l12m`
➡️ These may be three different definitions. Need one Gold Layer definition.

**Q6. What is a "new buyer"?**
DDX Scorecard: `12_months_new_buyer_key = 'DDM_12NB_NB'` (acquired within 12M)
BAR KPIs: `customer_buyer_type` = 'Active : Newly Acquired Buyer' (based on acq_tenure + buyer type)
SuperGold: `new_buyer_status_key` in `cdp__transactional_kpis_v`
➡️ Need to align on one definition. The BAR adds nuance (Converted Prospect vs Newly Acquired).

**Q7. Churn definition alignment**
Liveramp: `churn_12_24_flag`, `churn_24plus_flag` (binary flags)
Supergold: `lapsed_buyer_status_key` (status key)
KPI Catalog: "customers who have not purchased in the last 12 months"
➡️ These need to be reconciled into one Gold definition. Are 12-24M and 24M+ granularities needed or just a single churn flag?

---

### D. Operational & Process Questions

**Q8. Canada-specific fields — where do they go?**
The SuperGold is built by US. Canada has specific needs:
* `preferred_language` (EN/FR) — critical for bilingual campaigns
* `brand_country = 'CAN'` filtering
* Canadian excluded brands (SHUUS, BIOUS, DER, BO)
* French-language campaign support in SFMC

➡️ How are Canada-specific attributes handled in the shared SuperGold model?

**Q9. Data refresh frequency alignment**
BAR KPIs: Monthly refresh
CLV: Quarterly refresh
Campaign Performance: Monthly refresh
Liveramp: Weekly/as-needed
➡️ Does the Gold Layer refresh accommodate all these cadences?

**Q10. What about the DDX-to-Gold migration path?**
Current reports query `crm_reporting.*` and `crm_base.*` tables directly. The Gold Layer introduces new `cdp__*` tables. What is the migration plan?
* Dual-write period?
* View compatibility layer?
* Which reports migrate first?

---

### E. Missing from the KPI Catalog

Comparing the Excel KPI Catalog (~80 defined KPIs) against what Canada actually uses in reports, I noticed these **Canada-used KPIs not clearly in the catalog**:
* **In/Out Flow** (Email Optins − Email Unsubs per period) — key executive KPI, not in the catalog
* **Media Addressable** count — used in scorecard, not defined in catalog
* **Campaign Attribution by Lookback Window** (3/5/7 day) — attribution methodology not standardized in catalog
* **Send Time Optimization metrics** — present in Campaign Performance notebook but not in catalog
* **New Repeat Rate** (new buyers who repeat in same window) — used in scorecard, not in catalog
* **Retained vs Reactivated buyer breakdown** — in reports but not explicitly defined in catalog
