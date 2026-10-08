# Skill: prep-meeting
Trigger: "prepare <meeting>".
1. `pm.py show MTG-xxxx` of the previous meeting; `pm.py find <attendee>` for their open actions, commitments, questions.
2. New since then: `logs/ingest-log.md` lines after the meeting date.
3. Write `briefs/<date>_<meeting>.md` (template `templates/meeting-brief.md`): agenda with IDs, open questions, asks per attendee. Register the meeting: `pm.py add meetings ...`.
4. Reply: link to the brief + top 3 points.
