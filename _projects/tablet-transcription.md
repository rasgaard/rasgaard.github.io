---
title: On-device transcription for product
layout: default
date: 2026-06-30
status: ongoing
summary: Drop-in whisper-base replacement for cloud transcription in a product demo, tested on Android tablets.
---

# {{ page.title }}

## Goal

Replace a costly cloud transcription service with on-device inference in a real product context, keeping the value-add while killing the per-use cost.

## Report

The opening came from the product side: one product is at a scale where centralized cloud transcription costs more than the value it adds, yet the feature itself is genuinely wanted. The product owner had a standalone Lovable-built demo to experiment on. Downloading it and instructing Claude Code to wire in `whisper-base` via Transformers.js worked seamlessly, including on the Android tablets used for product testing.

Working prototype: yes. Product decision: still pending.
