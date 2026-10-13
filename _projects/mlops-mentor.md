---
title: MLOps mentor
layout: default
date: 2026-01-31
status: finished
summary: Auto-scraping 450 student MLOps repos plus a Gradio app for scalable project feedback.
---

# {{ page.title }}

## Goal

Give ~450 MLOps students reliable, ongoing feedback on their group projects, without TAs having to read every single repository.

## Report

Collected my supervisor's scraping scripts into [rasgaard/mlops-mentor](https://github.com/rasgaard/mlops-mentor): repo mining for high-level indicators (CI workflow files, `requirements.txt`, lines of code), expanded with an LLM pass for qualitative feedback. Results land in a HuggingFace dataset, surfaced through a [Gradio app](https://huggingface.co/spaces/rasgaard/DTU-MLOps-TA).

Two honest footnotes. First, I never got fully comfortable blessing it as an *official* tool; the hope was to co-create it with the students during the course. Second, TA-ing made one thing obvious: LLMs have largely absorbed the TA's old job as the patient, always-on helper. What the course really teaches now is *stamina*: going at dependency hell and incompatibilities until things just work.
