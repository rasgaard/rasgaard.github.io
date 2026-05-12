---
title: Hosting Meetups, Building Prototypes and Summer Plans in Vienna
layout: default
date: 2026-04-30
tags:
  - status
---
# {{ page.title }}

## On-device AI meetup

I had the great pleasure of hosting a meetup around _On-device AI_. As it was my first time doing something like this I didn't really know what to expect. My company supervisor put me at ease by saying something like "If you can gather 5 people who are interested in the topic then that's a meetup." and that felt very manageable.

We ended up being around 30 people on the attendance list and another 30 on the waiting list. With a little bit of no-show I think we were about 25 people in the meeting room. During the day I was mostly concerned with the attendees finding out where to go as the office space can be a bit difficult to figure out. Luckily I have some fantastic colleagues who helped get everyone herded up with the elevator one or two at a time to get to the meeting room where the meetup would take place.

I'm not so sure that my presentation was really all that good or memorable but perhaps that doesn't matter that much. I have been to plenty of meetups where the presentations were probably the least interesting part of attending. It's more about gathering people with similar interests in a room and feeling that interest and motivation to go in a certain direction. 

I was super pleased with how it turned out when thinking about it. I did not expect people asking straight away about when the next meetup would be. Having Asbjørn present their work at NobodyWho was great. Seeing the people behind such a project can really change your perception of it. I went from initially thinking "Ah, that's just a Llama.cpp wrapper" to "These guys seem to _really_ care about what they're building, how it's done and are obviously _very_ talented at what they're doing".

We ended up having beers at Bootleggers which is always a fantastic way to end. I had some great discussions with some of the attendees and learned a thing or two. 


## Rapid prototyping of offline AI applications for Laerdal

There has been kind of a nagging feeling that I haven't been doing a lot of explorative work in terms of what on-device AI could look like for products in Laerdal. My company supervisor and I sat down and identified a few areas that would be nice to address. Simply put, I needed to build out a few demos that could show some functionality that certain teams would find interesting.

Through some heavy use of Claude Code I put together two demos, showcasing offline AI through the browser using Transformers.js. I was very pleasantly surprised with how well it turned out.

#### Simulating conversations with emergency dispatcher

Laerdal has a product called _Revivr_ that's being developed in collaboration with the British Hearth Foundation (BHF). It's purpose is to train the general public to be better equipped for calling emergency dispatchers by providing it as a simulated experience.

You can try it on BHFs website [here](https://www.bhf.org.uk/how-you-can-help/how-to-save-a-life/how-to-do-cpr/learn-cpr-in-15-minutes). It was mentioned on stage by [Satya Nedella at Microsoft's AI Tour in London](https://www.youtube.com/watch?v=kOkDTvsUuWA&t=1949s) about a year ago. 

Anyway, I wanted to see if you could replicate that experience with local AI. I knew of [similar applications developed](https://www.linkedin.com/posts/xenova_new-real-time-conversational-ai-models-can-ugcPost-7336107895983341569-rYCv?utm_source=share&utm_medium=member_desktop&rcm=ACoAABSldDUBzdKI0ia86yJIa5yQU94LKYCbuVk) by the lead developer of Transformers.js (Xenova aka Joshua Lochner) and wondered if I could just point Claude Code in the direction of that repository and have it create a slightly different framing around the voice to voice interface. 

Turns out that was very much possible. Within a few days I had working prototype where I could even select between different models to see how well smaller models could carry out the role and conversation.  

#### Medical advice generation grounded in official documents

One of the "AI-first" products in development in Laerdal is using language, video and audio understanding to assist emergency call dispatchers to give proper advice during medical emergency calls. It was covered here by the [Norwegian National Broadcasting](https://www.nrk.no/rogaland/laerdal-medical_-uis-og-amk-sentraler-utvikler-ny-ki-losning-for-113-som-skal-redde-flere-liv-1.17773176). It's a system that both listens in and watches the camera feed of a caller and provides the dispatcher with relevant advice for the situation. This advice is based on a comprehensive document called [_Norsk Indeks for Medisinsk Nødhjelp_](https://www.helsedirektoratet.no/veiledere/norsk-indeks-for-medisinsk-nodhjelp/Norsk%20indeks%20for%20medisinsk%20n%C3%B8dhjelp.pdf/_/attachment/inline/c9aa280e-3e84-4197-8743-36f5dd934b8b:98f620f9fde60a4ecd28c362f13f06812839ba6d/NIMN_2024_versjon_5_0.pdf) (_Norwegian Index for Medical Emergency Relief_). This document has been parsed so that it's better suited for retrieval systems. 

I wanted to see if I could make a small emergency advice application that you could use offline. We imagined that it could be used as part of a first-aid kit where you would find it on a dedicated device as it doesn't depend on internet access or any external services.

This, also, worked really well. Knowing of demos related to [in-browser Postgres databases](https://github.com/huggingface/transformers.js-examples/tree/main/pglite-semantic-search) I just needed some pretty rudimentary LLM integration to get it to work with a full RAG pipeline. Again, I used Claude Code for the entirety of the application building process and had a working "demoable" application very quickly. It even helped me evaluate the retrieval as the initial version gave terrible advice. I simply copied the inputs/outputs and asked what could have gone wrong. I ended up with a solution where it rephrased the question into something that would be more similar to the documents as I relied on a smaller embedding model that performs really well on semantic sentence similarity. 

## Summer school in Vienna

I signed up for [_The European Summer School on Artificial Intelligence_](https://essai2026.eu/) which takes place in Vienna, Austria 6-10 July. 

This is my first summer school attendance outside of Denmark which is super exciting. If I recall correctly there should be something like 400 participants, so quite a big one. 

I'm mostly excited to go traveling a bit as I haven't done that all that much. It'll be nice to further "demystify" that and figure out that it isn't complicated, probably just a bit cumbersome at certain points in time. 

The courses during the summer school looks very good. Especially the one that's most relevant to my project: [The Art of Compressing LLMs: Pruning, Distillation, and Quantization Demystified](https://essai2026.eu/program.php#id-C6). But I also look very much forward to other courses such as [Foundations of Concept-Based Interpretable Deep Learning](https://essai2026.eu/program.php#id-C13) .

## Invitation to Green AI workshop

After having tried to involve myself in the local research community I was very pleased to see an invitation to a _[workshop on Green AI](https://www.aicentre.dk/events/20260508-p1-programs-workshop-green-ai)_ arrive in my inbox. This gave me the opportunity to bring some of my in-progress work and hear what other people think of it.

I ended up making a [poster](https://docs.google.com/presentation/d/1KWO1v-RkOvF8sLPbcDzun7w7MnwQ2M74b8VQh_qcQcE/edit?usp=sharing) about pruning the layers in the Whisper encoder. It felt like a low-stakes environment so I didn't spend all that long on it but probably longer than I initially expected to spend. 

## Courses and assignments

I have had to spent quite a bit of time on several mandatory course-related activities this month. The Industrial PhD Course from Innovation Fund Denmark had to be finished up by writing an 8-10 page assignment documenting my learnings and reflections from the course. 

The Sustainability Evaluation and Communications course also required some work before the course even started. I could have chosen to put this sustainability course at any other time during my studies but I'm pretty satisfied that it's (mostly) over and done with now. 

I could go on quite the rant about the irrelevance of the sustainability-part of the course but I'd rather not have it in writing so I can make sure that it fades from memory with time. It was probably the meanest I have ever been in a course evaluation and part of me regrets it a tiny bit but then again, just make a better course. Please.

After completing this round of courses, seminars and workshops I will have accumulated 12.5 ECTS out of the 30±2.5 ECTS. I'm pretty sure that I only have the mandatory _Supervision and Facilitation of Learning_ course left.