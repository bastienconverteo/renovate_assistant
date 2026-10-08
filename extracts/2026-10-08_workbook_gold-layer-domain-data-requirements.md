# Extract: Gold Layer Domain Data Requirements (workbook)

- Type: workbook (xlsx, 1.9 MB, 41 sheets of which 12 visible and 29 hidden)
- Date of input: last modified 2026-10-06 (file timestamp); latest backlog entry created 2026-09-09
- Original: raw/2026-10-08_workbook_Gold-Layer-Domain-Data-Requirements.xlsx
- Author: the US team (per Bastien); contributors named in the backlog are listed below
- Ingested: 2026-10-08
- Method: values read with a script; formulas not evaluated; data stays in the raw file.

## What the workbook is for (READ ME sheet, documented)
Business requirements for the data in the Gold Layer, by domain and sub-domain, to guide the tech teams building the final tables. Fields are a curated subset drawn from: the Global Granular Data Model (GDM, mandated analytics model), One Consumer Profile (mandated activation model) and the LUSA B2C Business Glossary. The READ ME states that three sheets are the sources of truth for what must be in the gold layer: **All Domains**, **BAR Activation KPIs** and **KPI Catalog**.

## Visible sheets
| Sheet | Size | What it holds |
| --- | --- | --- |
| All Domains - SuperGold | 479 field rows (357 distinct field names) | The "super gold" field list: domain, sub-domain, business term, current SG field name, current SG table, business definition, survivorship rule |
| Values Dictionary - SuperGold | 64 attributes with allowed values | Value lists and meanings per attribute (HighTouch attribute name, gold attribute name) |
| Diamond Schema BRD | about 570 rows | Target state ("Diamond") of the same fields: optional rename and Diamond table |
| Diamond Row-By-Row Changes | about 580 rows | Per field: type of change for Diamond, reason, possible CDP impact (RAG), renamed column; plus a table of change categories |
| D2C KPI Catalog - LU 5-8 | 958 numbered KPI rows (926 named) | Reporting KPI catalog (see below) |
| BAR Activation KPIs | 20 filters | Activation segmentation filters with category, buckets, definition, priority |
| All Domains - Gold | about 420 rows | Earlier gold-layer field list with prioritisation columns (in GDM? in One Consumer Profile? in C360? LiveRamp? Attentive?) |
| Event - Parameter Pairings | about 300 rows | GA4 event and parameter pairs, with an include-in-gold flag |
| DDX Renovate Backlog | 82 items | Backlog BL-003 to BL-085 |
| Backlog Attr Impact to Wave 1 | 28 items | Impact of backlog attributes on CDP wave 1 |
| Prod Deployments Aug2026 | about 100 rows | Value changes deployed to production in August 2026 (story, HT name, column, table, value, release date) |
| READ ME / TAXONOMY GUIDE | | Guide and key concepts |

30 hidden sheets are older versions, gap analyses, data quality and BAR variants (e.g. All Domains (Old Version), KPI Catalog, D2C KPI Catalog - LU 2-21 (WIP), BAR Activation KPIs - old, Renovate Timeline, Gap Analysis, SG Data Quality Backlog, DQ Insights). They were not analysed in this pass.

## SuperGold field list (documented)
- 479 field rows (357 distinct field names, because the same field repeats across views) in 8 domains: Customer 245; Transactions 76; Campaign 54; Customer - Contacts 27; Product 27; Interactions 21; Website Browsing (GA4) 21; Customer - AA Models 8. Correction 2026-10-08: the first version said 454 because it skipped 25 rows that have a field name but no business term (recent additions such as preferred_language).
- Spread over 21 SuperGold views (cdp__...), largest: beauty profile 54, BAR KPIs 52, 3P demographic 46, order header 30, campaign interaction metrics 28, contact info 27, order line item 27, product hierarchy 27, loyalty 26, campaign master 26.
- Two fields point to cdp__acquisition_interaction_data_v with the note "to be relocated to cdp__transactional_kpis_v".
- Survivorship rule given for 445 of 479 field rows.
- The sheet is US-based: the definition of Brand Country says "For LUSA, will be 'USA'". No LATAM or Canada indication per field. (inferred: coverage for LATAM and Canada is unknown)

## KPI catalog "D2C KPI Catalog - LU 5-8" (documented)
- 958 numbered rows, 926 with a metric name. Columns include funnel step, KPI category and sub-category, metric name, type, section, page, periods, breakdowns, filters, business definition, technical definition, "Databricks check" and "Genie check".
- Sections: Executive 385, Product 242, Data Health 155, Loyalty 84, Campaign 61, Data Profile 31.
- Validation status: "Databricks check" filled on 37 rows (35 OK, 2 KO); "Genie check" filled on 3 rows (all KO). So the check that reporting KPIs can be computed from the gold layer has barely started.
- Many rows are variants of one KPI (e.g. "Total records", "- LY", "- YoY").

## BAR Activation KPIs (documented)
20 filters in categories: Baseline, Demographic profiling, Profile spend, RFM profile, Engagement profile and "NOT in BAR" (email and SMS active and engaged at 6 and 12 months). Change log entries dated 01/12/25 (AOV buckets 300-350 and 350+ added for CDP; 12-month email filter added to align with SMS).

## DDX Renovate Backlog (documented)
- 82 items. Status: Done 46, Deprioritized 12, Backlog 10, In Progress 6, Blocked 6, In Review 2. Priority: Critical 5, High 30, Medium 31, Low 13.
- Epics: Data Quality 29, Wave 1 29, Journey Migration 16, Wave 2 6, New Schema 1.
- Most frequent reporter: Ian Cidade (44 items); others: Alexis Turbet Delof 12, Fatima Ahmed 4, Ellie Chen 3, Allen Volkov 3, Jade Li 3, Daniel Basman 3. Reporter is not necessarily the owner.
- Blocked items:
  - BL-055 and BL-056: add geotracking and operating system info from Attentive and SFMC to contact info. Blocked because SFMC and Attentive are not sending the data, even though the pipelines are set up. Target delivery estimate 2026-08-05 (past).
  - BL-065, BL-066, BL-067: primary email, phone and address attributes. Blocked: rules definition work in progress.
  - BL-081: nullify 1900-01-01 birth dates on identity. Pending SFMC feedback on rule details.
- BL-068 and BL-075 (Attentive event cleansing and filtering on campaign interactions) are In Review and were "rolled back in Aug 21".
- In progress: BL-045 GA4 table structure, BL-076 loyalty event grouping, BL-085 Diamond schema creation and deployment (High), BL-077 mass_merchandise attribute (Wave 2), BL-017/018 order line standardisation.
- Wave 1 impact sheet: of 28 items, 5 count as "count impact" (e.g. birth month/day logic, order header and order line deduplication logic, Attentive event type change), 10 new attribute with no impact, 5 logic change with no impact, 2 simplify the Hightouch configuration.

## Observations (inferred)
1. The email sent to the data teams points them to "All Domains - SuperGold", while the READ ME names "All Domains" (a hidden sheet), the BAR sheet and the KPI Catalog as sources of truth. Confirm which sheet is the master for additions.
2. "Check that all reporting KPIs exist in this file" needs a list of the KPIs used in reporting. That list is not in this workbook as such; the closest candidates are the 958-row KPI catalog and the 52 BAR KPI fields in cdp__bar_kpi_v.
3. LATAM and Canada are not represented per field; the register will mark them unknown until a country-level check is made.

## Open questions
- What is the source list of KPIs actually used in reporting?
- Is "Diamond" the target schema that will replace SuperGold, and who approves its row-by-row changes?
- Deadline for the data teams' replies?
