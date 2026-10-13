---
title: 'MSc thesis: factual certainty in NLP'
layout: default
date: 2023-07-16
status: finished
summary: Can a language model point to where it learned a fact? Tested a popular explainability method and found where it breaks — and where it helps spot misinformation.
---

# {{ page.title }}

## Goal

Language models sometimes state falsehoods with total confidence — so-called hallucinations. Part of the problem is that a model's view of the world is just its training data, which inevitably contains conflicting information. If we could trace a prediction back to the training examples that taught it, we could clean datasets and make models more trustworthy.

This was my MSc thesis in Human-Centered AI at DTU Compute (Jan–Jul 2023, defended Aug 1st 2023): *Towards factual certainty in Natural Language Processing using explainability methods*. It explores Training Data Attribution — specifically TracIn — on a fact-tracing benchmark called FTRACE-TREx.

## Report

Trained T5-small on 1.5M fact abstracts and scored candidate training sets with TracIn (cosine similarity over checkpoints) for 1,000 novel facts. Three takeaways:

**1. TracIn is fragile to tiny target changes.** A ground-truth proponent like "Gone Bald is a noise rock band from Amsterdam, [The Netherlands]" scored -1.94 for the query "Amsterdam is the capital of [Netherlands]" — matching the targets either way flipped it to ~+2. Adding a single period to a target dropped gradient similarity to 0.32.

**2. The benchmark has balance issues.** Mean 83 proponents per query but median 7, with outliers in the tens of thousands. A few geography predicates dominate the proponent pool, and 13.6% of queries leak the answer in the input. Removing top TracIn abstracts dropped accuracy 33% — TracIn finds *useful* data, just not always the labelled proponents.

**3. TracIn can surface misinformation.** Systematically poisoning ~4.5% of proponents with plausible-but-wrong targets, then scoring false queries, cleanly separated poisoned from clean abstracts — a more robust use-case than leave-one-out estimation.

- Long write-up: [Towards factual certainty in NLP using explainability methods](/blog/thesis/)
- Full report (Overleaf): [thesis PDF](https://www.overleaf.com/read/vdyqtjdyvxmk)
