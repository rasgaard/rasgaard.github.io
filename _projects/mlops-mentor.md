---
title: MLOps mentor
layout: default
date: 2026-01-31
status: finished
summary: Every one of 450 students deserves feedback while they work. TAs cannot read 450 repos, so the reading got automated.
---

# {{ page.title }}

## Goal

Four hundred and fifty students doing course projects deserve feedback *while* they work, not after grades land. No teaching team can read that many repositories by hand, so the reading itself had to be automated.

## Report

Built [rasgaard/mlops-mentor](https://github.com/rasgaard/mlops-mentor): repo mining for concrete signals (CI setup, dependency files, code volume) plus a language-model pass for qualitative feedback. Results flow into a public dataset and a [Gradio app](https://huggingface.co/spaces/rasgaard/DTU-MLOps-TA) anyone can browse.

Two honest footnotes. It never quite became an official course tool; the hope was to shape it together with the students instead. And TA-ing made something obvious: language models have absorbed the TA's old role as the patient, always-on helper. What a course like this really teaches now is *stamina*, the art of wrestling dependency hell until things just work.
