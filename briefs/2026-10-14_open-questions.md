# Renovate – open questions (updated 2026-10-14)

"Gold" = the Renovate "super gold" layer: the `cdp__*` views in the US workbook sheet "All Domains - SuperGold" (479 fields). The US design is the baseline. Canada adds its own endpoints.

Update 2026-10-14: Genie answered the section E questions and produced a data context reference (`renovate-ingest-006/raw/2026-10-14_genie-answers_data-context-reference.md`). Genie's answers are data facts from Databricks. Where Genie interprets (e.g. "same IDs"), it is marked as to confirm.

Status legend: **Ready** = enough facts for Canada to take a position. **Partial** = some facts, more needed. **Open** = nothing new. **Answered** = closed.

## A. Decisions on definitions and Gold content (Canada position, then decide with Deepti)

| # | Question | Status to date | Still needed to decide | Who | Proposed Canada position |
|---|---|---|---|---|---|
| 1 | Does Gold keep monthly snapshots, or only the current state? | **Ready.** Canada exec reporting runs on a monthly customer × brand snapshot: 58 months (Jan 2022 to Oct 2026). CLV has 16 quarterly snapshots (Dec 2022 to Sep 2026). Gold is current-state only | Deepti's US plan for history; whether history is backfilled (#34) | Deepti, Andres | Gold holds a monthly customer × brand snapshot with the Canada status keys, history backfilled |
| 2 | Are derived KPIs pre-computed in Gold, or formulas on top? | **Ready.** 5 derived KPIs are used in 2+ reports: retention rate, AOV, engagement rate, new repeat rate, DDX revenue. 5 are used in one report: CLV, In/Out flow, media addressable, campaign attribution, churn rate. Formulas known (Genie section 3) | Deepti's US approach; Thomas & Olivier validate the formulas | Deepti; Thomas & Olivier | Gold provides the building blocks + one documented formula for the 5 shared KPIs (incl. brand exclusions). Single-report KPIs stay in reporting |
| 3 | Canada IDs vs Gold IDs | **Partial.** Bridge table: brand customer ID and brand MDM ID are 1:1 (10.5M each); global MDM ID groups them (10.5M → 8.0M). Genie concludes "same IDs, different names", but Canada tables already hold both as separate columns, so 1:1 does not prove the values are the same. Reporting IDs are md5-hashed; PII-side IDs are not | Andres: is Gold's brand customer ID = Canada's brand customer ID or brand MDM ID? Is Gold's global customer ID = global MDM ID? Hashed or cleartext in Gold? | Andres | Wait for Andres. Genie to compare values, not counts (F1) |
| 4 | One "contactable" definition | **Partial.** Canada rule confirmed: email contactability = Y or SMS double opt-in. 4.95M of 8.03M (61.6%); 4.62M email, 0.79M SMS. Gold has only email permission status. Cannot be counted under the Gold rule until Gold exists for Canada | How US email permission status compares to the Canada contactability key | Deepti; Sandra | Keep the Canada rule; Gold carries the email contactability key and SMS double opt-in |
| 5 | One "engagement" definition | **Partial.** Scorecard rule confirmed: contactable + click or open in last 12 months = 4.13M. BAR and LiveRamp counts not given. 4.13M of 4.95M contactable (84%) looks high for a click/open rate: to verify | BAR and LiveRamp counts; check the 84% (F4, F5) | Genie, then Bastien/Mezyan | Scorecard rule as Gold standard, if the 84% checks out |
| 6 | One "new buyer" definition | **Partial.** Canada 12-month new buyer key: 283K (L12M), 163K YTD. No comparison with BAR or Gold yet (Gold not built for Canada) | Compare the US Gold new buyer definition with the Canada key, on paper | Deepti; Bastien | Paper comparison first |
| 7 | Churn / lapsed windows | **Ready.** Canada churn key: active L12M 514K, lapsed 12-24M 383K, lapsed 24M+ 1.09M. LiveRamp's 12-24 and 24+ flags are derived from it. Damien's 12-36 flag cannot be built from it. **The US Gold lapsed buyer key has 12-24, 24-36 and 36+ month buckets**, so all 3 LiveRamp flags can be derived from it | Damien confirms; clarify Genie's contradiction (F2) | Deepti; Damien | Adopt the US lapsed buyer key; derive LiveRamp flags in the LiveRamp export |
| 8 | Where Canada-specific attributes live | **Partial.** Language messy (18 values: EN, en_CA, en-CA..., 29% unknown); Canada-only brands BIOCA, GAB; division ACD = LDB; currency CAD; brand exclusions vary by KPI (#32) | Deepti's pattern for local fields; who standardises language | Deepti | Gold carries a standardised language (EN/FR/unknown) and the Canada brand list |
| 9 | Refresh cadences | **Answered (sources).** Orders daily, email events daily, segment snapshot monthly, scorecard monthly (Monday job), customer 360 monthly, CLV quarterly | Andres validates Gold matches; LiveRamp weekly file vs monthly source (#33) | Andres | Gold daily for orders/events, monthly snapshot, quarterly CLV |
| 10 | Migration from CRM Base / Reporting to Gold | **Ready (inventory).** 6 reports mapped to their tables: DDX Scorecard, DDX Engagement KPIs, CLV Deepdive, Campaign Performance, LiveRamp Customer 360, DDX Quarterly Figures. Missing: "Buyer Analysis" and BAR dashboard (F3) | Complete inventory; Canada's migration order | Deepti, Andres | Scorecard first (largest dependency), then Engagement, Campaign, CLV, LiveRamp |
| 24 | LiveRamp columns (churn flags, engaged prospects, segment type) | **Partial.** Churn flags derivable (#7). Segment type: 5 values used (churn prediction 12M, RFMT, likely to convert 3M, product affinity buyer / prospect); Gold uses model name / segment value. Engaged prospects definition not given | Segment type → Gold mapping; engaged prospects definition (F5) | Deepti; Damien | Map segment type to Gold model name; derive flags in export |
| 25 | KPIs missing from the US catalog | **Answered.** Used in Canada: In/Out flow, media addressable, retained vs reactivated (Scorecard); campaign attribution 3/5/7 days (Campaign Performance); new repeat rate (Buyer Analysis, BAR). Send Time Optimization: not found | — | Bastien | Per your rule: the 5 go on the list of KPIs needing discussion. STO: drop unless someone claims it (F8) |

## B. Governance and planning

| # | Question | Status to date | Next step | Who |
|---|---|---|---|---|
| 11 | Final word for Canada beyond Mezyan and Bastien? | **Answered:** Ale (Mezyan's boss) can have it | — | — |
| 12 | Who decides the Gold design questions? | **Answered:** Canada decides with Deepti; escalate to Ale if not happy | — | — |
| 13 | Engineering sequencing: attributes or KPIs first? | Open. Direction: both in parallel | Wait | Deepti, Andres |
| 14 | Delivery timeline for attributes and KPIs | Promised by email, no date | Chase | Deepti |
| 15 | Canada D2C KPI catalog: when shared? | Promised, no date | Chase | Deepti |
| 16 | Workshop 2 date | Expected week of 2026-10-12; no date recorded | Chase, or tell me if held | Ajantha |
| 17 | Brand-specific local definitions Canada needs | Partial (see #32) | Bastien / Mezyan answer | Bastien, Mezyan |
| 18 | Brands excluded by Canada | **Answered (refined 2026-10-14):** depends on the use case. SHUUS and BIOUS are generally always excluded; no other exclusion unless specified | — | — |
| 19 | Stakeholder surnames and teams | Parked | Only if a formal email is needed | Bastien |
| 28 | Master workbook sheet for additions | Open | Ask | Deepti |
| 29 | Is "Diamond" the US target schema replacing SuperGold? | Open | Ask | Deepti (or Shabri, #31) |
| 31 | Shabri vs Deepti | **Answered (2026-10-14):** Shabri owns the L'Oréal USA SuperGold; Deepti is the Americas owner and takes the final decisions | — | — |

## C. Data teams

| # | Question | Status to date | Next step | Who |
|---|---|---|---|---|
| 20 | SFMC/Attentive list + follow-ups | Pending | Chase | Sandra |
| 21 | Genie team list + follow-ups | Pending. Genie writes "Olivier" for Oli | Chase | Thomas & Olivier |
| 22 | LiveRamp value formats | Open | Ask | Damien |
| 23 | LiveRamp file sourced from Gold? | **Answered:** yes, later | — | — |
| 30 | **New.** Damien's customer-level sub-categories (anti-aging, suncare...): Gold has product hierarchy only, no customer affinity | Open, rated high by Genie | Derive from orders × product hierarchy, or add a field? | Deepti; Damien |

## D. New questions raised by Genie's answers

| # | Question | Why it matters | Who |
|---|---|---|---|
| 32 | Brand exclusions per KPI: SHUUS, BIOUS always; DER, BO only in some contexts (LiveRamp, media addressable, new repeat rate); Aesop (AEO) excluded from retention and new repeat rate. You said all four are excluded by Canada | Rules must be written once (Gold or KPI catalog), otherwise numbers drift | **Answered (2026-10-14):** per use case; SHUUS and BIOUS by default, others only when specified. F6 still useful to document each KPI |
| 33 | LiveRamp file is weekly, but its source view refreshes monthly | Either the weekly file repeats data, or another source feeds it | Damien (F7) |
| 34 | Will Gold backfill the 58 months of snapshot history and 16 CLV quarters? | Without it, trend and YoY KPIs break at migration | Deepti, Andres |
| 35 | **Critical.** PII: LiveRamp, SFMC, Attentive need cleartext email/phone/address. PII in Gold, or a separate export layer? | All activation feeds depend on it | Deepti, Andres |
| 36 | Exact AOV: Gold has AOV buckets only; CLV needs exact values | CLV Deepdive breaks | Deepti |
| 37 | Do Canada-only brands (BIOCA, GAB) and the ACD = LDB division mapping exist in Gold's brand and division lists? | Canada rows lost or misgrouped | Deepti |

## E. Data checks

| # | Question | Status to date |
|---|---|---|
| 26 | Fill rates for Canada | Partial: language 29% unknown. Field is `pref_language` in Canada, `preferred_language` in Gold. Other fields untested |
| 27 | Which KPI catalog sheet did Genie use? | Not answered (F9) |

## F. Follow-up questions for Genie (copy-paste)

1. In dim_customer_bridge, compare values (not counts): for the same customer, is brand_customer_id equal to brand_mdm_id? Give the share of rows where they are equal. (#3)
2. Your gap list says churn_status_key does not map 1:1 to churn_12_24_flag / churn_24plus_flag, but you also say the flags are derived from that key in vw_customer360_liveramp. Show the view's flag logic and explain. (#7)
3. List all Canada reports and dashboards, including "Buyer Analysis" and the BAR dashboard, with the tables each reads. (#10)
4. Engaged = 4.13M of 4.95M contactable (84%). Does last_engagement_date_key count only clicks and opens, or sends too? Show the share per brand. (#5)
5. Count engaged customers under the BAR definition (active_engaged_last_12_months) and the LiveRamp definition (engaged_prospects_l12m), and give the definition of engaged_prospects_l12m. (#5, #24)
6. List each KPI with the brand exclusions (SHUUS, BIOUS, DER, BO, AEO) applied in the Canada report code. (#32)
7. What feeds the weekly LiveRamp file if vw_customer360_liveramp refreshes monthly? (#33)
8. Is any Send Time Optimization metric used in a Canada report? (#25)
9. Which KPI catalog sheet did you use: "D2C KPI Catalog - LU 5-8" (958 rows) or the hidden "KPI Catalog" (~198 rows)? (#27)
