# Skill: ingest
Trigger: a file in `inbox/` or pasted content (email, transcript, ServiceNow thread, workbook, deck).
1. `pm.py add sources title=... type=... date=... raw=... extract=...`. Save the original to `raw/<date>_<type>_<name>` unchanged (personal data rows stay in `inbox/`; keep only structure in raw).
2. Write `extracts/<date>_<type>_<name>.md` (template `templates/extract.md`): facts, decisions, actions, quotes, with evidence labels. Correct names with `GLOSSARY.md`.
3. Compare: `pm.py find <key terms>` and `pm.py impact <touched IDs>`. Contradiction → `pm.py add questions ...` (never overwrite).
4. Apply (if Bastien said add/approve) or propose: `pm.py add <register> k=v ...` / `pm.py set ID k=v ...`, with `src=SRC-xxxx`. Something that sounds decided but is not explicit → decision status `needs_confirmation`.
5. Update `CONTEXT.md` only for new stable facts or preferences; `STATUS.md` only if the headline or risks change.
6. One line in `logs/ingest-log.md`: `date | SRC-xxxx name | + IDs | ~ IDs`. Then `pm.py check` and commit.
7. Reply in the 5-line ingestion format (AGENTS.md).
Special: ServiceNow export → diff against the previous export, list new / closed / slipped tickets. Workbook → profile sheets, never copy whole sheets.
