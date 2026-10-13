---
title: Whisper encoder layer pruning
layout: default
date: 2026-06-30
status: finished
summary: "Removing encoder layers from Whisper-large-v3-turbo with label-free recovery — the \"Six Layers Less\" paper."
---

# {{ page.title }}

## Goal

Find out how far speech recognition can be compressed by removing *entire encoder layers* — and whether the lost performance can be recovered without any labeled data.

## Report 

Some deliberately random experimentation paid off early: it turned out **any single layer** of the `Whisper-large-v3-turbo` encoder could be removed with barely any degradation. That raised the real question — *how far can this go?*

Two analyses carried the project:

- **Layer similarity** — the signal traversing the encoder stack stays highly similar throughout, except at a few places where a significant change occurs. Those change points mark layers worth keeping.
- **Leave-one-layer-out ranking** — borrowing a recent result from LLM pruning literature, downstream performance with each layer removed gives a principled measure of "removability".

The first public outing was a poster at the low-stakes Green AI workshop in Copenhagen ([slides](https://docs.google.com/presentation/d/1KWO1v-RkOvF8sLPbcDzun7w7MnwQ2M74b8VQh_qcQcE/edit?usp=sharing)). Nobody tore the idea apart, so it got written up as a 4-page extended abstract — ***Six Layers Less: Encoder Pruning for Whisper with Label-Free Recovery*** — accepted to the [GLOW workshop at IJCAI 2026](https://glow-ijcai-2026.github.io/glow-ijcai-2026/) and presented as a poster in Bremen.


![Poster of the paper "Six Layers Less: Encoder Pruning for Whisper with Label-Free Recovery"](/assets/attachments/whisper-encoder-pruning/image.png)
