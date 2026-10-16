Subject: Recap of today's Renovate Gold / KPI review (Oct 15)

Hi all,

Thanks for the time today. Here is a quick recap of what we covered and what is still open.

Attendees: Deepti Keelara, Andres Gonzalez, Ajantha Mohanty, Bastien Duthu. Mezyan could not join.

Where Canada stands
- We compared the SuperGold tab against our reporting dashboards and the LiveRamp and SFMC use cases.
- Reporting: about 50 KPIs (plus variants by segment, last year, etc.). Around 10 looked missing and about 15 needed clarification.
- SFMC: around 100 fields requested by the business, still being prioritised on our side.
- Since the call I re-checked our questions against the KPI catalog and BAR tabs. Several KPIs we had flagged as missing are actually there (AOV, repeat rate, retained and reactivated buyers, unsubscribes, engaged prospects, the CLV definition). The real gaps are much fewer than the numbers above.

How to read the workbook
- SuperGold holds the attributes. The KPI catalog holds the calculated values. BAR lists the KPIs behind the US BAR Power BI report used for audience sizing. KPI catalog and BAR are both built in Gold.
- Anything we still can't find, we add as a row in the workbook and discuss it there.

Customer IDs
- Gold uses the brand customer ID as the key of the whole model, plus the global MDM ID. The brand MDM ID is not there today.
- The brand customer ID is an MD5 hash of the brand MDM ID combined with brand code, source and a few other fields. It maps 1:1 to the brand MDM ID, but the hash can't be reversed, so if we need the brand MDM ID it has to be exposed in Gold.
- Andres confirmed IT can expose the brand MDM ID if Canada needs it.
- In the US the brand MDM ID came from Reltio and was dropped. Canada doesn't use Reltio, so the origin of Canada's brand MDM ID needs checking.

PII
- PII is in Gold through the CDP tables (contacts table includes email, phone, address). It just isn't obvious in the workbook.
- Access is a governance question: marketers doing activation should see PII, analysts should not. Likely handled with Unity Catalog groups.

Snapshots and time windows
- Every Gold table carries a snapshot date key (Deepti showed the campaign interaction metric table and the contacts table). It isn't written in the workbook, which is why we missed it.
- This means we can compute any time window ourselves (12 months, YTD, 1 month...) from the snapshots.

Contactability
- First email opt-in date is missing. Deepti is fine adding it since Canada needs it for the in/out flow of contactable customers.
- Unsubscribes are covered in the KPI catalog.

CLV
- The KPI catalog defines CLV (year 1 + year 2 + year 3, each as AOV x frequency x retention), but it is probably not computed for the US. Deepti is checking.

Migration and how we work with IT going forward
- crm_reporting goes away. crm_analytics stays for analytical use cases but will sit on the new Gold. Canada will need to refactor its queries and logic onto the new data model either way.
- Any cleaning or standardisation Canada does today should be sent to IT as requirements, so it is applied between bronze and silver and Gold arrives clean.
- New data sources should go into Renovate. Reporting-only external data (campaign platform data, for example) can be joined outside, but PII should never leave Renovate.
- The reporting layer will sit on top of Renovate and be governed by IT, with KPIs built as Databricks metric views in code, so the Americas share one standard.
- To add KPIs later, Canada can either raise IT stories (IT is planning dedicated capacity and a reporting data engineer) or contribute directly through pull requests in the pipeline.

Follow-ups
- Deepti: where Canada's brand MDM ID comes from; confirm in writing where PII sits and that every table has snapshots (and how much history); confirm whether CLV is actually computed.
- Andres: PII access rules (who sees what, Unity Catalog groups).
- Bastien: go through the remaining questions against the KPI catalog and BAR and send the updated list; decide whether Canada needs the brand MDM ID (check which exports and reports join on it today, LiveRamp at least); list Canada's cleaning and transformation rules; list Canada's analytical use cases beyond reporting (CLV, segmentation models, activation feeds).
- Ajantha: send the meeting follow-up and schedule the next session next week, same time. We'll share the agenda beforehand and skip it if there is nothing to discuss.

Still open beyond today
- Engagement: the US counts clicks, reviews, purchases and site visits but not opens. Canada counts clicks or opens. We need to agree on one rule.
- Campaign attribution: rule and window used in Gold, and whether Canada can keep 3, 5 and 7 days.
- Paid media contactable records: the KPI exists in the catalog but has no definition yet.
- Brand exclusions per KPI (Canada excludes some brands): no place for this in the catalog yet.
- Refresh cadence and Canada delivery dates.

Thanks,
Bastien
