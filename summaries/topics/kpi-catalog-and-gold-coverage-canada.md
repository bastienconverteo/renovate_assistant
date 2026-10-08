# Topic: Canada KPI catalog and Gold coverage

Last updated: 2026-10-08 (workshop summary versions 1 and 2 reconciled) | Owner: Bastien | Sources: workshop 1 recap, Genie analysis, US workbook

## State in five lines
1. The US built the SuperGold layer and KPI catalog; Canada reuses them as baseline (decided at workshop 1) and adds Canada-specific needs.
2. Gold becomes the only consumption layer for Genie, SFMC and CDP, so every Canada KPI and attribute must exist in Gold (REQ-0001, REQ-0002).
3. Genie compared four Canada reports (32 KPIs) with SuperGold: 14 present, 8 mismatched or partial, 10 gaps. Biggest gap: Canada reports are monthly snapshots, SuperGold is current-state only.
4. Ten design questions are open (DEC-0001 to DEC-0010) plus attributes-versus-KPIs sequencing (DEC-0017); Canada's 3-month period is a new requirement (REQ-0011).
5. Three data teams (Sandra, Damien, Thomas and Oli) are asked for their data elements: all pending, no due date. No firm delivery deadline exists yet; Deepti and Andres are to communicate dates.

## What happened
- 2026-10-08: ingested the Elevate deck (context), the US workbook, Genie's cross-reference analysis and the workshop 1 recap.
- Workshop 1 (date not stated): approach agreed; next workshop to be scheduled by Ajantha for the week of 2026-10-12 (inferred) and to start with a manageable set of priority KPIs.

## People (from workshop 1, version 2)
- Deepti: leads reporting and analytics on the IT side, all zones; defines what Gold should look like. Andres: manages implementation and data engineering on the IT side. Ajantha: Renovate project manager across US, Canada, LATAM. Governance line (Deepti): Gold is global and uniform; local adjustments only for specific business needs (e.g. brand-specific "active customer"); align with US definitions. Attributes vs KPIs first: unresolved, team will work on both.

## What is next
- Bastien: Match / Gap / New review of US KPIs (ACT-0010); prepare a priority KPI set for the next workshop (ACT-0017, suggested); run the Databricks field coverage prompts (ACT-0004).
- Deepti: share the Canada KPI Catalog (ACT-0009); with Andres confirm sequencing and deadlines (ACT-0013, ACT-0014).

## Where to look
registers: kpis, requirements (REQ-0003 to REQ-0012), decisions (DEC-0001 to DEC-0017), actions, commitments. Extracts in `extracts/` dated 2026-10-08.
