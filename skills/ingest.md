# Skill: ingest

Trigger: Bastien drops a file in `inbox/` or pastes content (call transcript, ServiceNow thread, workbook, deck, ticket export) and asks to add it.

Steps
1. Save the original to `raw/<yyyy-mm-dd>_<type>_<short-name>.<ext>` (pasted text becomes a .md file). Do not alter it.
2. Write an extract in `extracts/` using `templates/extract.md`. Keep decisions, actions, commitments, dates, quotes; leave bulk data in the raw file. Mark evidence `documented`, `verbal` or `inferred`.
3. Compare with existing registers: related rows, contradictions, overlapping datapoint names or definitions (check by country), regional differences.
4. Present a change set: new rows, changed rows (old -> new), contradictions to confirm, links found (which datapoints, requirements, decisions, stakeholders this touches). Ask: "this touches X, Y, Z, correct?"
5. After approval only: update registers, refresh affected summaries and `STATUS.md`, add a line to `logs/ingest-log.md`, update `INDEX.md` if a topic appeared.

Special cases
- ServiceNow list export: diff against the previous export in `raw/`; report new, closed, re-prioritised and slipped tickets; map tickets to stories.
- Call transcript: correct names and terms using `GLOSSARY.md`; flag unclear speaker attribution.
- Workbook: profile sheets (purpose, key columns, row counts); never paste whole sheets into memory.
- Sounds like a decision but not explicit: record as `needs_confirmation`, never as an explicit decision.
