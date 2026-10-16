# Context (stable facts only; details live in registers, cite IDs)

## Project
- Renovate: L'Oréal programme building a common "super gold" layer in Databricks for the Americas (USA, Canada, LATAM). Gold becomes the primary consumption layer (Genie, SFMC, CDP); CRM Base and CRM Reporting go away (DEC-0015).
- The US built the baseline: workbook SRC-0002 (SuperGold = DP-0001..0479 in 21 cdp__ views; US KPI catalog 958 rows). US-specific: Canada reuses most of it and adds endpoints. US people are not tracked.
- Governance: Gold is global and uniform; local adjustments only for specific business needs, e.g. brand-specific "active customer" (DEC-0014).
- Timeline: Canada onboarding 2027, LATAM later, "planning tbc" (inferred, SRC-0001). No firm delivery deadline (COM-0002). Deck budgets are irrelevant.

## People
- Bastien: Canada-side project manager (Converteo, git bastien.duthu@converteo.com). Manager: Mezyan (STK-0009), PM responsible for the Canada data teams.
- Canada business owners of KPI definitions and Canada completion: Mezyan and Bastien (DEC-0019; another final approver may be named, QST-0011). Canada weighs in on every Gold design decision to minimise post-migration adaptation (DEC-0020). There is no Fatima: recap v1 misnamed Mezyan (STK-0007 superseded).
- Programme: Ajantha, Renovate PM across regions (STK-0008). Deepti, IT lead reporting and analytics for all zones, Americas Gold owner, takes the final Gold decisions; Canada decides with her, escalation to Ale, Mezyan's boss (DEC-0023, STK-0010). Shabri owns the LUSA SuperGold only (STK-0011). Andres, IT implementation and data engineering (STK-0006).
- Data teams: Sandra SFMC and Attentive, Damien LiveRamp, Thomas and Oli (Olivier) Genie (STK-0001..0004).

## Current work (October 2026)
- Map the Gold data elements Canada needs: data-team asks ACT-0001..0003 (asap, no due date); Bastien's gap analysis between the files ACT-0020.
- Check every Canada reporting KPI exists in Gold: SRC-0003 checked 32 KPIs (CAKPI-*); the main gap is monthly snapshots versus current-state Gold (DEC-0001).
- KPI catalog workshops: MTG-0001 held (US catalog = baseline, Match / Gap / New); next one to schedule (ACT-0016).

## Source notes
- Workbook READ ME: sources of truth are All Domains, BAR Activation KPIs and KPI Catalog; data teams were pointed to "All Domains - SuperGold".
- Genie's analysis is design-level; fill rates and value sets are untested (prompts SRC-0010 not run yet).
- Canada data landscape (tables, snapshots, IDs, KPI formulas, report inventory, refresh): Genie reference SRC-0013. Its raw file holds the ID hashing rule with its salt: never quote it outside the repo.
- The LiveRamp weekly file will be built from Gold (QST-0009). Brand exclusions are per use case (DEC-0022).
- The LiveRamp file sample stays in `inbox/` (personal data); only its column names are in `raw/` (SRC-0007).
- US backlog lessons to watch for Canada: SFMC / Attentive geotracking and OS data not sent (BL-055, BL-056); primary email, phone, address rules (BL-065..067); 1900-01-01 birth dates (BL-081); Attentive cleansing rollback (BL-068, BL-075); US moving to a "Diamond" target schema (BL-085).

## Bastien's preferences
- Quick answers ("impact of this decision", "generate a status") without reading documents; condensed replies, minimal tokens.
- Capture small details; they may link to a later transcript or email.
- Business requests outweigh Genie / LLM suggestions; suggestions are still recorded and put to the business.
- Inputs: files in `inbox/`, or pasted emails and ServiceNow threads (no connector). Calls via Biscotti. Data facts via Databricks Genie.
- Personal proof of concept approved by IT, no compliance gate; personal data rows are still never committed.
- Folder on his Mac `~/Documents/Projects/renovate`, remote `renovate_assistant` on GitHub; Bastien pushes.
