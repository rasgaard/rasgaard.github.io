---
title: Retreats, Meetups, and Beyond the Academic Game
layout: default
date: 2026-03-31
tags:
  - status
---
# {{ page.title }}

## Seminars, team days and retreats
This month was a bit special. I had four different two-day events in my calendar, meaning that about two weeks' time was pre-allocated. 
### Laerdal AI Services days
*3rd/4th*

These team days are usually done every half year or so. One of the primary outcomes is just getting to see and physically spend some time our colleagues from the office in Stavanger. The topic for these days were pretty loosely defined. We were asked to bring something that we would like to spend time exploring and teams were formed based on that. I brought OpenClaw as something to play with and was joined by two colleagues. Other teams were looking into Claude Code and Azure Agents SDKs.

From what I had gathered from all the hype leading to increased sale of Mac Minis I thought that OpenClaw was a plug-and-play service. I was disappointed to say the least. My expectation quickly fell apart when I encountered broken menus, complicated setup processes and confusing documentation. 

I kept on asking myself whether all of these non-technical people yapping about OpenClaw on LinkedIn has actually tried it or if they just bought into the idea of it. Based on my experiences during these days I'm suspecting it's the latter. 

### DTU Compute PhD Kick-off Seminar
*5th/6th*

This was the first off-site seminar of the month. The purpose was to introduce new PhD students at DTU Compute both to each other but also to common concerns and thoughts about doing a PhD in general. I quickly felt that the content would be more relevant if I had *just* started on the PhD rather than being 6 months in. A lot of the fellow PhD students were just starting out and the content was definitely tailored towards those. That being said it was still really good. 

Some of the preparation for the kick-off included watching a TED talk by Uri Alon titled "[Why science demands a leap into the unknown](https://www.ted.com/talks/uri_alon_why_science_demands_a_leap_into_the_unknown)". His description of "being in the cloud" when things seem uncertain really stuck with me. We should celebrate being in these uncertain states as they indicate that we are in unknown - and often highly interesting! - territory. But that can also feel deeply uncomfortable. A thing I have gathered from discussions during this first half year of the PhD is that being able to *thrive* in this intuitively uncomfortable situation is a key part of doing well - both in terms of personal well-being but also research output.

### Industrial PhD Course
*24th/25th*

As part of being funded by the Innovation Fund Denmark's Industrial Researcher programme it is mandatory to participate in this course. It's spread over the first half year or so and goes over a lot about expectations, stakeholder management, value creation and many more topics. It gathers the entire cohort of industrial PhD from the given round of funding, resulting in about 50 industrial PhD students with a huge variety in projects.

This seminar was the last mandatory gathering of the course. It took place in Middelfart (at Severin Kursuscenter). The overall contents of the two days were fine. Nothing groundbreaking but it was nice to get together with the group again to compare our individual experiences of starting up a PhD. 

Part of this seminar was an elective workshop on *research-based value creation*. It turned out to be even more stakeholder mapping which got a bit daunting, but we also had to think about the different kinds of value that our project brings. Not just economic value for the business, also personal happiness and joy, community building, accessibility of knowledge. There are lots of different ways of finding value in the project. The presenter (from [Kitchen](https://kitchen.au.dk/), Aarhus University) mentioned an example wherein he had made a more accessible version of his academic work which had ended up creating a lot more value than the academic work alone. 

### DTU Compute, Cognitive Systems Spring retreat
*26th/27th*

The final stay was most definitely the nicest at Marienlyst Strandhotel. A bit more luxurious than the bunk beds at Hillerød Hostel during the DTU Compute PhD seminar. The topic of the retreat was AIs impact on research - a topic that I have thought about quite a lot since trying to use Claude Code as a research assistant, inspired by Karpathy's [autoresearch framework](https://github.com/karpathy/autoresearch). 

We split into groups and worked on a Hackathon case that explained the problem of students not knowing who works on what. The process of starting a project such as the bachelor's and master's thesis is currently very informal. Students often just email potential supervisors until something works out. This is not a very sustainable way of going about it as some supervisors are naturally more exposed to students than others due to having popular courses etc. That leads to few supervisors having a lot of students *along with their large courses*.

A few data sources were presented, DTU Orbit, Findit, etc. where we could scrape information about recent publications and research interests. This proved to be the hardest part of the exercise. It must have looked like a DDoS attack from Helsingør from the perspective of the DTU Library. The services were not responding soon after we got going.

After having scraped *some* data - with the help of Claude Code, of course. I don't think I wrote a single line of code during the retreat - I started another instance that would create a recommendation system based on the data files. Nothing too groundbreaking but it was nice to see that you're able to produce some fairly complete experiences in a matter of hours, given that you have the data foundation in place.

## Talk at ITU from Marian Tietz, Head of Open Source at 🤗 Hugging Face
I was tipped about a lunch talk at the IT University in Copenhagen by Marian Tietz, head of open source at Hugging Face. Naturally I immediately booked my calendar and headed there. Turns out there's a group at ITU that arranges these kinds of talks on a regular basis. 

The talk was about [LoRA ]([https://huggingface.co/docs/diffusers/training/lora](https://huggingface.co/docs/peft/package_reference/lora))and other related parameter efficient fine-tuning (PEFT) methods. It was nice to be at such a specialized presentation and not just yet another perspective on how AI agents is going to change everything. 


## On-device AI Meetup
Once a month I gather the company and university supervisor for a status update. For february I shared that I had created a [transcription application](https://rasgaard.com/webai-stuff/transcribe/) using Claude Code and Transformers.js - just to experiment with how well Claude Code could be used to make apps with that library. I shared this on the Danish Data Science Community's "share-your-work" Slack channel. It was quickly picked up by Kasper Junge who shared it on his LinkedIn. 

Some of the reactions in the comments expressed confusion about the simplicity of the code: "Is it really only those three files to run this entire thing?", for example. This made me think that I was perhaps sitting on some knowledge that was worth sharing more broadly. My company supervisor then encouraged me to organize a meetup for people interested in on-device AI. I didn't really know what to expect but we ended up with a full (30 people) list of attendees and about 30 people on the waiting list as well. 

I was also lucky be in contact with a local Copenhagen-based startup, [NobodyWho ](https://nobodywho.ooo/), that develops a library to run LLMs locally and efficiently on any device. When I asked if they would be interested in presenting during the meetup I was met with lots of enthusiasm. Thanks for that :)

## Thoughts about "Don't play the game" - A. Karpathy
Once in a while I re-read some "advice posts" (I have collected them [here](https://rasgaard.com/phd/)). One of my favorites is Andrej Karpaty's [A Survival Guide to a PhD](https://karpathy.github.io/2016/09/07/phd/). It's almost like I discover a new section that applies to my current situation each time I read it.

He has the following section which I have thought a lot about since:
> **Don’t play the game**. Finally, I’d like to challenge you to think of a PhD as more than just a sequence of papers. You’re not a paper writer. ***You’re a member of a research community*** and your goal is to push the field forward. Papers are one common way of doing that but I would encourage you to ***look beyond the established academic game***. Think for yourself and from first principles. Do things others don’t do but should. Step off the treadmill that has been put before you.

A lot of the activities during this month hasn't been directly tied to any traditional research-output. However, recontextualizing it in a way that *looks beyond the academic game* brings a sense calmness to me. 

For example, the meetup took some time to organize and hasn't resulted resulted in any progress on my academic work but I met up with interesting people and meaningfully expanded my network of people interested in on-device AI. Also, I imagine that some of the attendees now know me as "*that guy who organized the on-device AI meetup*", which I think is valuable in itself (see *[The person who did X](https://karpathy.github.io/2016/09/07/phd/)*).
