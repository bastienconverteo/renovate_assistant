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
