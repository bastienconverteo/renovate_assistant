# Renovate (Canada): governance proposal

Draft for Bastien, 2026-10-08, updated 2026-10-09 with Bastien's answers. Built from the stakeholders, decisions, actions and commitments registers (ingest 004) and the v0.2 context. Nothing in the repo was changed.
Legend: **R** does the work, **A** accountable (one per line, final say), **C** consulted before, **I** informed after. `*` = role inferred, not documented. `?` = nobody named in the registers.

## 1. Principles
1. Gold is global and uniform (DEC-0014). Deepti decides Gold design at programme level, but Canada weighs in on every decision before it is taken: Canada will migrate all its dashboards and use cases to Gold, so any decision that adds adaptation work after go-live must be argued out first (Bastien, 2026-10-09).
2. Canada's job is to bring evidence and demand: Match / Gap / New against the US baseline (DEC-0011), data-team needs, report coverage.
3. Every open decision gets one named decider and a target meeting. Today all of DEC-0001..0010 have `decided_by: unknown`.
4. Meetings produce decisions, actions and commitments that land in the registers within a day. No decision lives only in a recap email.

## 2. RACI

People: **Bastien** (Canada PM, Canada business owner with Mezyan), **Mezyan** (your manager, PM for Canada data teams, Canada business owner of KPI definitions and Canada completion; the "Fatima" in workshop recap v1 is Mezyan), **Ajantha** (Renovate PM, all regions), **Deepti** (IT reporting and analytics lead, defines Gold), **Andres** (IT implementation and data engineering), **Data teams** (Sandra SFMC/Attentive, Damien LiveRamp, Thomas and Oli Genie), **DDX team** (Canada reporting team doing Match/Gap/New).

| # | Activity | Bastien | Mezyan | Ajantha | Deepti | Andres | Data teams | DDX team |
|---|---|---|---|---|---|---|---|---|
| 1 | Workshop planning and scheduling (COM-0003) | C | I | A/R | C | C | I | I |
| 2 | Attributes first or KPIs first, and delivery timeline (DEC-0017, COM-0002) | C | I | C | A/R | R | I | I |
| 3 | Create the Canada KPI catalog (COM-0001) | C | I | I | A/R | I | I | C |
| 4 | Match / Gap / New review of US KPIs (ACT-0010) | A/R | I | I | C | I | I | R |
| 5 | Collect data elements from data teams (ACT-0001..0003) | A | I | I | I | I | R | I |
| 6 | Gap analysis and consolidation into the workbook (ACT-0006, ACT-0020) | A/R | I | I | C | C | C | C |
| 7 | One Gold definition of contactable, engagement, new buyer, churn (DEC-0004..0007) | R (Canada position) | C | C | A | C | C | C |
| 8 | Snapshots, derived KPIs, ID naming (DEC-0001..0003) | C | C | C | A | R | I | C |
| 9 | Canada-specific attributes, refresh cadences (DEC-0008, DEC-0009) | R (proposes) | C | C | A | C | C | C |
| 10 | Migration path from crm_reporting / crm_base (DEC-0010) | C | C | C | C | A/R | C | C |
| 11 | Escalation and priority calls for Canada | R | A | I | I | I | I | I |
| 12 | Build Gold (views, pipelines) | I | I | I | C | A/R | C | I |
| 13 | Test: reproduce Canada reports from Gold (KPI values match) | C | I | I | C | R | I | R |
| 14 | Downstream cutover (SFMC, LiveRamp, Genie read from Gold) | C | A | I | C | C | R | I |
| 15 | Business sign-off for Canada (KPIs, Canada completion) | R | A | C | C | C | C | C |
| 16 | Cross-region consistency (US / Canada / LATAM) | C | I | A/R | R | C | I | I |
| 17 | Canada KPI definitions (business side): Canada position on each definition | R | A |
| 18 | Project memory: registers, status, decision log | A/R | I | I | I | I | I | I |

Reading the table: Deepti owns what Gold contains, Andres owns how it is built and migrated, Ajantha owns the cross-region calendar and consistency, Canada (Bastien and Mezyan, business owners) owns demand, its position on every definition, and acceptance. Mezyan holds the final Canada word until you name someone else (Bastien, 2026-10-09: they will align and say if someone else has the final word). Mezyan is C, not I, on rows 7 to 10 because Canada wants to weigh in before Gold design decisions.

## 3. Settled and still open
Settled (Bastien, 2026-10-09):
- Workshop 1 = "Renovate KPI Workshop", 2026-10-07.
- Mezyan and Fatima are the same person; there is no Fatima. The v1 recap wrote "Fatima" where v2 wrote "Mezyan" for the same "attributes first" remark, probably a transcription error. (A Fatima Ahmed in the US workbook backlog is an unrelated US name.)
- Mezyan and Bastien are Canada's business owners of KPI definitions and of project completion for Canada. They may name someone else with the final word later.
- Canada weighs in on all Gold design decisions to minimise post-migration adaptation work.

Still open:
- Does a cross-region Renovate meeting already exist (Ajantha)?
- Who tests on the IT side, and who does Canada UAT?
- Data teams' entity and manager; who can commit them to dates?

## 4. Meeting organization

| Meeting | Status | Who | Cadence | Inputs | Outputs |
|---|---|---|---|---|---|
| **KPI / attribute workshop** | Exists (workshop 1 held; no. 2 week of 2026-10-12, Ajantha schedules) | Ajantha (chair), Deepti, Andres, Bastien, DDX team | Weekly while Match/Gap/New is running, then every 2 weeks | Short priority KPI set with Match/Gap/New (ACT-0017), open DEC list | Decisions DEC, updated Canada catalog, actions with owners and dates |
| **Gold design decisions** (30 min) | Add | Deepti (decider), Andres, Bastien, Mezyan; Ajantha optional | Every 2 weeks, right after the workshop | DEC-0001..0010 with Genie options, and Canada's position with its adaptation cost per option | One decision per item or an explicit deferral with a date. Could be the last 30 min of the workshop at first |
| **Data teams sync** (30 min) | Add, replaces email chasing | Bastien, Sandra, Damien, Thomas, Oli; Deepti on demand | Every 2 weeks until lists are in, then monthly | Workbook "All Domains - SuperGold", pending asks ACT-0001..0003, Genie questions B1-B10 | Confirmed data element lists, new REQs, dates |
| **Canada weekly 1:1** (30 min) | Add if not existing | Bastien, Mezyan | Weekly | Status, risks, escalations, decisions needed | Priorities, escalations, sign-off path |
| **Cross-region sync** | Unknown, confirm with Ajantha | Ajantha, Deepti, Andres, regional PMs | Monthly | Regional status, consistency issues | Alignment on definitions across US / Canada / LATAM |
| **Delivery timeline checkpoint** | Add later, once Deepti and Andres publish dates | Deepti, Andres, Bastien | Monthly | COM-0002 timeline, progress | Re-plan, risk flags |
| **Build and test checkpoint** | Add when engineering starts | Andres, Deepti, Bastien, DDX team, data teams | Every 2 weeks during build | Test results vs current reports | Defects, cutover readiness |

Drop or avoid: separate one-off calls per data team, and recap emails as the only record. Do not create a standing steering committee yet: no firm deadline (COM-0002) and no budget discussion in scope.

## 5. How each meeting feeds the repo
Weekly rhythm already in ARCHITECTURE.md: Monday prep-meeting, Tuesday workbook ingest, Thursday reconcile transcript, Friday exec-update.

| Step | Meeting | Prep (before) | Reconcile (after) |
|---|---|---|---|
| Mon / Tue | Workshop | Brief from digest: open DEC, Match/Gap/New status, pending COM | Biscotti transcript or recap ingested; new DEC, ACT, COM with owner and date; contradictions go to QST |
| Tue / Wed | Design decisions | `pm.py impact DEC-xxxx` for each item | Close DEC with `decided_by`, date, rationale; list newly unblocked ACT |
| Thu | Data teams sync | Pending list per team, questions B1-B10 | Update ACT-0001..0003, new REQ, new datapoints |
| Weekly | Canada 1:1 | Status from digest | Escalations and priorities as ACT or BLK |
| Fri | Exec update | Status generated from registers | Sent to Mezyan; replies ingested as new inputs |

## 6. First moves
1. Bastien and Mezyan write Canada's position on DEC-0001..0010 (preferred option, adaptation cost of each alternative) before the decision meeting.
2. Ask Ajantha to reserve 30 min at the end of workshop 2 (or a separate slot) to go through those decisions with Deepti and Andres.
3. Start the biweekly data teams sync, since three asks have no due date.
