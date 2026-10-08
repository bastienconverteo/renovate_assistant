# Extract: Canada KPI workshop 1, written summary

- Type: call recap (written summary of the first Canada KPI workshop; not a verbatim transcript)
- Date of input: received 2026-10-08; the call date and the author of the recap are not stated
- Original: raw/2026-10-08_workshop-summary_kpi-workshop-1.md
- Participants named: Bastien, Deepti, Andres, Fatima, Ajantha; teams mentioned: Canada DDX team, Reporting team, SFMC, Genie. Full attendee list not stated.
- Ingested: 2026-10-08
- Evidence: documented (written recap), unless marked inferred.

## Decisions (explicit)
1. The **US KPI catalog is the baseline for Canada**. Canada reviews the US KPI definitions and classifies each as adopt as-is, Canada-specific adjustment, or missing/new Canada KPI ("Match / Gap / New").
2. **Initial focus: consumer funnel, KPI name and KPI definition.** Extra dimensions (MTD, YTD, YoY, monthly) come later.
3. A **dedicated D2C KPI Catalog for Canada** will be created to hold Canada-specific definitions and additional requirements.
4. **Gold becomes the primary consumption layer.** Legacy CRM Base / CRM Reporting access is going away, so downstream consumers (Genie, SFMC, CDP) must consume from Gold; the required KPIs and attributes must be represented in Gold.
5. **Direction: as much consistency as possible across US, Canada and LATAM**, towards a single consumer profile / source. US definitions are adopted where they work, rather than creating market-specific versions.

## Facts and requirements raised
- Canada has already started a preliminary comparison; Bastien reviewed several KPIs against Canada's reporting and will expand it once SFMC and Genie feedback arrives.
- Canada requires a **3-month period** in addition to MTD / YTD (example given for the Canada catalog).
- Gold-layer **attributes** must be reviewed too, not only KPIs. The US Gold structure is a starting point; Canada decides the attributes it needs. Fatima: the US exercise started with attributes first, KPIs later; for Canada the sequencing depends on priorities.
- **No firm delivery deadline** was committed. Deepti will align with Andres and communicate the dates, possibly separate deadlines for attributes and for KPIs.
- Section 5 of the recap ("Global Standardization vs. Canada-Specific Requirements") has a title but no content; section 6 carries the substance.

## Actions (owner, timing as written)
| Action | Owner | Timing |
| --- | --- | --- |
| Create / share the dedicated Canada KPI Catalog based on the US baseline | Deepti | Next step |
| Review US KPIs and identify Match / Gap / New Canada requirement | Bastien / Canada DDX team | In progress |
| Gather requirements and feedback from SFMC, Genie and other Canada stakeholders | Canada team | In progress |
| Review Gold-layer attributes required for Canada | Canada + Reporting team | Next phase |
| Confirm whether attributes or KPIs must be finalised first for engineering | Deepti / Andres | TBD |
| Confirm delivery deadlines for attributes and KPIs based on implementation needs | Deepti / Andres | To be communicated by email |
| Conduct a focused workshop on identified KPI discrepancies and priority KPIs | All | Next meeting |
| Schedule the next Canada KPI workshop | Ajantha | Next week |

## Next meeting
Moves from approach to the actual KPI review, starting with a manageable set of priority / obvious KPIs, not the whole catalog. Ajantha schedules it for next week (week of 2026-10-12, *inferred* from the receipt date).

## Links to earlier material
- Confirms the use of the US workbook as baseline (CONTEXT.md) and gives a formal frame to Bastien's "reuse and add" approach.
- Raises the stakes of REQ-0001 and REQ-0002: if Gold is the only consumption layer, every KPI and attribute used by SFMC, Genie and CDP must exist there. The Genie gaps (snapshot, new consumer keys, opt-in and unsub dates, CLV, churn flags, segment_type) become Gold requirements.
- Open decisions DEC-0004 to DEC-0007 (definitions of contactable, engagement, new buyer, churn) are now framed by the direction to adopt US definitions where they work.
- Data-team asks ACT-0001 to ACT-0003 (Sandra, Damien, Thomas and Oli) feed the "gather feedback from SFMC and Genie" action. LiveRamp (Damien) is not mentioned in the recap.
- Possible name matches with earlier files, not verified: Fatima (a Fatima Ahmed reported 4 backlog items; a Fatima appears on the "Gold the new reporting" workstream in the deck), Andres (named on the identity resolution and Cassandra workstreams in the deck).

## Open questions
- Date of the next workshop, and who decides priority KPIs?
- Roles and entities of Deepti, Andres, Fatima, Ajantha (Canada, US or global)?
- Which Canada-specific periods besides 3 months are needed?
