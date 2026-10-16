# Canada questions: review after workshop 2 (2026-10-15)

Every Canada question (the CA rows added to the workbook) re-checked against **all workbook tabs** (SuperGold, Gold, KPI catalog, BAR, Values Dictionary, Diamond, backlog, hidden tabs) and against what Deepti and Andres said on 2026-10-15.

**Result: of the 39 Canada questions, 17 can be closed from the workbook itself and several more were answered in the call. 10 still need Deepti or Andres (most only partly). The rest is Canada homework.**

Status key:
- **Closed (workbook)**: the answer is in the US file; nothing to ask.
- **Closed (call)**: answered on 2026-10-15.
- **Ask Deepti / Andres**: still needs them.
- **Canada**: our own work, or a requirement we write and send.

## 1. Still waiting on Deepti or Andres (10)

| Ref | Question | What we now know | What is left |
|---|---|---|---|
| CA-A01 / CA-P04 | Snapshots and history | Deepti: every Gold table has a snapshot date key (showed the campaign interaction metric table and the contacts table). Workbook: snapshots are dropped from SuperGold ("time travel not needed in super gold", Diamond BRD row 559). So history lives in Gold, not in the CDP views | Deepti confirms in writing; monthly or daily; how far back; will Canada's 58 months and 16 CLV quarters be backfilled |
| CA-A02 (part) | Canada brand MDM ID origin | Andres: Gold keys on brand customer ID (MD5 of brand MDM ID + brand code + source + other variables); brand MDM ID can be exposed on request. Gold field list already includes brand MDM ID and global MDM ID | Deepti: where Canada's brand MDM ID comes from, since Canada does not use Reltio |
| CA-A03 (part) | PII access rules | PII is in Gold: `cdp__contact_info_v` holds email, phone and address (contact_type / value), names are in identity (Taxonomy Guide; Deepti) | Andres: who sees PII (marketers yes, analysts no); Unity Catalog groups |
| CA-K03 | Engagement definition | US catalog "Active Engagers": click (email/SMS), review, purchase or site visit in 12 months. **No opens.** BAR adds sign-ups. Canada scorecard counts clicks **or opens** | Agree one rule. This is a real difference, not a missing field |
| CA-K06 | Media addressable | "Paid Media Contactable Records" exists in the catalog (Data Health scorecard) but has no definition | Deepti: definition, to compare with Canada's |
| CA-K08 | Campaign attribution 3/5/7 days | Catalog only has "CRM Campaign Attributed Revenue (GA)". Gold campaign interactions carry attributed order, date and revenue, attribution rule not stated | Deepti: attribution rule and window; can Canada keep 3/5/7 days |
| CA-K10 | CLV | Catalog defines it: CLV = value Y1 + Y2 + Y3, value = AOV x frequency x retention rate. Deepti thinks it is not computed and is checking | Deepti's answer; then compare with Canada's quarterly CLV model |
| CA-K11 | Brand exclusions per KPI | No exclusion column anywhere in the catalog | Add the rule per KPI (default SHUUS, BIOUS) in the catalog or metric views |
| CA-P01 | Delivery dates | Hidden US timeline: "LATAM and Canada integration with US Global workspace: not started, TBD" | Dates for Canada |
| CA-P06 | Refresh cadence | Nothing in the workbook. Canada today: orders and email events daily, snapshot monthly, CLV quarterly | Low priority; confirm Gold matches |

## 2. Closed from the workbook (17)

| Ref | Question | Answer and where |
|---|---|---|
| CA-A04 / CA-K02 | Contactable | Catalog "% contactability" = opt-in on at least one direct channel (email, SMS). Gold `contactability_key` combines all channels (CONEML, CONSMS...). Same as Canada's rule |
| CA-A06 | New consumer keys | Catalog has "Unique New Names" (R12, YTD). Gold has `acquisition_date_key`, so 1M / 12M / YTD are derivable. Note: Diamond removes `new_consumer_status_key` |
| CA-A07 | Churn 12-24, 24+, 12-36 | Gold `lapsed_buyer_status_key`: 12, 24, 36 and 36+ month buckets. BAR buyer status: inactive 13-24, 24-36, 36+. All three LiveRamp flags derivable |
| CA-A08 | Exact AOV | Catalog AOV = net sales / orders (plus Members, New Buyers, Active Buyers AOV). Per customer: `last_12mnths_net_sales` / `last_12mnth_unique_orders`. The buckets were only the BAR view |
| CA-A10 | Engaged prospects | Catalog "Active Engaged Prospects": engaged in 12 months, no purchase. Also RFMEI prospect segments with engaged Y/N. Only check: Damien's definition matches |
| CA-A11 | Customer sub-category | Product sub-category (`level7_desc`) joins to order lines; catalog already uses sub-category KPIs. Derivable. Rule (period, top one or all) is for Damien, not Deepti |
| CA-A14 | Where Canada fields go | Andres: Canada lists what is missing, IT evaluates and evolves the model. Process: a row for discussion, then a backlog story |
| CA-A16 | Postal code | `postal_code` exists next to `zip4` / `zip5`. Canadian format becomes a data-quality rule (Canada) |
| CA-K01 | Pre-computed or formula | Andres: KPIs become Databricks metric views in an IT-governed reporting layer on Renovate. Formulas live in code, one per KPI |
| CA-K04 | New buyer | Catalog: first purchase in the last 12 months, whatever the acquisition date. Gold `new_buyer_status_key` in 3-month buckets. Matches Canada's key in principle; a count check with Genie is enough |
| CA-K05 | In/Out flow (part) | Out: catalog "Unsubscribes" (people who withdrew opt-in, R12 / YTD). In: needs first opt-in date (see call) |
| CA-K07 | Retained vs reactivated | Catalog has Retained Buyers, Reactivated Buyers and Retained + Reactivated. Note: catalog reactivated = no purchase 13-24 months and one before; Gold key says 24-36 months. Check which one Canada uses |
| CA-K09 | New repeat rate | Catalog "New Buyers Repeat Rate": new buyers with 2+ purchases / new buyers |
| CA-K12 | 3-month period | Catalog periods: R12, YTD, MTD, till date, selected period. Gold has 0-3 month buckets, and snapshots allow any window |
| CA-P05 | Migration path | Andres: `crm_reporting` disappears, `crm_analytics` stays, Canada refactors every query onto the new tables |
| CA-P07 | Master sheet | READ ME: All Domains, BAR Activation KPIs and KPI Catalog are the sources of truth. Deepti: attributes in SuperGold, calculated values in the KPI catalog, add missing items as rows. Agreed additions become backlog stories |
| CA-P08 | Diamond | Diamond = next SuperGold: same views, 30 fields removed, 15 renamed, 2 moved; a backlog story covers its deployment. Canada should map to Diamond names |

## 3. Closed in the call

| Ref | Answer |
|---|---|
| CA-A02 (main) | Gold carries brand customer ID and global MDM ID; brand MDM ID can be exposed if Canada needs it (Andres). Same grain, 1:1 |
| CA-A03 (main) | PII is in Gold, through the CDP tables (Deepti) |
| CA-A05 | First email opt-in date is missing; Deepti OK to add it. Unsubscribe date: `email_perm_status_modified_dt` gives the last change; check it is enough |
| CA-K05 (in-flow) | Unblocked by the first opt-in date |
| Sources | New sources go into Renovate. Reporting-only external data can be joined outside; never PII (Andres) |
| New KPIs later | Through IT stories (dedicated reporting data engineer planned), or as a developer via pull requests (Andres) |
| CA-P02 | Sequencing: Canada lists what is missing, IT evaluates and evolves the model in phases (Andres). No more "attributes or KPIs first" debate |
| CA-P03 | Canada KPI catalog: in practice, Canada's rows added to this workbook ("add it here and we can talk about it", Deepti) |
| Workbook use | SuperGold = attributes, KPI catalog = calculated values, BAR = the US BAR report's buckets; all built in Gold (Deepti) |

## 4. Canada homework

| Ref | What | Owner |
|---|---|---|
| CA-A09 | LiveRamp segment type: Gold stores models as `model_name` / `segment_value` (US models: RFMEI, CLTV, Crossfish, churn, prospect prioritisation...). Ask becomes: will Canada's own models (churn 12M, RFMT, likely to convert 3M, product affinity) load into that view? Add to the use-case list for Andres | Bastien |
| CA-A12 | Language: `preferred_language` exists; the US backlog has an en/es cleanup rule. Write the Canada rule (EN / FR / unknown) as a standardisation requirement | Bastien |
| CA-A13 | Canada brands (BIOCA, GAB) and ACD = LDB: a data check once Canada is loaded; write it as a requirement | Bastien |
| CA-A15, A17, A18, A19 | Sandra's items: Canadian taxes (Gold has one `tax_amt`), CAD spend bucket (US one is LUSA), full birth date (US notes year of birth can no longer be stored; check Canada's rule), WhatsApp (not in the model). Triage with Sandra first | Bastien, Sandra |
| New | Transformation and standardisation rules from the Scorecard, CLV and Campaign notebooks, sent to IT for bronze to silver (Andres) | Bastien |
| New | Analytical use cases beyond reporting (CLV, segmentation models, activation feeds) for Andres | Bastien |

## 5. Points to correct or watch
- **"Reverse hashing"**: MD5 cannot be reversed. To get the brand MDM ID back, Gold must expose it (Andres offered) or keep the bridge. Decide whether Canada needs it: check which exports and reports join on it today (LiveRamp at least; the US uses it in Attentive).
- **Snapshots**: Deepti says every table has them; the workbook drops them from SuperGold. Both can be true (Gold yes, CDP views no). Get it in writing.
- **Bastien's figures** in the call: 50 reporting KPIs, about 10 missing, about 15 with questions. After this review, most "missing" KPIs exist in the catalog (repeat rate, retained / reactivated, unsubscribes, engaged prospects, AOV, CLV definition). Real gaps left: first opt-in date, campaign attribution windows, media addressable definition, engagement with opens, brand exclusions.
