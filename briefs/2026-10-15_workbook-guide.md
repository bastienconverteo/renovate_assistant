# How the US Gold workbook works (and what Canada needs)

Source: `raw/2026-10-08_workbook_Gold-Layer-Domain-Data-Requirements.xlsx` (43 tabs: 13 visible, 30 hidden), reviewed 2026-10-15 after workshop 2. Row numbers refer to the original file.

## 1. The three layers it describes

| Layer | What it is | Who uses it | Tab |
|---|---|---|---|
| **Gold** | Full requirement list of fields, by domain, with their DDX source table | Analytics, reporting, data engineering | All Domains - Gold (hidden "All Domains" = newer, fuller version) |
| **SuperGold** | `cdp__*` views built for the CDP (Hightouch). Curated subset of Gold, renamed, cleaned, one row per customer per brand where possible | Activation (Hightouch, SFMC, Attentive) | All Domains - SuperGold, Values Dictionary - SuperGold |
| **Diamond** | Next version of SuperGold: same tables, 30 fields removed, 15 renamed, 2 moved | Activation, once deployed | Diamond Schema BRD, Diamond Row-By-Row Changes |

KPIs sit on top of these layers: **KPI catalog** (all calculated metrics) and **BAR Activation KPIs** (customer-level buckets and flags used by the BAR audience-sizing report). Deepti, 2026-10-15: both were built in Gold. Andres: in future the reporting layer runs on Renovate as Databricks metric views, governed by IT.

The READ ME names three sources of truth: All Domains, BAR Activation KPIs and the KPI Catalog.

## 2. Tab by tab

### Visible tabs

| Tab | What it holds | Use for Canada |
|---|---|---|
| READ ME | Purpose, sources (Global GDM, Global One Consumer Profile, LUSA glossary), key concepts (1:1 vs 1:many) | Read once |
| TAXONOMY GUIDE | Each sub-domain mapped to its view in `prod_us_catalog.ddx_b2c_gold`. States that PII lives in `cdp__contact_info_v` (contact_type / sub_type / value) | Where each type of data sits |
| All Domains - SuperGold | 479 fields in 20 views. Columns: domain, sub-domain, business term, field, view, definition, survivorship | **Attributes.** Check here first |
| Values Dictionary - SuperGold | Allowed values and meaning for the coded fields (contactability key, buyer status keys, lapsed buckets, model names) | Check that Canada's codes map |
| Diamond Schema BRD | SuperGold rebuilt as the target "Diamond" schema, with optional renames. Rows 517-575 list fields deliberately left out and why | Map Canada to Diamond names, not SuperGold |
| Diamond Row-By-Row Changes | Change type per field (removal, renaming, addition) and CDP impact | See what disappears |
| D2C KPI Catalog - LU 5-8 | 958 KPI rows (686 distinct names), table `kpi_catalog`. Columns: funnel step, category, metric, type, section and page of the US D2C dashboard, period (R12 / YTD / MTD / till date / selected period), filters, business definition. Technical definition and checks mostly empty | **Calculated KPIs.** Check here before calling a KPI missing |
| BAR Activation KPIs | 21 customer-level filters of the BAR report (buyer status, % active engaged, spend buckets, RFM, AOV buckets, engagement windows) | Customer buckets used for audiences |
| All Domains - Gold | 418 Gold fields with DDX source, flags (GDM, One Consumer Profile, C360, LiveRamp, Attentive, KPI), priority. Rows 395-421 list excluded fields and why | Gold-only fields (e.g. brand MDM ID, global MDM ID) |
| Event - Parameter Pairings | GA4 event and parameter pairs kept in Gold | Only if Canada uses GA4 |
| DDX Renovate Backlog | ~80 enhancement stories (BL-xxx): adds, data-quality fixes, Diamond. Columns: type, title, domain, attribute, epic, priority, reporter, status, sprint, Wave 1 impact | **Where additions are requested** |
| Prod Deployments Aug2026 | Value changes released in August (e.g. contactability codes to labels) | Watch for code changes |
| Backlog Attr Impact to Wave 1 | Which backlog items change counts vs legacy (order dedup, birth date logic, Attentive events) | Expect count differences after migration |

### Hidden tabs (history and working files)
- **Renovate Timeline**: US plan Jan to May 2026 (P0, then sprints 1-4, KPI Catalog / Reporting April-May). Last line: "LATAM and Canada Integration with US Global workspace: not started, TBD".
- **All Domains, All Domains (Old Version), Customer / Contacts / Campaign / Transactions / Interactions, Business DQ Sheet**: earlier versions of the field list per domain.
- **KPI Catalog, D2C KPI Catalog - LU 2-21 (WIP)**: earlier KPI catalog versions (the older one has LUSA comments and the "80 KPIs for DDX Tech V1" flag).
- **BAR tabs (old, Clean, (2), Working F&D, Technical, Confidence)**: the BAR report's Power BI formulas, backend tables and SQL. Useful if Canada needs the exact BAR logic.
- **Gap Analysis tabs, Insights, OneConsumerProfile (Activation), GDM to DDX Mapping**: coverage of DDX vs global models.
- **SG Data Quality Backlog, DQ Insights, Data Standardization Gap Analysis, DBX&HT Prod Review**: data-quality tracking.
- **Attentive Gap Analysis**: Attentive data mapped to Gold. Shows US Attentive uses `brand_mdm_id` as a custom attribute.
- **Attributes Omitted**: glossary fields dropped and why.

## 3. What the US built
- 20 SuperGold views covering identity, contactability, loyalty, beauty profile, acquisition and interaction KPIs, transactional KPIs, BAR customer KPIs, TransUnion 3P data, AA model outputs, contacts (PII), orders (header, line, line detail), campaigns (master, interactions), loyalty events, interactions, GA4, product.
- Customer status keys already computed per customer: buyer, lapsed (6/9/12/24/36/36+ months), retained, repeat, reactivated, new buyer (in 3-month buckets), decile, order frequency, engagement windows, AOV and spend buckets.
- A KPI catalog that covers the whole US D2C dashboard: Executive, Data Health, Data Profile, Campaign, Loyalty, Product.
- A backlog process: every addition is a story with a reporter, a priority and a Wave 1 impact check.
- Data-quality rules written as backlog stories (label consolidation, code-to-value translation, language rule en/es).

## 4. What it does not cover (yet)
- Canada data: the plan has Canada integration as TBD.
- History: the Diamond BRD drops `snapshot_key` from SuperGold ("time travel not needed in super gold"). Deepti says snapshots exist on the Gold tables. So history lives in Gold, not in the CDP views.
- Brand exclusions per KPI: no column in the catalog.
- Technical definitions: almost all empty in the catalog.
- Canada specifics: French language (US Gold notes "language: cannot legally collect"; the US rule is en/es), CAD spend buckets, Canadian taxes, Canadian postal codes, Canada brands.
- Full date of birth: Gold notes "year of birth: we can no longer collect / store this info" (US policy).

## 5. Fields Diamond removes that matter to Canada
- `new_consumer_status_key` (Is New Consumer L12M): "not in active use". Canada's new-names keys can instead be derived from `acquisition_date_key`, which stays.
- `13mnths_consumer_email_open_status_key` / `click_status_key`: removed.
- `lapsed_consumer_status_key`: removed (covered by other keys).
- `sms_perm_status`: replaced by `sms_double_optin` (fits Canada's SMS rule).
- `snapshot_key` on the BAR KPI view: dropped from SuperGold.

## 6. What Canada needs to make this work
1. **Check both tabs before calling something missing.** Attributes in SuperGold (and Gold), calculated values in the KPI catalog, customer buckets in BAR.
2. **Write Canada's additions in the US format**: a row in the SuperGold or KPI catalog tab for discussion, then a backlog story once agreed.
3. **Turn Canada's data cleaning into requirements** (Andres): every standardisation the Scorecard, CLV and Campaign notebooks apply today goes to IT so it happens between bronze and silver.
4. **List Canada's analytical use cases beyond reporting** (Andres): CLV model, segment models, LiveRamp, SFMC and Attentive feeds.
5. **Plan the refactor**: `crm_reporting` disappears; `crm_analytics` stays; every Canada query moves to the new tables and names (Diamond).
6. **Agree the remaining definitions with Deepti**: engagement (Canada counts opens, the US does not), campaign attribution windows, media addressable, brand exclusions.
7. **Get dates**: Canada integration is TBD in the US plan.
