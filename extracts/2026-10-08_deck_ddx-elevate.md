# Extract: "From Renovate to Elevate" deck (DDX Elevate)

- Type: deck (PDF export, 21 pages)
- Date of input: dated March 2026 on the cover (file name says "latest"; export made 2026-10-08)
- Original: raw/2026-10-08_deck_DDX-Elevate-latest.pdf
- Author / audience: not stated (programme-level deck, "C1 - Internal use")
- Ingested: 2026-10-08
- Reading note: text extracted from the PDF; roadmap charts and the architecture diagram lose their layout, so dates read from charts are marked *inferred*.

## Key points
- Elevate is positioned as the next phase after Renovate: "from Renovate to Elevate, scaling the Americas consumer data ecosystem". Rationale: AI-ready marketing, real-time orchestration, agentic commerce. (documented)
- Current situation: the CDP was enabled on AWS, Databricks and Hightouch; legacy remains expensive but still serves active B2C and B2B demand in 3 regions. Foundational capabilities (control, trust, stability) are incomplete. (documented)
- Renovate results claimed: 1000+ tables down to under 100; 1200+ jobs down to under 300; deployment 48x faster (98% less time); about 30% lower compute and egress costs. (documented, claims by the deck)
- Path chosen: "controlled transition": protect continuity (e.g. B2B), freeze non-essential legacy enhancements, focus investment on Databricks remediation. B2C moves first; B2B stays temporarily in legacy. (documented)
- Target stack: Databricks (medallion, Unity Catalog, Lakebase) retained and expanded; Cassandra, DynamoDB, Lambda, microservices, Java UDFs migrated or retired; AWS S3 and API Gateway retained.
- Decisions still under validation: role of Hightouch (scheduling vs real-time identity resolution needs) and whether Reltio is retained or evolved depending on the identity resolution (IDR) pattern. (documented, as of March 2026)
- Roadmap (proposal): CDP onboarding in waves 1 to 8 from Q3 2026 to Q1/Q2 2028, with a pilot in Q2 2026 ("we are here" marker at Q2 2026). Canada and LATAM consolidated into one Americas DDX instance. Canada onboarding appears in 2027 and LATAM onboarding later in 2027 / early 2028, "planning tbc". (dates *inferred* from chart layout)
- Workstreams named: Bronze refactoring, Cassandra redesign, API upgrade/refactor, legacy features transfer (privacy, NPS, GDM...), IDR and survivorship, "Gold the new reporting", Canada/LATAM onboarding, B2B medallion upgrade, environments enablement, WAF (well architecture framework) discovery and activities.
- Delivery: Renovate is currently delivered by Databricks Professional Services, pending transition to an SI. Several first names appear against workstreams (Luis + Jagan, Eleazar + Allan, Alam, Andres, Fatima); roles not stated.

## Budget
The deck contains 2025 to 2027 budget figures. Bastien (2026-10-08): not relevant to this project's current scope; the deck is context only. Figures intentionally not summarised here; see the original in raw/ if ever needed.

## Findings on the current platform (inbound/outbound review)
Prod data replicated to staging incl. SFCC data (flagged as a serious security concern); 2025 Databricks compute cost about $2 M; over 1000 DynamoDB tables; S3 about $100 k per month; Cassandra 24 servers and a disaster recovery plan never tested; Reltio at 76 M records versus a 70 M quota, 4 M to clean; Attentive has only a production environment (risk of triggering test files); Tableau to be moved to Power BI in the CDP RFP.

## Decisions
- None recorded as explicit. "Controlled transition" is presented as the proposed path: treat as *needs confirmation*.

## Actions and commitments
- None with owner and date in this deck.

## Requirements and datapoints touched
- Gold layer is positioned as the future reporting source ("Gold the new reporting"); KPI catalog / reporting KPIs budgeted at 296 k in 2026. Links to the Gold Layer workbook.

## Open questions
- Is a version later than March 2026 available? The timeline and "we are here" marker may be out of date.
- Who owns each workstream (first names only in the deck)?
