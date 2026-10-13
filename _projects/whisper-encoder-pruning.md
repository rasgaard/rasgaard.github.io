---
title: Whisper encoder layer pruning
layout: default
date: 2026-06-30
status: finished
summary: Cutting whole layers out of a top speech recognition model, then getting the performance back without labeled data.
---

# {{ page.title }}

## Goal

Speech recognition keeps getting bigger, which keeps it off the small devices where it would matter most. The bet behind this project: most of a model's layers are passengers, and cutting them out is the fastest route to capable transcription that runs anywhere.

## Report

Deliberately random experiments paid off first: it turned out **any single layer** of the Whisper-large-v3-turbo encoder could be removed with barely any degradation, which raised the real question of how far that goes. Two analyses answered it. **Layer similarity** showed the signal barely changes through most of the encoder stack. **Leave-one-layer-out testing** gave a principled ranking of what can go.

The first outing was a poster at the friendly Green AI workshop in Copenhagen ([slides](https://docs.google.com/presentation/d/1KWO1v-RkOvF8sLPbcDzun7w7MnwQ2M74b8VQh_qcQcE/edit?usp=sharing)). Encouraged rather than torn apart, it became a four-page paper, ***[Six Layers Less: Encoder Pruning for Whisper with Label-Free Recovery](https://arxiv.org/abs/2609.27980)***, accepted to the GLOW workshop at IJCAI 2026 and presented in Bremen.

![Poster of the paper "Six Layers Less: Encoder Pruning for Whisper with Label-Free Recovery"](/assets/attachments/whisper-encoder-pruning/image.png)
