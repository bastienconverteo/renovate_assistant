# Workshop 2 prep – Canada questions for Deepti (2026-10-15)

For Bastien. One section per question added to the workbook copy `outputs/2026-10-15_Gold-workbook_Canada-questions-workshop-2.xlsx` (rows at the bottom of three tabs, refs CA-A / CA-K / CA-P).

Each entry: **why it's an issue**, **why we bring it up now**, **what we know**, **what we want from Deepti** (and our proposed position).

Source of the numbers: Genie on Canada Databricks, Oct 2026 snapshot (repo SRC-0013), Genie coverage check of 32 Canada KPIs (SRC-0003), US workbook (SRC-0002).

## Priorities for the meeting (if time is short)
1. Snapshots and history backfill (CA-A01, CA-P04). Without them, every Canada trend KPI breaks.
2. PII for activation (CA-A03). LiveRamp, SFMC and Attentive can't run without it.
3. Customer IDs (CA-A02). Canada has two different brand IDs (never equal); Gold must keep both or the bridge, or LiveRamp loses its key.
4. Derived KPIs: pre-computed or formula (CA-K01).
5. The 5 KPIs missing from the US catalog (CA-K05 to K09).
6. Timeline and sequencing (CA-P01, P02).

---

## Tab "All Domains - SuperGold" (attributes)

### CA-A01 Monthly customer snapshot
- **Issue:** Gold only keeps the current state of each customer. Canada's executive reporting runs on a monthly snapshot (customer x brand x month). Every trend, YoY and "as of month-end" number comes from it.
- **Why now:** it's the biggest gap Genie found (rated critical). It changes the Gold data model, so it must be decided before engineering starts.
- **What we know:** the Canada snapshot table has 58 months (Jan 2022 to Oct 2026) and refreshes monthly. The scorecard aggregates it (also 58 months).
- **Ask:** does the US plan a snapshot or history table? **Proposed position:** Gold keeps a monthly customer x brand snapshot with the Canada status keys.

### CA-A02 Customer IDs
- **Issue:** Canada has **two distinct brand-level IDs**: `brand_customer_id` and `brand_mdm_id`. They map 1:1 but are **never equal** (Genie, 0 of 14.2M rows in customer360). Joining one to the other needs the bridge table `dim_customer_bridge` (brand customer ID → brand MDM ID → global MDM ID). LiveRamp is keyed on the MDM IDs; Gold only lists `brand_customer_id` / `global_customer_id`.
- **Why now:** if Gold carries only one of the two IDs and no bridge, the LiveRamp export (and anything keyed on MDM IDs) loses its key. IDs are also unique only per brand, so every join must include the brand.
- **What we know:** 11.65M distinct brand customer IDs in customer360 (the earlier 10.5M figure came from the bridge table; different scope, to reconcile). Global MDM ID groups brand profiles about 1.32:1. IDs are md5-hashed on the reporting side, cleartext on the PII side.
- **Ask (Deepti / Andres):** is Gold's `brand_customer_id` Canada's brand customer ID or its MDM ID? Will Gold carry both IDs, or the bridge? Hashed or cleartext? **Proposed position:** Gold carries both brand IDs plus the global ID (or the bridge), always keyed with the brand.

### CA-A03 PII for activation
- **Issue:** LiveRamp, SFMC and Attentive need cleartext emails, phones and addresses. Today these sit in the PII schema (crm_base), separate from reporting.
- **Why now:** Genie flagged it critical. If Gold is hashed-only, all activation feeds lose their source when legacy access goes away.
- **Ask:** is PII in Gold, or in a separate export layer, and who owns the feeds?

### CA-A04 Contactable flags
- **Issue:** Canada counts a contact as contactable when the email contactability key = Y or SMS double opt-in = SSOI. Gold only has `email_perm_status`.
- **Why now:** contactable is a headline executive KPI. A different field means a different number after migration.
- **What we know:** Canada Oct 2026: 4.95M contactable of 8.03M (62%); 4.62M email, 0.79M SMS.
- **Ask:** can Gold carry both Canada fields? **Proposed position:** yes, keep the Canada rule.

### CA-A05 Opt-in and unsubscribe dates
- **Issue:** Gold has the email status and its last modified date, but not the first opt-in date or the unsubscribe date.
- **Why now:** In/Out flow (opt-ins minus unsubscribes, 1M / 12M / YTD) can't be computed without them.
- **Ask:** add `first_email_opt_in_date_key` and `email_unsubscribe_date`.

### CA-A06 New consumer status keys
- **Issue:** Canada's "new names" keys (1 month, 12 months, YTD) are not in Gold.
- **Why now:** the New Contacts and New Contacts Contactable KPI families break without them.
- **Ask:** add the three keys, or agree an equivalent.

### CA-A07 Churn / lapsed buyers
- **Issue:** LiveRamp uses churn flags 12-24 and 24+, and Damien asks for a 12-36 flag. Canada's current churn key stops at "24+", so 12-36 can't be built today.
- **Why now:** good news to confirm. The US Gold lapsed buyer key has 12-24, 24-36 and 36+ buckets, so all three flags can be derived from it.
- **What we know:** Canada Oct 2026: active L12M 514K, lapsed 12-24M 383K, lapsed 24M+ 1.09M.
- **Ask:** confirm Canada can use the US key. **Proposed position:** adopt it and derive the flags in the LiveRamp export.

### CA-A08 Exact AOV
- **Issue:** Gold only has AOV buckets. CLV needs the exact value.
- **Why now:** CLV Deepdive breaks without it.
- **Ask:** add an exact AOV (or the net sales and order counts to compute it).

### CA-A09 LiveRamp segment type
- **Issue:** LiveRamp filters on `segment_type` (churn prediction 12M, RFMT, likely to convert 3M, product affinity buyer / prospect). Gold stores model outputs as model name / segment value.
- **Why now:** LiveRamp audience filtering depends on it.
- **Ask:** confirm the mapping exists for the five Canada segment types.

### CA-A10 Engaged prospects L12M
- **Issue:** a LiveRamp flag with no Gold equivalent.
- **Why now:** it's in the current LiveRamp file, which will be built from Gold.
- **Ask:** which Gold field or rule replaces it? (Definition still to get from Damien.)

### CA-A11 Customer sub-category
- **Issue:** Gold has the sub-category ("Sub-Axe") per product, not per customer. Damien wants it per customer in the LiveRamp file.
- **Why now:** it needs a rule (period, top or all, list or single value). Someone has to build it.
- **Ask:** who builds per-customer attributes like this: Gold or the LiveRamp export? Damien is clarifying the rule.

### CA-A12 Preferred language
- **Issue:** Canada's language field has 18 raw values (EN, en_CA, en-CA...) and 29% unknown.
- **Why now:** FR / EN targeting is a legal and business need in Canada.
- **Ask:** will Gold standardise it to EN / FR / unknown, and who owns the cleanup?

### CA-A13 Canada brands and divisions
- **Issue:** Canada has brands that may not exist in the US lists (BIOCA, GAB). Some tables use division ACD for LDB.
- **Why now:** missing reference values mean Canada rows are dropped or mis-grouped.
- **Ask:** confirm the Gold brand and division lists cover Canada.

### CA-A14 Canada-specific fields
- **Issue:** no agreed place for Canada-only fields yet.
- **Why now:** it decides how much Canada adapts after migration.
- **Ask:** same views with Canada columns, or a Canada extension?

### CA-A15 to CA-A19 Requested by Sandra (SFMC / Attentive, 2026-10-15)
- **CA-A15 Canadian sales taxes:** SFMC holds GST, HST, PST and RST per line; Gold has one generic tax amount. Legal / finance need, Canada-only.
- **CA-A16 Postal code:** the field exists, but must accept the Canadian format (A1A 1A1), not US ZIP digits.
- **CA-A17 Spend bucket:** `LUSA_12m_spend_bucket` is US-only (USD, US divisions). Canada needs its own in CAD.
- **CA-A18 Full date of birth:** Gold identity only has month + day; the full date sits in US third-party data, likely empty for Canada.
- **CA-A19 WhatsApp:** opt-in, channel, engaged, clicked. Not in the Gold model at all. Check it's live or planned in Canada.
- Sandra's full list (~110 fields) still needs triage with her (must / nice, use case, current source) before it goes to Deepti.

---

## Tab "D2C KPI Catalog - LU 5-8" (KPIs)

### CA-K01 Shared derived KPIs
- **Issue:** retention rate, AOV, engagement rate, new repeat rate and DDX revenue are each used in 2+ Canada reports. Today each report computes them.
- **Why now:** if Gold doesn't fix one formula, numbers will drift between reports and between countries.
- **Ask:** pre-computed in Gold, or a standard formula on Gold building blocks? **Proposed position:** building blocks plus one documented formula each.

### CA-K02 Contactable rule
- **Issue / why:** see CA-A04. This is the KPI definition side.
- **Ask:** can "email contactable or SMS double opt-in" be the Americas rule?

### CA-K03 Engagement definition
- **Issue:** three definitions exist: scorecard (contactable + click or open in 12 months), BAR (active engaged 12M), LiveRamp (engaged prospects 12M).
- **Why now:** one KPI name, three numbers.
- **What we know:** Canada scorecard: 4.13M engaged. That's 84% of contactables, which looks high and is being checked with Genie.
- **Ask:** pick the standard. **Proposed position:** scorecard rule, once the 84% is verified.

### CA-K04 New buyer definition
- **Issue:** three definitions exist: scorecard 12-month key, BAR buyer type, Gold new buyer status.
- **What we know:** Canada: 283K new buyers L12M, 163K YTD.
- **Ask:** pick the standard; compare on paper first.

### CA-K05 to CA-K09 Five KPIs missing from the US catalog
- **Issue:** used in Canada but absent from the US catalog: In/Out flow, media addressable, retained vs reactivated buyers (all in the scorecard), campaign attribution 3/5/7 days (campaign report), new repeat rate (buyer analysis).
- **Why now:** your rule: anything Canada uses must be on the list to discuss. If not added, these reports can't migrate.
- **Ask:** add them to the Canada catalog. Note: In/Out flow also needs CA-A05.

### CA-K10 CLV
- **Issue:** computed quarterly in a Canada table (16 quarters of history), with a 3-year model.
- **Ask:** pre-computed in Gold, or stays in reporting on Gold inputs?

### CA-K11 Brand exclusions
- **Issue:** exclusions vary by use case. Default is SHUUS and BIOUS only. Others (DER, BO, Aesop) appear in some KPIs only.
- **Why now:** if not written per KPI, numbers won't match after migration.
- **Ask:** add an exclusion column (or rule) per KPI in the catalog.

### CA-K12 3-month period
- **Issue:** Canada uses a 3-month period besides MTD / YTD / R12 (raised at workshop 1).
- **Ask:** can the catalog support it?

---

## Tab "DDX Renovate Backlog" (planning)

### CA-P01 Delivery timeline
- Promised by email at workshop 1, not received. We need it to plan Canada's migration.

### CA-P02 Sequencing
- Mezyan pushed attributes first; the stated direction is both in parallel. Needs confirming with Andres.

### CA-P03 Canada D2C KPI catalog
- Deepti committed to create it at workshop 1. It's the base for the Match / Gap / New review.

### CA-P04 History backfill
- 58 monthly snapshots and 16 CLV quarters. Without backfill, YoY and trends break on day one.

### CA-P05 Migration path
- **What we know:** 6 Canada reports are mapped to their legacy tables: DDX Scorecard, Engagement KPIs, CLV Deepdive, Campaign Performance, LiveRamp Customer 360, Quarterly Figures. Buyer Analysis and BAR are still to map.
- **Proposed order:** Scorecard first (largest dependency), then Engagement, Campaign, CLV, LiveRamp. Ask for a dual-run period and compatibility views.

### CA-P06 Refresh cadence
- Today: orders and email events daily; snapshot, scorecard and customer 360 monthly; CLV quarterly. The LiveRamp file is weekly (its source is monthly; Damien is clarifying).

### CA-P07 Master sheet
- The data teams were pointed to "All Domains - SuperGold", but the READ ME names "All Domains" as the source of truth.

### CA-P08 Diamond schema
- The US backlog shows a "Diamond" schema in progress. If it replaces SuperGold, Canada's mapping must target it.

---

## Not for Deepti (internal, pending)
- Sandra: SFMC / Attentive data elements (asked again 2026-10-14).
- Thomas and Olivier: Genie data elements (asked again 2026-10-14).
- Damien: clarifications on sub-categories and 12-36 churn (in PM, 2026-10-14).
- Genie follow-ups (ID values, churn logic, engagement 84%, Buyer Analysis inventory): Bastien.
