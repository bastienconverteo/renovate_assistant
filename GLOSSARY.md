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
| SSOI | Value of sms_double_optin meaning opted in (?) | Genie analysis (?) |
| MTD / YTD / YoY / R12 / LY | Month to date, year to date, year over year, rolling 12 months, last year | KPI catalog |
| WAF | Well Architecture Framework (enhancement of the DDX architecture) | Elevate deck |
| Lakebase | Databricks operational database planned to replace Cassandra | Elevate deck |
| B2C / B2B | Consumer and professional businesses; B2C moves first | Elevate deck |
| USA / Canada / LATAM | The three regions in scope; LATAM countries to list when known | Bastien |
| Excluded brands (Canada) | SHUUS, BIOUS, DER, BO (to confirm) | Genie analysis |
| LR | LiveRamp (abbreviation used by Damien) | Damien reply 2026-10-08 |
| Is_Churn_12M_36M | One flag for the 12-36 month churn window, requested by Damien to create the lapsed buyers segment | Damien reply 2026-10-08 |
| Sub-categories | Product sub-categories (anti-aging, suncare...) finer than product_category, requested by Damien | Damien reply 2026-10-08 |
| LR for RENOVATE.xlsx | Sample of the LiveRamp weekly file with Damien's two added columns (51 columns); lives in inbox/, not committed because it holds personal data | Bastien 2026-10-08 |
