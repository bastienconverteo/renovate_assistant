# Project context (stable facts)

Small details are kept here on purpose: Bastien asked that anything possibly relevant be captured, because it may connect to a later call transcript or email. Each fact has a source and date. Newer facts replace older ones; do not delete, mark as superseded.

## Perspective and scope
- Bastien is the project manager on the **Canada** side of Renovate (Bastien, 2026-10-08: "We are Canada"). Renovate overall builds a common super gold layer in Databricks for the Americas (USA, Canada, LATAM). [documented]
- The **US team built the workbook** "Gold Layer Domain Data Requirements" and its SuperGold layer. It is US-specific. Canada will likely reuse a lot of it and add new potential endpoints. [documented, Bastien 2026-10-08]
- LATAM comes later. The Elevate deck (March 2026) shows Canada onboarding in 2027 and LATAM later in 2027 / early 2028, "planning tbc". [inferred from chart]
- US people named in the workbook and deck are US-specific and not tracked for now. [documented, Bastien 2026-10-08]

## Current task: complete the Gold layer data-element mapping
- Bastien asked the data teams, by email (2026-10-08), to document every data element used by downstream products and activation platforms (SFMC, LiveRamp, Attentive, Genie, others) in the workbook sheet "All Domains - SuperGold", and to send him their list so he can update the file. [documented]
  - Sandra: SFMC and Attentive. Damien: LiveRamp. Thomas and Oli: Genie. Surnames unknown.
  - Deadline: "asap", no due date. Report them as **pending** in every status and brief until they reply. [documented, Bastien 2026-10-08]
- Second objective: check that every KPI used in reporting can be found in the workbook. The list of KPIs used in reporting is in **Databricks**. Bastien gives the workbook and a prompt to Databricks (Genie), which analyses with the data context. The prompts are in `prompts/`. [documented]

## Source material notes
- The Elevate deck is for context only. Its budgets are not relevant to this project's current scope: do not surface them. There is no deck newer than March 2026. [documented, Bastien 2026-10-08]
- Workbook READ ME says the sources of truth for the gold layer are the sheets All Domains, BAR Activation KPIs and KPI Catalog. Bastien's email directs teams to "All Domains - SuperGold". [documented]
- Workbook sheet "D2C KPI Catalog - LU 5-8" has 958 KPI rows; Databricks/Genie checks exist for only a handful. [documented]

## Lessons from the US backlog to check for Canada (from the workbook, not Canada facts)
- SFMC and Attentive did not send geotracking and operating system data to the US gold layer (BL-055, BL-056).
- Primary email, phone and address rules were still being defined (BL-065 to BL-067).
- Birth date 1900-01-01 values needed nullifying, pending SFMC feedback (BL-081).
- Some Attentive event cleansing was rolled back on Aug 21 (BL-068, BL-075).
- The US is moving to a "Diamond" target schema (BL-085 in progress).

## Working preferences (Bastien)
- Wants quick answers to "what is the impact of this decision" and "generate a status" without searching documents or mails.
- Ingestion by dropping files in `inbox/` or pasting emails and ticket threads (ServiceNow) in the chat; approves change sets before registers change.
- Folder lives on his Mac at ~/Documents/Projects/renovate; git identity bastien.duthu@converteo.com; remote renovate_assistant on GitHub (pushed by Bastien).
- IT approved the proof of concept as a personal tool (no compliance gate for now); revisit before sharing wider.

## Added 2026-10-08 (evening): Canada reporting vs SuperGold (from Genie's analysis, verified by Claude against the workbook)
- A **KPI catalog workshop** is upcoming (date and attendees unknown). Genie's notebook was prepared for it. Source: raw/2026-10-08_genie-analysis_canada-kpi-cross-reference.md. [documented]
- Canada reporting assets analysed: DDX CA B2C Executive Report (DDX Scorecard, source `fact_customer_segment_by_brand`; CLV Deepdive, source `vw_fact_order_sales`), CA B2C Campaign Performance Report (`fact_message_tracker`), Liveramp Customer 360 Canada dashboard (`vw_customer360_liveramp`). Current reports query `crm_reporting.*` and `crm_base.*`. [documented]
- Biggest finding: Canada executive reports are monthly snapshots (`snapshot_year_month`); SuperGold is current-state only. Also missing in SuperGold: new consumer status keys, email opt-in and unsubscribe event dates, CLV, retention, churn flags, engaged prospects flag, segment_type. 14 of 32 report KPIs are fully present. [documented, gaps verified]
- Canada uses `brand_mdm_id` / `global_mdm_id` (Reltio MDM) where SuperGold uses `brand_customer_id` / `global_customer_id`: unresolved. [documented]
- Canada-specific needs: `preferred_language` EN/FR (the field already exists in `cdp__identity_v`), `brand_country = 'CAN'`, excluded brands SHUUS, BIOUS, DER, BO (to confirm), French-language campaigns in SFMC. [documented by Genie]
- Refresh cadences in use: BAR KPIs monthly, CLV quarterly, campaign performance monthly, LiveRamp weekly or as needed. BAR dashboard is in PowerBI on `cdp__bar_kpi_v` (52 KPIs). [documented by Genie]
- Genie's notebook is design-level (report logic versus SuperGold definitions). It did not test which Canadian tables hold which fields, fill rates or value sets: prompts A and B remain useful. [documented]
- Correction: SuperGold has 479 field rows (not 454); counts in earlier notes are fixed.

## Added 2026-10-08 (night): KPI workshop 1 recap
- First Canada KPI workshop held (date not stated); written recap in raw/2026-10-08_workshop-summary_kpi-workshop-1.md, extract in extracts/. [documented]
- Agreed: US KPI catalog is the baseline; Canada classifies KPIs as Match / Gap / New; first focus is consumer funnel, KPI name and definition (dimensions later); a dedicated Canada D2C KPI catalog will be created; Gold becomes the primary consumption layer; keep consistency across US, Canada and LATAM and adopt US definitions where they work. Canada needs a 3-month period in addition to MTD / YTD. No firm delivery deadline. [documented]
- People: Deepti (creates the Canada KPI catalog; aligns deadlines with Andres), Andres, Fatima (noted the US exercise started with attributes first), Ajantha (schedules workshops). Roles and entities unknown. These are Canada workshop participants and are tracked (supersedes "US names are not tracked" for them; US backlog reporters in the workbook remain untracked). [documented]
- Next workshop: Ajantha to schedule for next week (inferred week of 2026-10-12); it starts with a manageable set of priority / obvious KPIs. [documented]
- Registers were populated on 2026-10-08 after Bastien's "approve all" (change sets 001 and 002); the workshop recap was applied in the same pass because it came with the instruction to add it to memory. Bastien can correct any row.

## Added 2026-10-08 (late): workshop 1, second summary reconciled with the first
- Roles: Deepti leads reporting and analytics on the IT side for all zones (defines what Gold looks like: KPIs and attributes); Andres manages implementation and data engineering on the IT side for all zones; Ajantha is the Project Manager for Renovate bridging US, Canada, LATAM. Bastien is the Canada-side project manager (Ajantha is the programme-level PM). [documented, summary v2]
- Governance: Gold is a global initiative meant to be uniform; local adjustments are possible for specific business needs (example given: brand-specific definitions such as "active customer"); otherwise align with US definitions to keep one source of truth. [documented]
- Purpose restated: move from separate CRM Base and CRM Reporting to one unified Gold layer; downstream SFMC, Genie, CDP must be supported by Gold. [documented]
- Unresolved conflict: version 1 says Fatima noted the US started with attributes first; version 2 says Mezyan suggested starting with attributes. Possibly one person. [to confirm with Bastien]
- Text quirks: "goal layer" = Gold layer; the Canada sheet is called "T2C KPI catalog Canada" in v2 and "D2C KPI Catalog" in v1 (probably D2C). [inferred]
- Both summaries agree on the core; details of the comparison in extracts/2026-10-08_workshop_kpi-workshop-1-summary-v2.md.

## Added 2026-10-08 (night): Mezyan's role, Damien's reply, business-first principle
- Mezyan is Bastien's boss: Project Manager and responsible for the Canada data teams. Probably a separate person from Fatima (workshop summary version 1 says Fatima, version 2 says Mezyan for the attributes-first remark; still unresolved). [documented, Bastien]
- Damien (Canada team, in charge of LiveRamp) answered the data-element request: he shared the LiveRamp data schema, linked to the file Canada sends weekly, and added two missing fields: sub-categories (anti-aging, suncare, etc.) and Is_Churn_12M_36M (to create a lapsed buyers segment). The schema itself is not in the repo yet (ACT-0019). [documented, Bastien relayed]
- Neither field exists in SuperGold (product_category exists, no sub-category; no churn flag; lapsed_buyer_status_key has 12, 24, 36 month buckets and may cover part of the churn need, inferred). Registered as REQ-0013, REQ-0014, DP-0480, DP-0481.
- Genie had also suggested churn 12-24 / 24+, engaged prospects L12M and segment_type. Kept as suggestions to put to the business (ACT-0018).
- Principle (Bastien): requests from business teams carry more value than attributes predicted by Genie or any other LLM; still record LLM suggestions and ask the business whether they are relevant. Label them "suggested by Genie" versus "requested by <team>". [documented, preference]
- Source: raw/2026-10-08_message_damien-liveramp-reply.md; extracts/2026-10-08_message_damien-liveramp-reply.md.
