# Extract: Genie answers + Renovate data context reference

- Type: Genie analysis (Databricks)
- Date of input: 2026-10-14
- Original: raw/2026-10-14_genie-answers_data-context-reference.md
- Author: Databricks Genie, prompted by Bastien with section E of the open-questions table
- Ingested: 2026-10-14 (SRC-0013)

## Key points (documented = Genie queried Databricks; analysis = Genie's interpretation)
- Two worlds: PII side `stg_canada_catalog.crm_base` (cleartext, unhashed IDs) and analytical side `prod_canada_catalog.crm_reporting / crm_analytics` (md5-hashed IDs). A fixed hashing rule joins them (see raw, section 1.1). [documented]
- IDs: brand_customer_id : brand_mdm_id = 1:1 (10.5M each); brand_mdm_id → global_mdm_id 10.5M → 8.0M. "Same IDs, different names" is Genie's reading of a 1:1 count, not a value comparison. [analysis, to confirm]
- Backbone table `fact_customer_segment_by_brand`: customer × brand × month, 58 monthly snapshots Jan 2022 → Oct 2026, monthly refresh; holds status keys (buyer, new buyer, repeat, retained, reactivated, new consumer 1M/12M/YTD), contactability, last engagement, churn key, pref_language. [documented]
- Churn key buckets (Oct 2026): N/A 6.07M, active L12M 514K, lapsed 12-24M 383K, lapsed 24M+ 1.09M. LiveRamp churn flags are derived from it in the view. 12-36 needs a split of 24M+ by last purchase date. [documented]
- US Gold `lapsed_buyer_status_key` (DP-0139) buckets: ... 366-730 days (24LB), 730-1095 (36LB), >1095 (36PLB) → 12-24, 24+ and 12-36 all derivable. [analysis by Claude from workbook]
- Scorecard `pbix_2bc_scorecard`: brand × month, 58 months, Monday job; KPI definitions listed (contactable, active buyers 1M/3M/12M/YTD, new contacts, opt-in/unsub, new/repeat/new-repeat buyers, retained, reactivated, media addressable, click-or-open 12). [documented]
- CLV table: brand × segment × quarter, 16 quarterly snapshots Dec 2022 → Sep 2026. [documented]
- Derived KPIs in 2+ reports: retention rate, AOV, engagement rate, new repeat rate, DDX revenue. In 1 report: CLV, In/Out flow, media addressable, campaign attribution 3/5/7d, churn rate. Formulas in raw section 3. [documented]
- Counts Oct 2026: 8,034,882 customers; contactable 4,945,619 (61.6%); email 4,621,106; SMS 794,383; engaged 4,134,644; active buyers L12M 514,260; new buyers L12M 283,346, YTD 163,339; repeat L12M 137,160; retained 169,688; reactivated 64,655. [documented]
- Report inventory: DDX Scorecard, DDX Engagement KPIs, CLV Deepdive, Campaign Performance, LiveRamp Customer 360, DDX Quarterly Figures, with tables read. [documented]
- Refresh: message tracker daily, order sales daily, segment snapshot monthly, scorecard monthly, customer360 monthly, CLV quarterly. [documented]
- Canada specifics: pref_language 18 values, 29% unknown; SHUUS/BIOUS always excluded, DER/BO in some contexts, AEO excluded from retention and new repeat rate; ACD = LDB; Canada-only brands BIOCA, GAB; CAD. [documented / analysis]
- New gaps from Genie: AOV buckets vs exact (CLV); customer-level sub-categories; PII accessibility for activation (critical). [analysis]
- Stakeholders: Genie names **Shabri** (USA PM, SuperGold owner, schema design authority) and "Olivier" (= Oli). [analysis, to confirm]
- Assets: notebook paths and IDs for Scorecard, CLV, Campaign Performance, Bastien's RENOVATE and quarterly figures notebooks; LiveRamp dashboard UUID (raw section 11).

## Contradictions / to verify
- Genie gap 5 says churn key does not map 1:1 to LiveRamp flags; section 2.1 says the flags are derived from it.
- Engaged 4.13M of 4.95M contactable (84%) looks high for click/open L12M.
- Bastien (2026-10-09): SHUUS, BIOUS, DER, BO excluded by Canada; Genie: exclusions differ by KPI.
- Records: Deepti defines Gold; Genie: Shabri is schema design authority.
- LiveRamp file weekly (Damien) vs source view monthly.
- "Buyer Analysis" report used in KPI formulas but absent from the report inventory.
- "21 cdp__ views" vs Genie's table of 20 views summing to 479 fields.

## Sensitive content
- Raw section 1.1 contains the ID hashing rule including its salt. Keep the repo private; do not quote it in emails or decks.
