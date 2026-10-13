---
title: In-browser offline transcription
layout: default
date: 2026-03-31
status: finished
summary: A Transformers.js web app that transcribes fully on-device, built with Claude Code, which went small-time viral.
---

# {{ page.title }}

## Goal

Test how far coding agents and [Transformers.js](https://huggingface.co/docs/transformers.js) go for building *real* on-device AI applications. Starting with the most obvious one: speech-to-text with no server involved.

## Report

Pointed Claude Code at the Transformers.js examples and had a working transcription web app within a day. Shared it on the Danish Data Science Slack thinking little of it. Minutes later LinkedIn notifications went off, after former chairman Kasper Junge posted about it. The best reactions were sheer disbelief at the simplicity: *"Kører den selve modellen som javascript i klientens browser?"* (It runs the model as JavaScript in the client's browser?!)

The interest had a concrete side effect: my company supervisor suggested organizing a meetup, which became the first **On-device AI CPH Meetup**: 30 attendees plus a 30-person waitlist, with [NobodyWho](https://nobodywho.ooo/) presenting their local-LLM runtime.

- Live demo: [rasgaard.com/webai-stuff/transcribe/](https://rasgaard.com/webai-stuff/transcribe/)
- Background: [Getting Started with Transformers.js](/blog/getting-started-transformerjs/), [Prompting Whisper](/blog/whisper-prompt-js/), [Whisper-tiny for Danish](/blog/whisper-tiny-danish/)
