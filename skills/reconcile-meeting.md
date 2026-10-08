# Skill: reconcile-meeting

Trigger: a transcript is ingested after a meeting and Bastien asks to reconcile.

1. Run the ingest steps 1 to 3 for the transcript.
2. Load the matching brief in `briefs/`. For each agenda item and pending action, classify: answered, partly answered, not discussed, or not resolved. Never close an item by default.
3. Produce one review: questions answered, proposed actions, changed commitments, explicit decisions, statements that sound like decisions but need confirmation, changed assumptions, new links to historical evidence, remaining questions.
4. Bastien approves or corrects; then update registers, summaries, STATUS and the ingest log.
