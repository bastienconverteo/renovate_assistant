# Renovate status (Canada view)

Last refreshed: 2026-10-08 | Sources: Elevate deck, US workbook, Genie analysis, workshop 1 recap, Bastien's messages | Not available: ServiceNow tickets, call transcripts, replies from Sandra, Thomas and Oli, the LiveRamp schema file, Canadian table coverage (Databricks prompts not yet run)

## What changed
- Workshop 1 held: US KPI catalog is the baseline for Canada; a dedicated Canada KPI Catalog will be created (Deepti); Gold becomes the primary consumption layer.
- Damien (LiveRamp) replied: LiveRamp schema shared and two fields to add (sub-categories, Is_Churn_12M_36M); recorded as REQ-0013 and REQ-0014.
- Genie compared four Canada reports with SuperGold: 14 of 32 KPIs fully present, 8 mismatched or partial, 10 gaps (snapshot dimension, new consumer keys, opt-in/unsub dates, CLV, churn flags, segment_type).

## On track
- Match / Gap / New review of US KPIs by Bastien and the Canada DDX team: in progress.
- Feedback gathering from SFMC, Genie and other Canada stakeholders: in progress.

## Pending (no due date)
- Sandra (SFMC, Attentive), Thomas and Oli (Genie): data element lists requested by email on 2026-10-08, no reply yet.
- Damien (LiveRamp): replied 2026-10-08 with two fields; completeness not confirmed and the schema file not yet received (ACT-0002 in progress, ACT-0019).
- Bastien: put the Genie-suggested attributes to the business teams for relevance (ACT-0018, proposed).
- Deepti (IT lead, reporting and analytics, all zones): share the Canada KPI Catalog ("next step"). Deepti and Andres: communicate delivery deadlines for attributes and KPIs (by email, no date).
- Ajantha (Renovate project manager across regions): schedule the next workshop (next week, inferred week of 2026-10-12).

## Blocked
- Nothing registered as blocked. Lessons from the US backlog to watch for Canada: SFMC / Attentive geotracking and OS data not being sent; primary email, phone and address rules; 1900-01-01 birth dates.

## Threatens the next milestone
- No firm delivery deadline exists, so slippage cannot yet be measured.
- The snapshot question (DEC-0001): if Gold is current-state only, Canada's monthly executive scorecard cannot be reproduced from Gold.

## Decisions needed (open)
- DEC-0001 snapshots; DEC-0002 derived KPIs pre-computed or formula; DEC-0003 ID naming (brand_mdm_id vs brand_customer_id); DEC-0004 to DEC-0007 (DEC-0007 now includes Damien's Is_Churn_12M_36M) one definition each for contactable, engagement, new buyer, churn; DEC-0008 Canada-specific attributes; DEC-0009 refresh cadences; DEC-0010 migration path; DEC-0017 attributes or KPIs first. Decision owners not yet identified.

## Missing information
- Canadian table coverage per field (Databricks Prompts A and B not run); KPI sections beyond the four reports analysed; surnames of all named people; who actually said "attributes first" in workshop 1 (Fatima or Mezyan, Bastien's manager); workshop dates; Canada-specific brand definitions (for example "active customer").

## Regional coverage
| Region | Position |
| --- | --- |
| USA | SuperGold built: 479 field rows in 21 cdp__ views; US KPI catalog (958 rows) |
| Canada | Reuses US baseline; 32 report KPIs checked at design level (14 present); field-level data coverage not assessed |
| LATAM | Not assessed; onboarding later (2027 or beyond, planning tbc, inferred) |
