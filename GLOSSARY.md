# Glossary

Meanings marked (?) are inferred and need confirming. Add terms, synonyms and country codes as they appear.

| Term | Meaning | Source / notes |
| --- | --- | --- |
| Renovate | Programme building the new Databricks data foundation (medallion layers, gold) for the Americas consumer data; "from Renovate to Elevate" in the March 2026 deck | Elevate deck |
| Elevate | Next phase after Renovate (scale and optimise the Americas consumer data ecosystem) | Elevate deck |
| DDX | The consumer data platform ("Next Gen DDX") that Renovate and Elevate rebuild | Elevate deck (?) |
| Gold layer / SuperGold (SG) | The common curated layer. "SuperGold" is the US-built design: cdp__ views listed in the workbook sheet "All Domains - SuperGold" | US workbook |
| Diamond schema | Target schema planned to replace SuperGold; workbook sheets "Diamond Schema BRD" and "Diamond Row-By-Row Changes" | US workbook |
| Medallion | Bronze / silver / gold layering in Databricks | Elevate deck |
| CDP | Customer data platform | Elevate deck |
| IDR | Identity resolution (and survivorship) | Elevate deck |
| MDM, Reltio | Master data management; Reltio is the MDM tool. Canada IDs are brand_mdm_id / global_mdm_id | Elevate deck; Genie analysis |
| Hightouch (HT) | Activation tool; its IDR role was under validation in March 2026 | Elevate deck |
| SFMC | Marketing automation platform (likely Salesforce Marketing Cloud, ?) | Bastien's email |
| Attentive | SMS marketing platform | Bastien's email |
| LiveRamp | Audience activation platform | Bastien's email |
| Genie | Databricks Genie (natural-language data assistant) and the Genie / reporting data team (Thomas, Oli) | Bastien |
| C360 | Customer 360 view (crm_base.customer360 and Liveramp view vw_customer360_liveramp) | Workbook; Genie analysis |
| CRM Base / CRM Reporting | Legacy table sets (crm_base.*, crm_reporting.*) that current Canada reports query; access is going away | Workshop 1 |
| BAR | Activation KPI set / dashboard (PowerBI) built on cdp__bar_kpi_v; expansion of the acronym unknown | Workbook |
| BMDM | Beauty data model ("Beauty Data", beauty profile) | Workbook |
| GDM | Global Granular Data Model, the mandated analytics data model | Workbook |
| One Consumer Profile | The mandated activation data model | Workbook |
| LUSA | L'Oréal USA | Workbook (?) |
| D2C KPI Catalog | US catalog of KPIs (sheet "D2C KPI Catalog - LU 5-8"); baseline for the Canada catalog | Workbook |
| "Goal layer" | How the workshop summary version 2 writes "Gold layer" (transcription slip) | Workshop 1 v2 |
| T2C KPI catalog Canada | Name used for the Canada KPI sheet in version 2; probably the D2C KPI Catalog (?) | Workshop 1 v2 |
| Canada KPI Catalog | Dedicated catalog Deepti will create from the US baseline | Workshop 1 |
| Match / Gap / New | Classification of each US KPI for Canada: adopt as-is, Canada-specific adjustment, missing/new | Workshop 1 |
| Consumer funnel | Acquisition, engagement, conversion, retention, loyalty steps used to group KPIs | KPI catalog |
| DDX Scorecard | Canada B2C executive report (monthly snapshot, source fact_customer_segment_by_brand) | Genie analysis |
| Snapshot | Monthly stored state of customer segments (snapshot_year_month) | Genie analysis |
| In/Out flow | Email opt-ins minus unsubscribes per period | Genie analysis |
| CLV | Customer lifetime value = retention x AOV x frequency (computed) | Genie analysis |
| AOV | Average order value | Workbook |
| RFMT | Segment type used by LiveRamp (expansion unknown) | Genie analysis (?) |
| SSOI | Value of sms_double_optin meaning opted in | SRC-0013 |
| MTD / YTD / YoY / R12 / LY | Month to date, year to date, year over year, rolling 12 months, last year | KPI catalog |
| WAF | Well Architecture Framework (enhancement of the DDX architecture) | Elevate deck |
| Lakebase | Databricks operational database planned to replace Cassandra | Elevate deck |
| B2C / B2B | Consumer and professional businesses; B2C moves first | Elevate deck |
| USA / Canada / LATAM | The three regions in scope; LATAM countries to list when known | Bastien |
| Excluded brands (Canada) | Per use case. SHUUS and BIOUS excluded by default; no other brand unless specified (DEC-0022). Genie: DER, BO in some contexts; AEO (Aesop) in retention and new repeat rate | Bastien 2026-10-14; SRC-0013 |
| LR | LiveRamp (abbreviation used by Damien) | Damien reply 2026-10-08 |
| Is_Churn_12M_36M | One flag for the 12-36 month churn window, requested by Damien to create the lapsed buyers segment | Damien reply 2026-10-08 |
| Sub-categories | Product sub-categories (anti-aging, suncare...) finer than product_category, requested by Damien | Damien reply 2026-10-08 |
| LR for RENOVATE.xlsx | Sample of the LiveRamp weekly file with Damien's two added columns (51 columns); lives in inbox/, not committed because it holds personal data | Bastien 2026-10-08 |
| LUSA SuperGold | The US (L'Oréal USA) SuperGold, owned by Shabri; Deepti owns the Americas Gold and takes final decisions | Bastien 2026-10-14 |
| crm_base / crm_reporting / crm_analytics | Canada legacy schemas: crm_base = PII side in stg_canada_catalog (cleartext IDs); crm_reporting and crm_analytics = analytical side in prod_canada_catalog (md5-hashed IDs) | SRC-0013 |
| fact_customer_segment_by_brand | Canada backbone table: customer x brand x month snapshot, 58 months since Jan 2022 | SRC-0013 |
| churn_status_key | Canada churn key: DDM_CHRN_NA, DDM_CHRN_L12M (active), DDM_CHRN_L12_24M, DDM_CHRN_L24M_PLUS | SRC-0013 |
| pref_language | Canada language field (18 raw values, 29% unknown); called preferred_language in SuperGold | SRC-0013 |
| ACD / LDB | ACD in some tables = LDB (L'Oréal Dermatological Beauty) | SRC-0013 |
| BIOCA, GAB | Canada-only brands: Biotherm Canada, Giorgio Armani Beauty Canada | SRC-0013 |
| AEO | Aesop brand code | SRC-0013 |
| Buyer Analysis | Canada report named in KPI formulas, missing from Genie's report inventory | SRC-0013 |
| source_customer_id | ID as it arrives from a source system (Salesforce/Demandware, MARS, CEGID); one customer can have several | Genie 2026-10-14 (raw/2026-10-14_genie-answer_ddx-id-hierarchy.md) |
| brand_mdm_id / brand_customer_id | Both brand-level IDs (same identity level) but two distinct ID systems: 1:1 mapping, values never equal (0 of 14.2M rows). Join via dim_customer_bridge. LiveRamp uses brand_mdm_id; SuperGold lists brand_customer_id | Genie 2026-10-14 (value check) |
| global_mdm_id / global_customer_id | Cross-brand person ID (one person across brands); ~10.5M brand IDs → 8.0M global IDs in Canada. Same renaming as above | Genie 2026-10-14 |
| ID uniqueness | Canada IDs are unique only per brand_code: always join on brand + ID | Genie 2026-10-14 |
