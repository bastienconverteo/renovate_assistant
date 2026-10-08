# Databricks Genie prompts: Canada coverage of the US SuperGold layer

How to use
1. Open Genie (or the Databricks assistant) on the tables that hold the Canadian data. Attach `Gold Layer Domain Data Requirements.xlsx` (copy in `raw/`).
2. Paste Prompt A, read the answer, then run Prompt B once per batch listed below and Prompt C per KPI section.
3. Paste each answer back to Claude with "ingest the Databricks answer". Claude archives it, compares it with the registers and proposes changes. Never skip the paste-back: the answers are the evidence for the datapoints and KPI registers.
Tip: if Genie truncates or answers vaguely, shrink the batch or ask it to continue ("continue from field N").

---

## Prompt A: orientation (run first)

I am the project manager for the Canada side of "Renovate", a project that builds a common "super gold" data layer for the Americas (USA, Canada, LATAM). The USA team already built the attached workbook "Gold Layer Domain Data Requirements.xlsx". Canada wants to reuse as much of it as possible and add new fields where needed.

Use only these sheets and ignore the hidden ones:
- "All Domains - SuperGold": columns Domain, Sub-Domain, Business Term, Current SG Field Name, Current SG Table, Business Definition, Survivorship Rules.
- "Values Dictionary - SuperGold": allowed values and meanings per attribute.
- "D2C KPI Catalog - LU 5-8": the KPI list (Metric name, Business definition, Technical definition, Section).

Step 1 only. Using the tables you can access, list every table or view that holds Canadian data (customers or consumers, contacts and consent, orders and order lines, campaigns and campaign interactions, loyalty, products, web or app events, predictive or beauty profile data). For each give: full name, short description, row count, date range, and whether it looks like a Canadian equivalent of one of the SuperGold views named in the workbook (for example cdp__identity_v, cdp__contact_info_v, cdp__order_header_v).

Rules: read-only queries, aggregates only, no personal data in the output. If you cannot tell something, write "unknown" instead of guessing. End with the list of questions you need answered before the next step.

---

## Prompt B: field coverage per batch (repeat for each batch)

Step 2, batch: **<Domain> / <Sub-Domain>** (see the batch table below).

For every field of this batch in the sheet "All Domains - SuperGold", tell me for Canada:
- canada_source: the table.column that holds it, or "none"
- status: one of available_as_is, available_needs_transformation, partial, not_available, unknown
- fill_rate_pct and rows_tested (how you measured it)
- value_set_diff: differences against the allowed values in "Values Dictionary - SuperGold" (list them), or "same"
- definition_diff: differences in meaning or format compared with the US definition, or "same"
- survivorship_ok: Y or N, whether the stated survivorship rule can be applied to the Canadian data
- sql: the short query you used

Then list the columns that exist in the Canadian tables for this sub-domain but are NOT in the workbook and could be useful as new fields, with a short reason.

Return two CSV blocks (text, comma-separated, with header):
1. `domain,sub_domain,field_name,sg_table,canada_source,status,fill_rate_pct,rows_tested,value_set_diff,definition_diff,survivorship_ok,sql,comment`
2. `domain,sub_domain,canada_source,description,fill_rate_pct,reason` (candidate new fields)

Rules: read-only, aggregates only, no personal data in the output, one row per field, "unknown" rather than assumptions, and state any filter you applied (for example brand or date range).

### Batches (field counts from the workbook)
| Batch | Domain: Sub-Domain (fields) |
| --- | --- |
| 1 | Customer: Identity (10), Contactability (11), Acquisition Data (7) |
| 2 | Customer - Contacts: Contact Info (26) |
| 3 | Customer: Loyalty (26); Interactions: Loyalty Interactions (10) |
| 4 | Customer: BMDM (Beauty Data) (53); Customer - AA Models: Predictive attributes (8) |
| 5 | Customer: 3P Demographic Data (46) |
| 6 | Customer: Interaction KPIs (7), Acquisition / Interaction KPIs (5); Interactions: Interaction Tracking (9) |
| 7 | Transactions: Order Header (30), Order Line (26), Line Adjustments (4) |
| 8 | Customer: Transactional KPIs (22), BAR KPI (52) |
| 9 | Campaign: Campaign Master (26), Campaign Interactions (28) |
| 10 | Product: Product Dimensions (27) |
| 11 | Website Browsing (GA4): Daily event table (11), User view (10) |

---

## Prompt C: KPI coverage per section (repeat per section)

KPI coverage, section: **<Executive | Product | Data Health | Loyalty | Campaign | Data Profile>** of the sheet "D2C KPI Catalog - LU 5-8".

For each KPI row of that section (columns Metric name, Business definition, Technical definition), tell me whether it can be computed for Canada with the available tables:
- status: computable, computable_with_gaps, not_computable or unknown
- depends_on_fields: the SuperGold field names it needs, using names from "All Domains - SuperGold" where possible
- missing_fields: fields it needs that are not available for Canada
- used_in_reports: the name of any existing Canadian report, dashboard or table where this KPI (or an equivalent) is already used, or "none found"
- sql_or_logic: the short calculation
Variants of the same KPI (for example "- LY" and "- YoY") can be grouped on one row, with the variants listed in the comment.

Then list the KPIs used in existing Canadian reports or dashboards that are NOT in the catalog.

Return CSV text with header: `kpi_id,metric_name,section,status,depends_on_fields,missing_fields,used_in_reports,sql_or_logic,comment`, followed by a second CSV of the KPIs that are in reports but not in the catalog: `report_or_table,kpi_name,definition_or_logic`.

Same rules: read-only, aggregates only, no personal data, "unknown" rather than assumptions.
