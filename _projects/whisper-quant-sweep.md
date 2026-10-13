---
title: Whisper quantization sweep
layout: default
date: 2025-11-30
status: dropped
summary: "The obvious first try at shrinking speech recognition: smaller numbers, sparser weights. It mostly failed, instructively."
---

# {{ page.title }}

## Goal

Before cutting layers, try the obvious: shrink the model's numbers and zero out half its weights, then chart what survives. If the cheap tricks worked, nothing fancier would be needed.

## Report

Shrinking the numbers was essentially free: same accuracy at half the size. Zeroing half the weights was a disaster at 101% error, and retraining only partly resurrected it to around 18% against a 4% baseline:

| Setup | Size | Error rate |
| ----- | ---- | ---------- |
| Baseline | 1074 MB | **4.27%** |
| Smaller numbers | 578 MB | **4.24%** |
| Half weights zeroed | 1074 MB | **101.20%** |
| … plus retraining | 1074 MB | **17.63%** |

Getting started took generous help from a maintainer of the compression toolkit, via the GPU MODE Discord community.

**Why it is here:** dead ends are findings too. This one cleared the way for layer pruning, which worked far better, and it stays visible so nobody (including future me) repeats it.
