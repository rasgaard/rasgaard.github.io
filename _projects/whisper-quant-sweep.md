---
title: Whisper quantization sweep
layout: default
date: 2025-11-30
status: dropped
summary: TorchAO int8 + Wanda sparsity on Whisper-small, shelved when layer pruning proved far more effective.
---

# {{ page.title }}

## Goal

Map the moderate-compression landscape for `Whisper-small` (244M params) on LibriSpeech: int8 quantization and 50% unstructured sparsity, aiming for the kind of overview tables the PyTorch blog produces for LLMs.

## Report

The numbers told a split story:

| Setup | Size | WER |
| ----- | ---- | --- |
| Baseline | 1074 MB | **4.27%** |
| Int8 weight-only | 578 MB | **4.24%** |
| Wanda 50% unstructured | 1074 MB | **101.20%** |
| … + 1 epoch calibration | 1074 MB | **17.75%** |
| … + 2 epochs calibration | 1074 MB | **17.63%** |

Quantization was essentially free; unstructured sparsity collapsed the model, and calibration only partly resurrected it. Getting started took help from TorchAO maintainer Jesse Cai via the GPU MODE Discord, much appreciated.

**Why dropped:** two reasons. First, I wanted dedicated time on the edge-deployment branch rather than more sweeps. Second, layer pruning later proved *far* more effective for Whisper. Kept here so the dead end stays visible.
