---
title: Agents, Fragmentation, and a Conference Talk
layout: default
date: 2026-02-28
tags:
  - status
---
# {{ page.title }}


## Thoughts on being bottlenecked by implementation

While I don't think I've ever been dismissive of coding agents I think I may have just been underwhelmed. The potential has always been clear, even from the days of installing GitHub Copilot in VS Code, typing `def tic_tac_toe()`, waiting a bit and pressing tab when the completed function appeared. 

We've been on that paradigm for some years until the current Coding Agents really took off. It really feels like a fundamental paradigm shift during the later parts of 2025 and people are just now waking up to the realization here in early 2026.

I have been thinking about the implications from the perspectives of a machine learning researcher. A  common recipe in the old (pre-LLM) era of doing ML research was to,
1. Find an interesting paper within the problem space of your interest
2. Cross your fingers that they attached a GitHub repo
	1. The exclusivity of this feature gave rise to sites such as paperswithcode.com. I think it's important to reflect on that.
3. Hope that the code is of decent quality and that you will be able to somewhat reproduce the results.

Now with Coding Agents such as Claude Code we can *sample* a repository seemingly out of thin air. Importantly, this of course also goes for ideas that are not yet put onto paper. Rate of experimentation iteration is going to be absolutely crazy. The speed of large class of ML research projects are no longer bottlenecked by a PhD student's coding abilities or PyTorch knowhow nearly as much as it was before. Small, isolated experiments are suddenly insanely cheap.

Being an inexperienced researcher I don't see the landscape of opportunities that this brings very clearly. However, I have a feeling that this presents a fundamental shift in how ML research is being done. Probably also [research in general](https://www.popularbydesign.org/p/academics-need-to-wake-up-on-ai).

## Presenting at [IDA Driving AI](https://ida.dk/driving-ai)
I'll be giving a talk titled "*Smaller and Faster AI: A Primer in Model Compression*" at IDAs Driving AI conference that's taking place on may 27th. 

Here's the abstract I sent in:
> As AI models grow in size and complexity their hardware requirements increase accordingly. State of the Art models from frontier labs require enormous data centers and dubious (at best) data collection strategies. However, there is a parallel track that often gets overlooked. As the AI capability ceiling is raised, the floor rises with it. This means that the baseline performance for smaller models has seen rapid growth, enabling otherwise infeasible use-cases such as local, offline AI on mobile devices. 
> 
> One research area dedicated to producing smaller and more efficient models is model compression: The act of starting with a larger and highly capable model and using that to produce a smaller model with similar capabilities. Model compression techniques such as quantization, pruning and knowledge distillation have become essential to applying AI models. This presentation explains core concepts of model compression and showcase that they are necessary and important for the AI adoption we are currently seeing.

## Papers I've especially liked

I have been trying to make it a habit that when I read a paper that I especially like I'll post it on Bluesky. The response has been very nice and has led to a deeper level of engagement. 
### [Layer pruning in LLMs](https://openreview.net/pdf/72eeca23221e8c89efea8668851038632d42559d.pdf), [post](https://bsky.app/profile/rasgaard.com/post/3mexzopccf22f)
Due to residual structures in Transformer-models it's possible that many layers contribute very little to the downstream performance of the network, allowing for removal those redundant layers with little impact.
### [Performance Per Watt](https://arxiv.org/pdf/2511.07885), [post](https://bsky.app/profile/rasgaard.com/post/3mfbvj34qws25)
LLM cloud inference dominates usage, but should it? Local models and accelerators have improved massively over recent years. Perfect routing to best local model "reduce energy consumption by 80.4%, compute by 77.3%, and cost by 73.8% versus cloud-only deployment"
## Local AI deployment ecosystem fragmentation

This is from a discussion on the Danish Data Science Community [Slack](https://danskdatascie-o8m9638.slack.com/) where I posted the following:

Stumbled upon this post asking "[Where are the local AI apps? Millions build AI apps with natural language, but local AI deployment remains impossibly complex. Why?](https://inference.plus/p/where-are-the-local-ai-apps)". I found it super interesting and wanted to share.

I have been spending the better part of the past half year starting off my PhD in edge deployment and model compression by getting familiar with the landscape of edge/on-device deployment. It has sometimes left me with a slight feeling of helplessness. When deploying models to local hardware you're at the mercy of developers of hardware SDKs, toolkits, libraries etc. and everyone is building their own solution to their own unique setting. That comes with varying levels of compatibility, support and so on. The figure from the post illustrates this really well. It is extremely hard to even get an overview of all the options.

My hope is that posts like this help shed light on those challenges. It even suggests a solution that I'm increasingly convinced is a valid direction: Coding agents to bridge the gaps left by fragmentation. A lot of the challenge is being overwhelmed by documentation, tooling, incompatibilities. Problem-solving stamina is one way to describe it.


Even if coding agents like Claude Code don't have the necessary knowledge upfront to solve a lot of these problems it certainly has the stamina. And it can document "happy path"-patterns it has found through rigorous problem solving in Agent Skills for future use.

I'm starting to be optimistic about this framing!

> "from what you describe it sounds more like what is needed are standards rather than an AI agent - but maybe I am reading it wrong" - Kenneth Enevoldsen

> "Interesting blog post
> 
> Overall I think it is quite an old problem, afaik even simple app development is quite hard for smartphones (different versions of OS, hardware etc), I think making local models work is definitely an even bigger challenge  
> 
> It would be nice, if for example we have some open  "local deployment" model, maybe trained on different hardware/OS versions to deal with certain issues. I wonder if something like a "phone chip simulator" exist to create RL environments for different phones" - Vladimir Salnikov

Their [posts](https://inference.plus/p/how-are-we-going-to-get-intelligence) generally shares this sentiment of the need for standards and how we've seen it before in the history of computing: "_This echoes the early days of computing when architectural incompatibility was the norm. IBM System/360 code (1964) wouldn't boot on a DEC PDP-11 (1970), and today an ANE binary won't magically light up on a rival NPU. IBM System/360 code wouldn’t boot on a DEC PDP-11, and today an ANE binary won’t magically light up on a rival NPU. Different decade, same fragmentation - just with tensors instead of punched cards._"
## Transcription tool using Transformers.js
I wanted to experiment with Coding Agents and building web applications with Transformers.js. I shared [the result](https://rasgaard.com/webai-stuff/transcribe/) on the Danish Data Science Community [Slack](https://danskdatascie-o8m9638.slack.com/) and didn't think much of it. A few minutes went by and my LinkedIn notifications went off. Turns out the former chairman, [Kasper Junge ](https://kasperjunge.com/) [posted about the project](https://www.linkedin.com/feed/update/urn:li:activity:7426905667011051520/).

What I liked the most about spreading the word around this project were the two comments reacting to the simplicity of using Transformers.js

> "øhhh kører det hele i de to js filer? 😅" - Mike Riess

and 

> "Jeg forstår det simpelthen ikke 🙂 Kører den selve modellen som javascript i klientens browser? Det lyder helt crazy? Er det så ren CPU?" - Jonas Akrough Larsen