---
title: Weird workshop experience and slight pivot
layout: default
date: 2026-08-31
tags:
  - status
---
# {{ page.title }}

## DDSA Pre-Graduate retreat

Back when I had just graduated I participated in the Danish Data Science Academy's Pre-Graduate retreat. It's a two-day retreat at Rødding Højskole where the focus is on getting clarity on whether or not a PhD in AI/ML/data science is something that you, as a soon-to-be graduate, might want to consider pursuing. I had a really good time as an attendee and it definitely helped me in my considerations.

Fast forward to this year's retreat planning and I was asked by one of the organizers if I wanted to be a guest speaker at a panel discussion. I immediately said yes without much consideration. I recognized it as getting a chance to reflect on my own decisions and crossroads during the past few years. And the retreat itself has a very nice, cozy and relaxed atmosphere to it. 

It was a pleasure to participate and I just hope that some of what I said moved the needle a tiny bit for at least some of the attendees. 

## IJCAI Workshop
My work on compressing the Whisper encoder through layer pruning had been accepted to the Generalizing from Limited Resources in the Open World (GLOW) workshop at the International Joint Conference on Artificial Intelligence. That meant I had to prepare a poster and present it in Bremen, Germany. I'll go ahead and give an account of my honest experience. It unfortunately wasn't all that good.

### Transportation
I decided on taking the Flixbus to Bremen. It was cheap and direct from Copenhagen. The only downside was the duration of the travel, which was about 8 hours. However, I thought that was manageable. The workshop was on a Saturday and so I booked the tickets for arrival Friday evening to stay at a hotel for a night. 

Going by the (unfilled at the time) schedule table on the workshop website the workshop were to start at 9 and conclude at about 12. Seeing that made me think that traveling for 16 hours for a 3 hour workshop was a bit silly but I went ahead anyway. On my way in the bus on the way to Bremen I decided to check out the schedule once again. Something might have changed or have been updated. Turns out the entire schedule had been updated *and* prolonged, meaning I had to reschedule my bus tickets. The initial price was about 600 DKK and the rescheduling was about 400 DKK. Also, the only tickets available that made sense had me arrive in CPH at 4 AM.

### Workshop
It wasn't all bad though. Since the schedule had been updated with the actual speakers and titles for talks I had something to look forward to. Some of the talks looked really interesting and relevant for my project. Super nice! It might be worth the hassle then, I thought.

I arrived about 5 minutes past 9 so the first talk had already started. Walking into the classroom where the workshop was held I was initially not sure if I was in the right room - and the speaker was with us online, not in person. I couldn't connect the content on the screen to the title on the schedule in a meaningful way. Turns out it was the right room though.

Not having been at many conference workshops I thought it was a little odd that the presenter wasn't physically there with us. The next speaker was there and I thought that maybe the first one was just an anomaly. But as it turns out, the in-person speaker was the anomaly. It was the only in-person speaker out of the nine talks. There was even a pre-recorded speaker which prompted a conference organizer to pull aside one of the workshop organizers to tell them that it wasn't allowed to have pre-recorded talks. Pretty awkward.

The whole atmosphere was fairly awkward during the entire workshop. No clapping, no talking, no discussions in breaks, people were not really asking questions (which I guess is more fair when the speaker is online). 

At this point I was ready to just present my poster for half an hour and go home which is exactly what happened. I can now say that I have a fairly good idea of what a conference workshop *shouldn't* be like and I guess that's also valuable. I met with one of my supervisors collaborators who had also had a paper accepted and we talked about the experience during the day and validated each other's thoughts about it. That was a nice way to end it off.

## Pivot to Local LLMs for Agentic Software Engineering

Something interesting has happened at Laerdal Copehagen, which I suspect is happening at a global scale for every organization that ships software: Everyone is suddenly using coding agents (Claude Code, specifically). It has rapidly changed the job of most software engineers and is challenging aspects on cost, productivity, meaningful work and a lot more. 

Due to cost management and resilience I was invited to a few meeting regarding questions on local models with coding capabilities. I had seen blog posts saying that Qwen3.8 27B runs reasonably well on GPUs with 24GB of VRAM so that's what I said in those meetings. 

It's of course exciting to work on but it's also a bit different from the original scope of the overall PhD project. Not that it's a problem. I see it as the most direct and easy way to undoubtably have made a difference in product development, cost saving, resilience and privacy. Those markers are the same whether it's a transcription service running locally on a phone for a product or a coding agent running on-prem in the office.  
### D3A Poster

Seeing my latest pivot I wanted to set a sort of deadlien to have some preliminary work done. [D3A](https://d3aconference.dk/) is coming up so I submitted a poster proposal with the title "*Compressing Local Coding Agents: Directions and Open Questions*". I hope it'll get some attention and in the ideal scenario lead to collaborations.
