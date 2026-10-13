---
title: Compressing local coding agents
layout: default
date: 2026-09-30
status: ongoing
summary: "How much coding-agent capability fits on-prem for cost, resilience, and privacy?"
---

# {{ page.title }}

## Goal

Figure out how much coding-agent capability fits on local hardware, so the company can host agents on-prem for **cost, resilience, and privacy** instead of renting them by the token.

## Report

The setup so far: a workstation with an Nvidia RTX Pro 4000 (24GB VRAM) on order, and Qwen-class ~27B models as the starting point, the size rumored to run reasonably in 24GB. Floating the idea at the AI Tinkerers demo night drew immediate enthusiasm, a good sign we're not alone in wanting this.

The framing goes back further: local deployment tooling is deeply fragmented (every hardware vendor's SDK, every toolkit's quirks), and agents are interesting precisely because they have the *problem-solving stamina* to bridge those gaps where humans burn out. Enough material has spun out of this already for a poster proposal to [D3A](https://d3aconference.dk/): *Compressing Local Coding Agents: Directions and Open Questions*.


![Poster of the project "Compressing Local Coding Agents. Directions and Open Questions"](/assets/attachments/local-coding-agents/image.png)
