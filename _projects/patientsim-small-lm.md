---
title: Small models as simulated patients
layout: default
date: 2026-10-13
status: ongoing
summary: Finding the smallest AI that can realistically play a patient, so training simulators work fully offline.
---

# {{ page.title }}

## Goal

Nurses learn by practicing difficult conversations with patients, and increasingly that practice happens with simulated patients played by AI. Today those simulations need large AI models running on powerful servers, which means they only work with a good internet connection and someone else's computer doing the work.

Laerdal trains health workers in places where that assumption breaks: tight data plans, unreliable connectivity, strict privacy needs. If the simulated patient could run entirely on an ordinary device with no internet at all, training could go anywhere. The question is how small the AI can get before the patient stops feeling like a patient.

## Report

The plan is simple: let small AI models play patients, watch carefully where they fail, and use those failures to judge the next candidate. First against scripted students for breadth (one hundred sessions), then against a stronger AI student for depth (sixty sessions), with every session scored on what good patient simulation actually requires.

The sixty in-depth sessions are done and scored. Right now the work is checking the automatic scoring against human judgment, so the judge can be trusted going forward.
