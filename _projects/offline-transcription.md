---
title: In-browser offline transcription
layout: default
date: 2026-03-31
status: finished
summary: Open a web page, get transcription, nothing ever leaves your device. Built in days, shared widely.
---

# {{ page.title }}

## Goal

Prove that useful AI can live entirely inside a web page: open a URL, speak, get text back, with no server involved. Privacy by architecture instead of by promise, and a per-use cost of exactly zero.

## Report

Pointed a coding agent at Transformers.js and had a working app within days. Shared it on the Danish Data Science Slack thinking little of it, and watched it take off on LinkedIn instead. The best reactions were pure disbelief that the model runs as JavaScript in the visitor's own browser.

The interest had a concrete side effect: it became the excuse to organize the first **On-device AI CPH Meetup**, with 30 attendees, a 30-person waitlist, and the team behind the NobodyWho local-AI runtime presenting.

- Live demo: [rasgaard.com/webai-stuff/transcribe/](https://rasgaard.com/webai-stuff/transcribe/)
- Background: [Getting Started with Transformers.js](/blog/getting-started-transformerjs/), [Prompting Whisper](/blog/whisper-prompt-js/), [Whisper-tiny for Danish](/blog/whisper-tiny-danish/)
