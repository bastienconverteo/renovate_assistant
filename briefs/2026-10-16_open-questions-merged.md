# Renovate (Canada): open questions, current state (2026-10-16)

Merged from: open questions table (2026-10-14, #1-#37, Genie follow-ups F1-F9), question review after workshop 2 (2026-10-15, CA refs = Canada rows added to the workbook) and the workshop 2 extract. Originals in the Mac repo `briefs/` and `extracts/`.

"Gold" = Renovate "super gold" layer. US design is the baseline; Canada adds its own endpoints. Workbook logic: SuperGold = attributes (CDP views), KPI catalog ("D2C KPI Catalog - LU 5-8") = calculated values, BAR = buckets of the US BAR Power BI report, Diamond = next SuperGold. Always check SuperGold, Gold, KPI catalog, BAR and Values Dictionary before calling anything missing.

**Count after workshop 2:** 39 Canada questions: 17 closed from the workbook, several closed in the call, 10 still need Deepti or Andres (most only partly), the rest is Canada homework. Real gaps left: first opt-in date, campaign attribution windows, media addressable definition, engagement with opens, brand exclusions per KPI.

## 1. Waiting on Deepti or Andres

| Topic (refs) | What we know | What is left | Who |
|---|---|---|---|
| Snapshots and history (#1, #34, CA-A01, CA-P04) | Canada exec reporting runs on a monthly customer × brand snapshot: 58 months (Jan 2022 to Oct 2026); CLV 16 quarterly snapshots (Dec 2022 to Sep 2026). Deepti (call): every Gold table has a snapshot date key (showed campaign interaction metric table, snapshot key 8 = August; contacts table). Workbook drops snapshots from SuperGold ("time travel not needed in super gold", Diamond BRD row 559): both true (Gold yes, CDP views no). Any window then computable from snapshots | Deepti in writing: monthly or daily, how far back, backfill of 58 months and 16 CLV quarters (without it trend and YoY KPIs break at migration). Canada position: monthly customer × brand snapshot with Canada status keys, history backfilled | Deepti, Andres |
| Canada brand MDM ID origin (#3, CA-A02 part) | Gold keys on brand customer ID = MD5 of brand MDM ID + brand code + source name + other variables; 1:1 with brand MDM ID; global MDM ID groups them (bridge: 10.5M → 8.0M). Brand MDM ID can be exposed on request (CDP uses it for some integrations). In the US it comes from Reltio and was dropped; Canada does not use Reltio. Reporting IDs md5-hashed, PII-side IDs not | Deepti: where Canada's brand MDM ID comes from. Canada: decide whether it needs brand MDM ID (check which exports/reports join on it: LiveRamp at least; US uses it in Attentive). MD5 is one-way, so no "reverse hashing": Gold exposes it or a bridge is kept | Deepti; Bastien |
| PII access (#35, CA-A03 part) | PII is in Gold via CDP tables: `cdp__contact_info_v` (email, phone, address as contact_type / value), names in identity. LiveRamp, SFMC, Attentive need cleartext. Deepti could not show it live; will confirm in writing | Andres: who sees PII (activation/marketers yes, analysts no), Unity Catalog groups | Andres; Deepti |
| Engagement definition (#5, CA-K03) | US catalog "Active Engagers": click (email/SMS), review, purchase or site visit in 12 months, **no opens**. BAR adds sign-ups. Canada scorecard: contactable + click **or open** in 12 months = 4.13M of 4.95M contactable (84%, looks high: verify) | Agree one rule (real difference, not a missing field). Check the 84% and BAR/LiveRamp counts (F4, F5) | Deepti; Bastien, Mezyan |
| Media addressable (CA-K06) | "Paid Media Contactable Records" in catalog (Data Health scorecard), no definition | Deepti: definition, to compare with Canada's | Deepti |
| Campaign attribution 3/5/7 days (CA-K08) | Catalog only has "CRM Campaign Attributed Revenue (GA)". Gold campaign interactions carry attributed order, date, revenue; rule not stated | Deepti: attribution rule and window; can Canada keep 3/5/7 days | Deepti |
| CLV (#36, CA-K10) | Catalog: CLV = value Y1 + Y2 + Y3, value = AOV × frequency × retention rate. Deepti thinks it is not computed for the US; checking | Deepti's answer; then compare with Canada's quarterly CLV model | Deepti |
| Brand exclusions per KPI (#18, #32, CA-K11) | Rule (Bastien 2026-10-14): depends on use case; SHUUS and BIOUS excluded by default, no other unless specified. Genie: DER, BO only in some contexts (LiveRamp, media addressable, new repeat rate); Aesop (AEO) excluded from retention and new repeat rate. No exclusion column anywhere in the catalog | Write the rule per KPI once (catalog or metric views), else numbers drift. F6 documents current code | Deepti; Bastien |
| Delivery dates (#14, CA-P01) | Promised by email, no date. Hidden US timeline: "LATAM and Canada integration with US Global workspace: not started, TBD" | Dates for Canada | Deepti |
| Refresh cadence (#9, CA-P06) | Canada sources: orders and email events daily, segment snapshot monthly, scorecard monthly (Monday job), customer 360 monthly, CLV quarterly. Nothing in the workbook | Low priority: confirm Gold matches. LiveRamp file weekly vs monthly source view (#33, F7) | Andres; Damien |

## 2. Closed

| Topic (refs) | Answer and source |
|---|---|
| Contactable (#4, CA-A04, CA-K02) | Catalog "% contactability" = opt-in on at least one direct channel; Gold `contactability_key` combines channels (CONEML, CONSMS...). Same as Canada rule (email contactability = Y or SMS double opt-in: 4.95M of 8.03M, 61.6%; 4.62M email, 0.79M SMS) |
| New consumer / new buyer (#6, CA-A06, CA-K04) | Catalog "Unique New Names" (R12, YTD); Gold `acquisition_date_key` gives 1M / 12M / YTD. Diamond removes `new_consumer_status_key`. New buyer: first purchase in last 12 months; Gold `new_buyer_status_key` in 3-month buckets; Canada key 283K L12M, 163K YTD. Count check with Genie is enough |
| Churn 12-24, 24+, 12-36 (#7, CA-A07) | Gold `lapsed_buyer_status_key`: 12, 24, 36, 36+ buckets; BAR inactive 13-24, 24-36, 36+. All LiveRamp flags (incl. Damien's 12-36) derivable. Canada churn key: active L12M 514K, lapsed 12-24M 383K, 24M+ 1.09M. Position: adopt US key, derive flags in the LiveRamp export. Genie contradiction on flag logic still open (F2) |
| Exact AOV (#36, CA-A08) | Catalog AOV = net sales / orders (+ Members, New Buyers, Active Buyers AOV; Deepti: Member AOV). Per customer: `last_12mnths_net_sales` / `last_12mnth_unique_orders`. Buckets were only the BAR view |
| Engaged prospects (#24 part, CA-A10) | Catalog "Active Engaged Prospects": engaged in 12 months, no purchase; RFMEI prospect segments with engaged Y/N. Check Damien's definition matches |
| Customer sub-category (#30, CA-A11) | Product sub-category (`level7_desc`) joins to order lines; derivable. Rule (period, top one or all) is for Damien |
| Where Canada fields go (#8 part, CA-A14, CA-P07, #28) | Canada lists what is missing, IT evaluates and evolves the model (Andres). Add rows to the workbook, then backlog stories. READ ME: All Domains, BAR Activation KPIs and KPI Catalog are sources of truth |
| Postal code (CA-A16) | `postal_code` exists next to `zip4` / `zip5`; Canadian format (A1A 1A1) becomes a data-quality rule |
| Pre-computed or formula (#2, CA-K01) | KPIs become Databricks metric views in an IT-governed reporting layer on Renovate; one formula per KPI in code. Shared KPIs (2+ reports): retention rate, AOV, engagement rate, new repeat rate, DDX revenue |
| In/Out flow (CA-K05) | Out: catalog "Unsubscribes" (R12 / YTD). In: unblocked by first opt-in date |
| Retained vs reactivated (CA-K07) | Catalog has Retained, Reactivated, Retained + Reactivated. Catalog reactivated = no purchase 13-24 months; Gold key says 24-36: check which Canada uses |
| New repeat rate (CA-K09) | Catalog "New Buyers Repeat Rate": new buyers with 2+ purchases / new buyers |
| 3-month period (CA-K12) | Catalog periods R12, YTD, MTD, till date, selected; Gold 0-3 month buckets; snapshots allow any window |
| Migration (#10, CA-P05) | `crm_reporting` disappears, `crm_analytics` stays on new Gold, Canada refactors every query. Inventory: DDX Scorecard, DDX Engagement KPIs, CLV Deepdive, Campaign Performance, LiveRamp Customer 360, DDX Quarterly Figures (Buyer Analysis, BAR dashboard missing: F3). Proposed order: Scorecard, Engagement, Campaign, CLV, LiveRamp |
| Diamond (#29, CA-P08) | Next SuperGold: same views, 30 fields removed, 15 renamed, 2 moved; backlog story covers deployment. Map Canada to Diamond names |
| IDs in Gold (#3 main) | Brand customer ID + global MDM ID, same grain, 1:1 (Andres) |
| PII location (#35 main) | In Gold through CDP tables (Deepti) |
| First opt-in / unsubscribe date (CA-A05) | First email opt-in date missing; Deepti OK to add. `email_perm_status_modified_dt` gives last change: check it is enough |
| New sources | Go into Renovate; reporting-only external data joinable across schemas; PII never leaves Renovate (Andres) |
| New KPIs later | IT stories (dedicated reporting data engineer planned) or pull requests as developer; integration via "consumer port" (Andres) |
| Sequencing (#13, CA-P02) | No "attributes or KPIs first" debate: phased evolution (Andres) |
| Canada KPI catalog (#15, CA-P03) | In practice Canada's rows in this workbook (Deepti) |
| Missing KPIs (#25) | In/Out flow, media addressable, retained vs reactivated, campaign attribution 3/5/7d, new repeat rate went on the discussion list (rule: missing but used in Canada ops). Most now found in catalog. Send Time Optimization not found: drop unless claimed (F8) |
| Governance (#11, #12, #31) | Ale (Mezyan's boss) can have Canada's final word. Canada decides Gold design with Deepti; escalate to Ale. Shabri owns LUSA SuperGold; Deepti is Americas owner and final decision-maker |
| LiveRamp file from Gold (#23) | Yes, later |
| Workshop 2 date (#16) | Held 2026-10-15 |

## 3. Canada homework (Bastien unless stated)

| Topic (refs) | What |
|---|---|
| LiveRamp segment type (#24, CA-A09) | Gold stores models as `model_name` / `segment_value` (US: RFMEI, CLTV, Crossfish, churn, prospect prioritisation). Canada uses 5 values (churn prediction 12M, RFMT, likely to convert 3M, product affinity buyer / prospect). Ask Andres whether Canada's models load into that view; add to use-case list |
| Language (#8, #26, CA-A12) | 18 raw values (EN, en_CA, en-CA...), 29% unknown; field `pref_language` in Canada, `preferred_language` in Gold; US backlog has en/es cleanup. Write Canada rule EN / FR / unknown |
| Canada brands (#37, CA-A13) | BIOCA, GAB and ACD = LDB division, currency CAD: data check once Canada is loaded; write as requirement |
| Sandra's SFMC items (#20, CA-A15, A17, A18, A19) | Canadian taxes (GST, HST, PST, RST per line; Gold one `tax_amt`), CAD spend bucket (`LUSA_12m_spend_bucket` is US-only), full birth date (Gold identity month + day; US notes year can no longer be stored; check Canada rule), WhatsApp (opt-in, channel, engaged, clicked: not in model). Sandra's full list ~110 fields: triage with her (must / nice, use case, source) before Deepti |
| Transformation rules | From Scorecard, CLV, Campaign notebooks, sent to IT for bronze to silver (Andres) |
| Analytical use cases | Beyond reporting (CLV, segmentation, activation feeds), for Andres |
| Brand-specific local definitions (#17) | Bastien / Mezyan answer (e.g. "active customer") |

## 4. Data teams and parked items

| # | Item | Status |
|---|---|---|
| 21 | Genie team list (Thomas & Olivier) + formula validation | Pending, chase |
| 22 | LiveRamp value formats | Open, ask Damien |
| 19 | Stakeholder surnames | Parked; only if a formal email needs them |
| 26 | Fill rates for Canada beyond language | Untested |
| 27 | Which KPI catalog sheet Genie used | Not answered (F9) |

## 5. Workshop 2 record (2026-10-15)

- Participants: Bastien (Converteo), Deepti Keelara, Ajantha Mohanty (Wipro), Andres Gonzalez (joined ~29:50). Mezyan absent. Evidence: verbal.
- Bastien's figures: 50 reporting KPIs (plus variants), ~10 missing, ~15 with questions; SFMC ~100 fields requested, being prioritised. Ajantha's read: "50-50". After review most "missing" KPIs exist in the catalog.
- Actions: Deepti (brand MDM ID origin, PII and snapshots in writing, CLV computed or not); Andres (PII access governance); Bastien (recap and pending questions to Deepti and Ajantha, re-check vs catalog and BAR, Canada transformation rules, analytical use cases, brand MDM ID need); Ajantha (send follow-up; next meeting ~2026-10-22, same time, agenda before, skip if nothing).

## 6. Genie follow-ups (copy-paste, still open)

1. In dim_customer_bridge, compare values (not counts): for the same customer, is brand_customer_id equal to brand_mdm_id? Give the share of rows where they are equal. (IDs)
2. Your gap list says churn_status_key does not map 1:1 to churn_12_24_flag / churn_24plus_flag, but you also say the flags are derived from that key in vw_customer360_liveramp. Show the view's flag logic and explain. (churn)
3. List all Canada reports and dashboards, including "Buyer Analysis" and the BAR dashboard, with the tables each reads. (migration)
4. Engaged = 4.13M of 4.95M contactable (84%). Does last_engagement_date_key count only clicks and opens, or sends too? Show the share per brand. (engagement)
5. Count engaged customers under the BAR definition (active_engaged_last_12_months) and the LiveRamp definition (engaged_prospects_l12m), and give the definition of engaged_prospects_l12m. (engagement, LiveRamp)
6. List each KPI with the brand exclusions (SHUUS, BIOUS, DER, BO, AEO) applied in the Canada report code. (exclusions)
7. What feeds the weekly LiveRamp file if vw_customer360_liveramp refreshes monthly? (cadence)
8. Is any Send Time Optimization metric used in a Canada report? (missing KPIs)
9. Which KPI catalog sheet did you use: "D2C KPI Catalog - LU 5-8" (958 rows) or the hidden "KPI Catalog" (~198 rows)? (catalog)

Note: a Genie answer on 2026-10-14 (ID value check, raw in repo) may already cover F1; see repo `raw/2026-10-14_genie-answer_id-value-check.md`.
