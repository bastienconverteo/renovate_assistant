Source: transcript of workshop 2 (KPI / Renovate gold layer review), 2026-10-15, pasted by Bastien in the project thread at 15:57 UTC. Content below unchanged.

---

# Meeting transcript – KPI / Renovate gold layer review (0:00 – 41:48)

Participants: Bastien Duthu (Converteo), Deepti Keelara, Ajantha Mohanty (Wipro), Andres Gonzalez.
Source: reconstructed by OCR from the scrolling transcript in the screen recording. `[…]` marks short passages that scrolled by too fast to be read; `[?]` marks an uncertain word or speaker. The sections 13:33–16:39, 18:18–20:11 and 32:56–41:28 were completed from text copied directly from the original transcript.

---

**Bastien Duthu (0:03)** – I have a sort of priority list of all the KPIs we identified that were missing from the file, or on which we had questions, and I was hoping we could at least start going over them and try to clarify how we see the different visions.

**Deepti Keelara (0:28)** – Okay.

**Bastien (0:30)** – So, I'm going to share my screen.

**Deepti (0:32)** – Yes, please.

**Bastien (0:35)** – Maybe you're right, my computer could be the problem. Right, so Mezyan is not going to join. I'll take it. Can you see my screen?

**Deepti (0:54)** – It's loading.

**Bastien (0:56)** – All right.

**Deepti (1:02)** – It stopped loading. I don't see anything anymore.

**Bastien (1:07)** – I'm a digital native, just so you know. I'm supposed to know this kind of thing. And it says I'm…

**Deepti (1:10)** – Yeah.

**Bastien (1:18)** – Sharing, so…

**Deepti (1:20)** – Can you unshare and share again? I don't know if that helps.

**Bastien** – Yeah, yeah. Yeah, my laptop is on its knees right now. […]

**Ajantha Mohanty (1:47)** – This is my 4th laptop, by the way. Every six months it breaks down and then I have to get a new one.

**Bastien (1:47)** – We see you.

**Deepti (2:05)** – That's good, yes.

**Bastien (2:09)** – All right, so what we did so far was that we went through all of the KPIs which were in this Super Gold tab, and compared them to our reporting needs and to the different use cases, like LiveRamp and so far SFMC.

**Deepti (2:22)** – Done.

**Bastien (2:28)** – And we just reviewed what was needed and raised a few questions. For reporting, I believe we are almost exhausted. There are a few more KPIs, but they fall back into the broad categories we have here. And for SFMC, we are still reviewing them because we have maybe 100 or so which were requested by the business team. I went through a priority list to get the biggest ones, but we still need to really challenge and go through all of the priorities which the business raised. Do you have any questions so far?

**Deepti (3:14)** – So, when you say Canada questions, are those for us or for you?

**Bastien (3:21)** – No, it's for you actually. It's more of a definition alignment, making sure that what we have and what we use in Canada can be replicated in the gold layer of Renovate.

**[Wipro/IT side, speaker unclear]** – So, Bastien, percentage-wise, how many were a 100% match? And how many do you think need analysis, like a gap analysis?

**Bastien (3:56)** – Now, in percentage of what do you mean?

**[Same speaker]** – The KPIs that you were able to do a one-to-one mapping of. Just an approximate, yeah.

**Bastien (4:25)** – So this is really just for the reporting dashboards that we have, and for this we have 50 KPIs, plus there are variants of course, like the different segments, last year, etc. Of those 50 KPIs we had maybe […] ten that we're missing altogether, and sort of 15 where we had some questions or we need to clarify.

**Ajantha (4:52)** – Okay. So 50-50 it seems, okay.

**Bastien (5:01)** – Yeah, it seems like it. […]

**Deepti (5:23)** – So for the ones that you have from line 505 on, is that all the questions you have, right?

**Bastien (5:27)** – Yes. It's not entirely exhaustive, no. It's the main ones and the ones for which we are sure that we have some questions. And for like 15 or so others, we still need to deep dive.

**Deepti (5:45)** – One question: some of it we can get back to you on. For example, snapshot – I know already it's there, I'll answer those questions. But for identity, I'm not sure what they have. […] As for brand MDM ID, we're not going to have brand MDM ID, we're only going to have brand customer ID.

**Bastien (6:08)** – Yeah? The difference between them being that the MDM is being hashed. Is this right, correct?

**Deepti (6:23)** – The brand customer ID is hashed. Yes. […] if multiple brands, then you do get it rolled up to the L'Oréal level. That's a global MDM ID, but I don't know if I understand what they […]

**Bastien (6:51)** – Yeah, exactly. What's the difference between the MDM and the global? And especially, since one is hashed and the other not, are both of them being included in the table so that we can also do the joins back on our end, or in the different other use cases we might have? It's actually just this question. Because I think I saw that there was only the brand customer ID in the file.

**Deepti (7:32)** – Right, we only have brand customer ID and global MDM ID.

**Deepti (7:37)** – I don't think we have brand MDM ID. Do they need brand MDM ID? Is that what the question is?

**Bastien (7:38)** – Yeah, exactly. Because you mentioned the brand customer ID is the one that's being hashed.

**Deepti (7:54)** – Brand customer ID is hashed, yes. Even in our current environment, brand customer ID is hashed.

**Bastien (7:54)** – Yes, but since you don't have the MDM ID, how do you reconcile both of these data?

**Deepti (8:04)** – Yeah.

**Bastien (8:07)** – You just apply the reverse hashing to the brand customer ID to get the regular MDM ID and then join back on this for all the use cases?

**Deepti (8:15)** – So, let me explain what a brand MDM ID is today and what a brand customer ID is. Brand MDM ID is generated and sent by Reltio, and brand customer ID is generated in DDX. So brand customer ID is basically a hash of brand code plus brand country and, you know, MDM source and, you know, brand MDM ID. Brand customer ID has multiple different components and it gets hashed. That's what a brand customer ID is. From what I understand – I can double check with Databricks – that's how they're calculating brand customer ID. Brand MDM ID was a Reltio-generated ID. In Canada, I don't know what it is; I'll get back to you on that. Canada doesn't use Reltio, right?

**Bastien (9:04)** – Nope.

**Deepti (9:05)** – Okay. Fair question. Let me take that question, because in the US they are only using brand customer ID because we had the Reltio ID and decided not to use that anymore. But I don't know what the reasoning is in Canada. Let me get back to you on that question.

**Bastien (9:20)** – All right. Okay, so yeah, perfect. We then need to get a clear view of this, because if not, it means that we'll need to do some additional work on our end to make sure that we can reconcile the data on this ID.

**Deepti (9:46)** – Yeah, fair point. I hear your concern there. Let me check with Andres about this ID. Hopefully he can join and we can ask him during the call.

**Ajantha (9:56)** – So just from my understanding, Canada has MDM ID an[d] […]

**Deepti (10:11)** – […] only has email per […], I'm going through each of them.

**Bastien (10:19)** – Yeah.

**Deepti (10:25)** – Can you…?

**Bastien (10:27)** – Yeah, sorry, yeah.

**Deepti (10:28)** – Can you elaborate – sorry, can you expand column G? I can only see a little bit.

**Bastien (10:36)** – Yes, oh yeah. So column G is actually where we have more of a question: where are the PII stored that we need for activation and for the personal identification of customers?

**Deepti (10:59)** – Because of CDP, today it's in gold. They brought everything to gold.

**Bastien (11:03)** – So gold being the gold layer that we're talking about here for Renovate, right?

**Deepti (11:10)** – Yes.

**Bastien (11:12)** – And so, because I couldn't find it in these fields. But maybe I looked wrong.

**Deepti (11:23)** – Everything that a CDP should have, it has.

**Bastien (11:30)** – All right.

**Deepti (11:33)** – All right, let me help you with that one. From what I und[erstand] […] But I don't know why I don't see it. Let me check. Regardless, the data should be here in the gold layer, so it's something that we will be able to have. For activation, yes. So obviously who will have access to what? For activation we should have it. For reporting, not everybody will have access, if that makes sense. Because…

**Bastien (12:13)** – On what would it be based, when you say not everyone?

**Deepti (12:20)** – I think, for example, analysts should not have access to PII, right? But somebody who's a marketer who's using it for activation should be able to have access. So that's more of a governance question. I will take that question back and get back to you. I don't want to answer something that… Like, that's more of an Andres thing.

**Bastien (12:44)** – Okay, is this something that can be related to RLS? Or is it unrelated and we don't have this in Databricks?

**Deepti (12:56)** – Yeah, in gold, is that what we're talking about?

**Bastien (13:01)** – Yeah, I was wondering how the differences could be made between someone who is in marketing and someone who is in digital or analytics, like…

**Deepti (13:12)** – I think that's a definition. I think you can create it in Unity Catalog, like groups where you can put them in. So let me quickly pull up something. Give me one second. I want to check. I thought we have all the PII in the CDP tables. We should have it, because CDP can only work with PII.

**Bastien (13:18)** – Okay. Right.

**Deepti (13:33)** – I'm just double-checking why it's not in that document.

**Bastien (14:02)** – Oh.

**Deepti (14:50)** – Yeah, I need to take this question back. I am not able to find it, but my understanding was that everything in CDP had PII, unless it's past or something [?]. Let me figure that out. Okay.

**Bastien (14:53)** – Okay. Yeah. Okay, thank you. I saw a lot of CDP fields, of course, but it was more about whether they are indeed in clear text or not. Okay, thanks.

**Deepti (15:22)** – One question on the line – or maybe we'll go line by line, that way we're not jumping back and forth, so…

**Bastien (15:22)** – Um, 15, we can, yeah. I mean, we can do it if anything catches your eye, let's go ahead, but yeah, we can go line by line. They're not in any sort of priority list, really.

**Deepti (15:43)** – Okay.

**Bastien (15:44)** – But this one we can skip. I found it.

**Deepti (15:45)** – OK, this is…

**Bastien (15:53)** – One question I had was about the contactability, where we have a KPI on the flow – the in and out flow of users – where we need the first opt-in date and the email unsubscribe date.

**Deepti (15:58)** – Okay.

**Bastien (16:12)** – Which I'm not sure I could find. These we can take offline. I don't expect you to have the answer right now, but if you have any questions about them, we can of course answer them. It's something you don't have to take right now.

**Deepti (16:31)** – First opt-in. So, contactability, to your question, is first email opt-in date.

**Bastien (16:39)** – Right.

**Deepti (16:40)** – It's missing.

**Bastien (16:41)** – So this way we can compute the number of people who are, the current rate of people who are contactable, you know.

**Deepti (16:52)** – So, I mean, if that's missing and absolutely needed for Canada, yeah, we are okay adding it. That's the whole point of this exercise, right? We are trying to get some of the KPIs […] we can add it. It just… Yeah, if this is important for you, then yep, that makes sense.

**Bastien (17:12)** – Yeah. Awesome. And by the way, I'm making a side note here: all of the KPIs can be made with different brackets, you know, like with a 12-month look-back, or one month, or year-to-date, or this kind of thing. Are they all being stored as such, or can they be computed using, say, snapshots like we saw here in the first line?

**Deepti (17:47)** – What do you mean, like…?

**Bastien (17:50)** – I mean, say, for the number of new contacts: are the KPIs stored as a rolling 12-month number of new contacts, or as a number of contacts at one point in time that we then need to look back into the snapshots for, to make the difference and get the number of contacts 12 months ago versus right now? Do you see what I mean? And maybe…

**Deepti (18:18)** – At a customer level, right? Give me one second. I'll show you how it looks.

**Bastien (18:20)** – Yeah, for instance.

**Deepti (19:29)** – So we do have snapshots. So your question is, for every KPI – like we have it in fact customer segment by brand – is that what you're trying to look for, like an [equivalent?] table?

**Bastien (19:29)** – Yeah. Okay. Thank you. (19:46) So, sorry, can you say again? So you do have some snapshots.

**Deepti (19:50)** – We do have snapshots, but it's…

**Bastien (19:50)** – Like, I'm using monthly separate [?]…

**Deepti (19:54)** – For every KPI, you have snapshots and you will see the trend over a period of time. So let me show you how it looks and then you tell me if this makes sense for you.

**Bastien (19:56)** – Yeah. Okay.

**Deepti (20:06)** – So you'll have a… Are you able to see my screen?

**Bastien (20:11)** – It's coming up. Yep, it's good.

**Deepti (20:17)** – So this is a campaign interaction metric table. You will see a snapshot date key of, like, 8, which is I guess August. And then you will see the different attributes and so on at that level.

**Bastien (20:25)** – Right.

**Deepti (20:36)** – So this is a lot more granular, but even for […] thing. So this is what you're expecting, right?

**Bastien** – Yes, yes, exactly. Okay, perfect. Yeah, okay, I was not aware that there was the snapshot, indeed I didn't see it.

**Deepti (20:49)** – Okay.

**Bastien (20:57)** – But this is a…

**Deepti (20:58)** – Maybe they never put it in the document, but from what I know we do have it. I'll answer that question for you as part of my review.

**Bastien (21:04)** – Okay. I'll make a full recap anyway of whatever we said, so…

**Deepti (21:15)** – Yeah, even if you see here, right, you see a snapshot date key – this is a different table. I looked at the contacts table, and even in here you will see all the information; you see address, PII is also there in this table.

**Bastien (21:15)** – Okay. But then I'm not really understanding what the document we are looking at is – the Super Gold or domains. It's not really referring to this table that you're mentioning right now, right?

**Deepti (21:51)** – Maybe because… wait, hold on.

**Deepti (21:57)** – Super Gold is all attributes, and if you want to look at the KPIs, you would go to the KPI table. This is where you'll have all the KPIs. So if you want to look at KPIs, you would refer to this; if you want to look at all attributes, you would refer to this.

**Bastien (22:09)** – Yes. And so where would the snapshots be then, just so I'm clear on how to use the document? I would think they would be in the attributes.

**Deepti (22:33)** – Good question. I have a feeling they just made an assumption that every table will have a snapshot, so they never put it here. I don't think you should worry about it. If you've asked that question, I'll answer it right there. But I am seeing that every table has snapshots, so you should be okay.

**Bastien (22:45)** – Okay. Okay, yeah, and you just showed it. Well, actually that's kind of a relief, because it means that we still get our trends. And from there, we can directly compute whatever time bracket we want using the snapshots, which would be pretty useful.

**Deepti (23:11)** – Yeah, I think snapshot was always part of the deal.

**Bastien** – Okay, great. Thank you. That was the top-priority question. And afterwards, we don't have to go through all of them because, as you said, we can always add them, and I'm sure it's something we can work on offline. But I was wondering how you store the computed KPIs, say a CLV for instance. Is this something that the US will compute on their end on the reporting side, depending on the granularity they choose, or is it stored in the tables as a value of CLV?

**Deepti (24:02)** – I don't think CLV was calculated and stored as part of the KPI list, because that's not something we got from the US team. But…

**Bastien (24:09)** – Yeah, I was thinking CLV, but CLV is computed on our end as well; maybe say AOV or any rate, for instance.

**Deepti (24:19)** – AOV should be there. AOV was made as part of the KPI list, from what I understand. Let me share my screen. It should be in the KPI catalog that I was talking about. So if you go here, you'll see Member AOV, right? It also gives the definition.

**Deepti (24:41)** – Yeah: average value per order placed by members during the selected period, right? This is your AOV, but you are saying your CLV is then calculated on top of your AOV. I don't think CLV was calculated for the US.

**Bastien (24:56)** – Okay.

**Deepti (25:05)** – Yeah, I don't see it as part of the… […]

**Deepti (25:34)** – Do you want to take a look at this definition? It's in the KPI catalog.

**Bastien (25:37)** – I wouldn't be able to challenge you right now, but yeah, exactly, I see it's CLV year one, year two, year three. This is just diving into the intricate definitions. I'll be OK with this.

**Deepti (25:56)** – So here, customer lifetime value is revenue per customer: AOV per year times average frequency per year times retention rate. This is a usual way of calculating CLV, right? I think that's how they're doing it.

**Bastien (26:01)** – Yeah, exactly. It sounds standard. Which makes me think that I need to… Oh yeah, okay, no, it's okay, I actually just got an answer. I'll look in more detail into the real differences between what we have identified so far and the KPI tabs, which I have to say I kind of skimmed over – specifically about the computed fields, to make sure they're here or not.

**Deepti (26:46)** – Yes, so your Super Gold is all attributes and your KPI catalog is all calculated values. So when you are referring, I would say check both to see if you have all your answers. And even after that, if you don't see something, you can add it here and we can talk about it.

**Bastien (26:50)** – Right. I'm asking because I saw in the BAR KPIs for customers that there were some buckets for AOV, like AOV last three months, this kind of thing, but then again in the Super Gold tab. So I'm guessing there are attributes for the bracket of the AOV, on which to do some groups for each customer. And I was wondering…

**Deepti (27:40)** – The BAR KPI – the reason why it's broken down into different tabs in the US is that there's a separate Power BI report called BAR, which is like a pseudo-CDP. They built a Power BI report where you can do your audience sizing. So it's another Power BI report. They gave us the KPIs separately just for that Power BI report, which is what was built like this. So you can refer to both of them, the KPI catalog and the BAR. Both of them were built out in the gold layer. It just has two different tabs because of how it's represented in the US Power BI.

**Bastien (28:23)** – Okay. No, it's very clear, actually, much clearer, because it got me to… Give me a few minutes today – give me the morning to go over all the questions again, see if I can find the answer myself or at least get the beginning of an answer.

**Deepti (29:04)** – No, no, take your time. No rush.

**Bastien** – Let's connect anytime. Actually, tomorrow is a bit short for me. […]

**Ajantha (29:16)** – Let's do this: I'll send a follow-up for this meeting, and from there we can define and see if we need any more questions or not.

**Bastien (29:33)** – Anyway, we're still waiting on a lot of KPIs from a few other use cases, so I'll be sure to have more follow-up questions afterwards.

**Deepti (29:34)** – Sounds good. Hello?

**Deepti (29:52)** – Andres, we're almost wrapping up, but one question came up, and I guess you're the right person to answer it. Brand MDM ID is not something that we have today in gold, right? That was one question that Canada has: will that be brought over? And how will they handle it wherever they use brand MDM ID today?

**Andres Gonzalez (30:19)** – So we are expecting to put the brand GDM ID and the brand customer ID into the loop. There was a dictionary that we created, so it is still in the gold layer, but we have not added that one because brand customer ID is the key of the entire data model. But we can offer that brand MDM ID if it's necessary. The thing is, a brand MDM ID and the brand customer ID have the same granularity. It's a one-to-one match, because the brand customer ID is generated based on the brand MDM ID. That's the reality today. So at the end, it's the same; it's just a different attribute name because of the nature of the tables. But we will be offering that attribute anyway.

**Bastien (31:08)** – Okay, and just to be clear and to understand how it works: the customer ID is the brand MDM ID that's being hashed, with like an MD5 or something?

**Andres (31:22)** – Yeah, it's an MD5 plus variables. So we put the brand code, source name, and some other things that are part of that, and we create the brand customer ID out of the brand MDM ID.

**Bastien (31:24)** – All right. So if we need the MDM ID – I think we need it, but I'll need to double check – we can just reverse-hash the customer ID and we should be good to go?

**Andres (31:45)** – That's the thing: we can still offer the brand MDM ID. If you need that one to be maintained, we can share it in the tables – right now the CDP is using it for some of the integrations we have – but we could incorporate it. That's part of the discussions we need to have. If you use that attribute and we need to make an aggregate over tables, it shouldn't be a problem. The overall process here is to identify what is missing from your end that you will require to make things work for you. Once we have that visibility, we evaluate and see where we need to add more attributes, where we need to add more things, and we make those decisions and we will be evolving the data model to the next phase of what you need for things to work.

**Bastien (32:37)** – Okay, perfect. I'm just asking because some of our exports or reporting rely on the MDM ID, so it was just to see if there was a way for us not to lose the key that we have. Or not, but we need to figure out whether it's a big deal to change it on our end as well. Okay, we can investigate that.

**Andres (33:01)** – Mm. I think we… What is important, besides the KPIs, is to discuss the other applications – the analytical use cases. I'm hearing that you are doing more than just reporting, and when that happens, we need to understand those things to make sure that you also understand the impacts on those layers, because now…

**Bastien (33:21)** – Yeah. Exactly.

**Andres (33:26)** – What you used to see in the CRM reporting today is going to disappear, and you will need to apply all your queries, all your logic, on top of the new tables of the new data model. That means you will need to transfer and transform all those components. While you do that transformation, if you can move to the brand customer ID, fine. If you need to keep using the brand MDM ID, again fine, we could expose it, but that will be required anyway. So you will need to do a refactor no matter what.

**Bastien (33:57)** – Yeah, that's actually what we're trying to figure out: whether everything we have today can be recomputed with Renovate, using all of the formulas we have, whatever aggregations and any kind of transformation we do – whether we can find everything through Renovate. So…

**Andres (34:10)** – Yeah. So that's a very important point, because transformation needs to happen earlier. If you are telling me that you are doing standardizations and transformations of attributes because those are not clean, I need all those rules to become part of the requirements, because that needs to happen in bronze. Once we move from bronze to silver, I'm going to do that transformation and avoid that. [Instead of] you having the data corrupted in gold, you should have the data standardized, so you should not be facing those problems anymore of transforming your data to be able to execute all your things. You should be getting clean data. That's also part of the premise: if you have a bunch of things that you are doing in that layer, you need to transfer those requirements to us.

**Bastien (34:19)** – Yeah, of course. Yeah. Right. Yeah.

**Andres (34:53)** – So then we can tell you exactly how the data will look. The data will look like you are asking us to make it look. So that's the premise.

**Bastien (35:03)** – All right. And about this: say we want to have some transformations on the data – not transformation, but more like data enrichment. Bad example, because apparently it's going to be available, but for PII, for instance, where we would normally be joining on the customer ID, or whichever ID, to some other tables we have containing PII or any kind of information – is this something we would be able to do on our end afterwards? Say, joining Renovate data with another table that just popped up, for instance. Or is this…

**Andres (35:44)** – Can you elaborate a bit more? Can you tell me your use case?

**Bastien (35:45)** – Yeah, sorry. I don't have any use case in mind, it's just that – I'm thinking out loud – if ever we want to enrich the data later, say a new data table drops with some specific, precise information, any other source which we need to integrate, for instance in reporting or dashboards, is this something that we would be able to do?

**Andres (36:06)** – Yeah, a new source, for example, of data that is coming in with new data.

**Bastien (36:18)** – Take the Renovate data and join it with this new source based on the ID, on any key. Is this something that we would be able to do and that could be considered, or would the new source have to be integrated into Renovate, in the gold layer?

**Andres (36:33)** – That's something that I would prefer to go into Renovate.

**Bastien (36:39)** – All right.

**Andres (36:39)** – Unless there is no need to bring it into Renovate – maybe if it's an external source that is really just for reporting purposes. But if you are moving PII and comparing across those two schemas using PII, you should not be getting the data outside of Renovate, in theory.

**Bastien (36:52)** – All right. Yeah, makes sense. PII was a bad example, but OK.

**Andres (36:59)** – So, that's the… Yeah, but if you get, I don't know, campaign data from a specific platform that is doing engagement, and you want to compare at campaign level – I know that happens – you could potentially do that join between the two schemas if you have data coming from the outside. And the CRM analytics schema that you have today, which is the schema you use for all the analytical use cases, will remain. The difference will be that we will be relying on this new gold layer that will be offering the new attributes, the new names and everything. You should be able to do that. I think when we arrive at that position, we need to discuss, because…

**Bastien (37:38)** – Uh-huh.

**Andres (37:42)** – The ideal scenario is that we put everything on top of Renovate, because the reporting layer will be on top of Renovate and governed by our team, the IT team, because we want to make sure that the new features that we are implementing, like metric views from Databricks…

**Bastien (37:48)** – All right. Okay.

**Andres (38:03)** – …and some other things that will become part of this semantic view of everything we do for KPIs, will be living within the code. It's not living outside, with notebooks that are run by users. If we have some things that are standardized, we want to make them part of the code of what DDX means for every single country in the Americas.

**Bastien (38:18)** – Yes.

**Andres (38:22)** – That's the big swap we are making there, because we really want to make this a standard. We don't want this to be a solution that every country has when it comes to measurement, because if not, it generates discrepancies, side discussions, back and forth with global teams. So we want to make sure that this stays under the governance of our side.

**Bastien (38:23)** – Right, makes sense. (38:37) Yes.

**Andres (38:44)** – Which doesn't mean that you cannot develop on top of that pipeline. If you have the skills and you know how to develop a KPI, you can become an extra developer on the pipeline and build your own KPIs within that pipeline. But you will need to become a developer within the IT organization, let's say, to put the…

**Bastien (38:47)** – Mm. (39:00) Within the framework, and…

**Andres (39:03)** – …to push the PR, do the pull requests, merge the code and do everything within the same landscape. We are not removing that, but there are certain skills that will be required to put the code in and merge it with low code at the end.

**Bastien (39:18)** – Okay. (39:21) Fair enough. And say – without going into the PRs and doing the work by hand myself – we want to add new KPIs, or again merge new sources, these kinds of things.

**Andres (39:31)** – Yeah.

**Bastien (39:40)** – Is this something that would be taken into account on your end, by IT, through your usual sprints and stories?

**Andres (39:46)** – Exactly, with the story points that we have with the board. We are trying to reorganize that team and make sure we have dedicated capacity for all of this. The goal is that you will have a dedicated story for reporting purposes, and that we have a dedicated data engineer who can do all these things and help you expedite things around reporting, because we know that those are important in the landscape of sharing insights and results with our brands and everyone in the loop. We can do all that integration through the consumer port, which is the one that we use today.

**Bastien (40:28)** – Perfect. Very clear. It was also one of the main questions for you. Well, then I think that's it from me. I've had an answer to most of my questions. So, Deepti and Ajantha, I will follow up on this with a recap of what we said and all the pending questions. I'll go through all the attributes and KPIs for which we have questions, and I'll let you know, and we can then answer these line by line, offline.

**Ajantha (40:59)** – Okay.

**Bastien (41:06)** – Too cool for this. [?]

**Deepti (41:07)** – I will also take back one question that you asked me about CLV, and I'll check and get back to you. I want to confirm that we actually have it in the tables.

**Bastien (41:12)** – Yeah. Okay, perfect. Okay.

**Ajantha (41:20)** – Okay, Bastien, do let me know when you want to have the next follow-up meeting. I can schedule one for us.

**Bastien (41:21)** – Sounds good. Yeah. (41:28) Okay, perfect. Let me check – let's schedule one maybe for next week at the same time. We'll share the agenda before, and if we don't have anything to say, then we can skip it.

**Deepti (41:43)** – Thank you.

**Andres (41:44)** – OK, next.

**Bastien (41:44)** – Perfect. Thank you all. Have a good day.

**Andres (41:46)** – In touch.

**Bastien (41:48)** – Goodbye.

*(Transcription stopped.)*
