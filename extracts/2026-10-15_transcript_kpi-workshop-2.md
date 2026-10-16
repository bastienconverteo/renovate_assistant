# Extract: workshop 2, KPI / Renovate Gold review (2026-10-15)

Raw: `raw/2026-10-15_transcript_kpi-workshop-2.md` (OCR from recording, gaps marked). Participants: Bastien Duthu (Converteo), Deepti Keelara, Ajantha Mohanty (Wipro), Andres Gonzalez (joined ~29:50). Mezyan absent. Evidence label: verbal.

## Answers
- **IDs (Deepti, Andres):** Gold carries brand customer ID and global MDM ID, not brand MDM ID today. Brand customer ID is the key of the whole model, hashed (also hashed today). Andres: brand customer ID = MD5 of brand MDM ID + brand code + source name + other variables; 1:1 with brand MDM ID; brand MDM ID "can be offered" if needed (the CDP uses it for some integrations). Deepti: in the US brand MDM ID comes from Reltio and was dropped; Canada does not use Reltio, so she will check where Canada's comes from.
- **PII (Deepti):** in Gold, through the CDP tables ("everything a CDP should have, it has"). Could not find it in the workbook live; will confirm. Access: activation users yes, analysts no; governance question for Andres (Unity Catalog groups).
- **First email opt-in date (Deepti):** missing; OK to add if Canada needs it.
- **Snapshots (Deepti):** every table has a snapshot date key (showed campaign interaction metric table, snapshot key 8 = August; contacts table with address and PII). Not written in the workbook; she will answer in writing. Bastien: any time window can then be computed from snapshots.
- **Workbook use (Deepti):** SuperGold = attributes; KPI catalog = calculated values; BAR = KPIs of the US BAR Power BI report (pseudo-CDP for audience sizing). Both KPI catalog and BAR were built in Gold. Check both before calling something missing; add missing items as rows.
- **AOV (Deepti):** in the KPI catalog (Member AOV: average value per order placed by members during the period).
- **CLV (Deepti):** defined in the KPI catalog (Y1 + Y2 + Y3; AOV x frequency x retention). Probably not computed for the US; she will check it exists in the tables.
- **Migration (Andres):** `crm_reporting` disappears. `crm_analytics` remains for analytical use cases, on the new Gold. Canada must refactor all queries and logic onto the new data model.
- **Data cleaning (Andres):** standardisation and transformation rules Canada applies today must become requirements; IT applies them from bronze to silver so Gold is clean.
- **New sources (Andres):** should go into Renovate. Reporting-only external data (e.g. campaign platform data) can be joined across schemas; PII must not leave Renovate.
- **Reporting layer (Andres):** on top of Renovate, governed by IT, using Databricks metric views; KPI logic in code, not user notebooks, to keep one standard across the Americas. Canada can develop KPIs as a developer in the pipeline (pull requests) or ask IT through stories; IT plans dedicated capacity and a reporting data engineer. Integration through the "consumer port".

## Figures given by Bastien
50 reporting KPIs (plus variants); about 10 missing; about 15 with questions. SFMC: about 100 fields requested by the business, still being prioritised. Ajantha's read: "50-50".

## Actions
- Deepti: Canada brand MDM ID origin; PII location in writing; snapshots in writing; CLV computed or not.
- Andres: PII access governance.
- Bastien: recap and pending questions to Deepti and Ajantha; re-check questions against the KPI catalog and BAR; list Canada transformation rules; list analytical use cases; decide whether Canada needs brand MDM ID.
- Ajantha: send the follow-up; schedule next meeting next week, same time (agenda shared before; skip if nothing).

## Correction to note
Bastien asked whether Canada could "reverse-hash" the brand customer ID. MD5 is one-way; the brand MDM ID must be exposed by Gold or kept in a bridge.
