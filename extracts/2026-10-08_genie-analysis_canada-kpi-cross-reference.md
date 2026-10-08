# Extract: Genie analysis, Canada reporting KPIs vs SuperGold

- Type: analysis notebook output (Databricks Genie), pasted by Bastien
- Date of input: 2026-10-08
- Original: raw/2026-10-08_genie-analysis_canada-kpi-cross-reference.md
- Ingested: 2026-10-08
- What it did: compared four Canada reports with the "All Domains - SuperGold" sheet of the US workbook (479 field rows in 21 cdp__ views) and listed gaps, mapping problems and questions for the upcoming **KPI catalog workshop**.
- Reports analysed and their source tables: DDX CA B2C Executive Report, DDX Scorecard (`fact_customer_segment_by_brand`); same report, CLV Deepdive (`vw_fact_order_sales`); CA B2C Campaign Performance Report (`fact_message_tracker`); Liveramp Customer 360 Canada dashboard (`vw_customer360_liveramp`).

## Result in one table (32 report KPIs)
| Status | Count | Examples |
| --- | --- | --- |
| Present in SuperGold | 14 | total contacts, active/new/repeat/retained/reactivated buyers, order frequency, send/open/click, campaign revenue, email coverage, loyalty active |
| Name or ID mismatch, or partial | 8 | contactable (email_contactability_key vs email_perm_status), brand_mdm_id vs brand_customer_id, AOV only as bucket, net spend lacks LY/LY2, media addressable, campaign attribution lookback, iOS open filtering |
| Gap (not in SuperGold) | 10 | snapshot/time dimension, new consumer status keys (1M, 12M, YTD), email opt-in and unsubscribe dates, new contacts contactable, In/Out change, CLV, retention rate, engaged prospects L12M flag, churn 12-24 / 24+ flags, segment_type |

## Gaps and mismatches reported
1. **Snapshot dimension (critical):** Canada's executive reports are monthly snapshots (`snapshot_year_month`); SuperGold is current-state only.
2. New consumer status keys (`1_month_`, `12_months_`, `ytd_new_consumer_status_key`) are missing.
3. First email opt-in date and email unsubscribe date are missing (only `email_perm_status_modified_dt`).
4. CLV (retention x AOV x frequency) and retention rate are computed, not fields.
5. `engaged_prospects_l12m`, `churn_12_24_flag`, `churn_24plus_flag` are missing; churn may derive from `lapsed_buyer_status_key`.
6. `segment_type` (RFMT, Churn Prediction 12M, Likely to Convert 3 Months, Product Affinity...) is missing; `cdp__bar_customer_models_v` uses `model_name` / `segment_value`.
7. IDs: Canada uses `brand_mdm_id` / `global_mdm_id` (Reltio MDM); SuperGold uses `brand_customer_id` / `global_customer_id`.
8. Contactability naming and AOV bucket versus exact value (see table).

## Open questions raised (for the KPI catalog workshop)
- Q1 historical snapshots or current state only? Q2 where do derived KPIs live (pre-computed or formula)? Q3 identity: same IDs or different resolution stages?
- Definitions to align: Q4 "contactable", Q5 "engagement" (three definitions in use), Q6 "new buyer" (scorecard vs BAR), Q7 churn.
- Q8 Canada-specific fields: `preferred_language` EN/FR, `brand_country = 'CAN'`, excluded brands (SHUUS, BIOUS, DER, BO), French-language campaigns in SFMC.
- Q9 refresh cadence: BAR monthly, CLV quarterly, campaign performance monthly, Liveramp weekly or as needed. Q10 migration path from `crm_reporting.*` / `crm_base.*` to `cdp__*`.
- Team questions B1 to B4 (Sandra, SFMC/Attentive), B5 to B7 (Damien, LiveRamp), B8 to B10 (Thomas and Oli, Genie).
- Canada-used KPIs it says are missing from the catalog: In/Out Flow, Media Addressable, campaign attribution by lookback window (3/5/7 days), Send Time Optimization metrics, New Repeat Rate, Retained vs Reactivated breakdown.

## Verification by Claude against the workbook (2026-10-08)
- Checked 44 field names. All "present" claims are correct, and all named gaps are really absent from the sheet: the new consumer status keys, `first_email_opt_in_date_key`, `email_unsubscribe_date`, `engaged_prospects_l12m`, the churn flags, `segment_type`, `email_contactability_key`, `brand_mdm_id`. No CLV, retention or snapshot field exists.
- The "479 fields across 21 tables" figure is right. **My own earlier count of 454 was wrong**: I skipped 25 rows that have a field name but no business term (recent additions). Corrected in the workbook extract.
- `preferred_language` is already in SuperGold (`cdp__identity_v`, added without a business term), so Q8 is partly answered: it exists; whether it is populated for Canada is not known.
- Genie says the KPI catalog has about 80 KPIs. The visible sheet "D2C KPI Catalog - LU 5-8" has 958 rows (many are LY/YoY variants), and a hidden "KPI Catalog" sheet has about 198 rows. Which one Genie used is unknown.
- `unsubscribed_cnt` exists in `cdp__campaign_int_metrics_v` (a campaign-level count), not a customer-level unsubscribe event date, so gap 3 stands.

## What this does and does not answer from my prompts
- Answers: whether the Canada reporting KPIs from four reports are covered by the SuperGold definitions (design level), and the main gaps.
- Does not answer: which Canadian tables hold which fields, fill rates, value differences, nor coverage of the other KPI catalog sections (Product, Data Health, Loyalty, Data Profile) or of other reports. Prompts A and B (data level) remain useful; Prompt C is only needed for uncovered sections.
