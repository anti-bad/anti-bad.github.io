---
layout: default
title: Anti-BAD Challenge
permalink: /challenge/
---

## Tasks and Application Scenarios

Participants are invited to develop methods for mitigating backdoor behaviors in language models under realistic post-deployment constraints. The Anti-BAD Challenge addresses common limitations faced by end-users, where retraining or extensive data analysis is often infeasible. The goal is to improve model trustworthiness without access to training data, backdoor-specific knowledge, or clean reference checkpoints—reflecting real-world challenges when models are obtained from public or third-party sources.

The competition features three tracks—**Classification**, **Multilingual**, and **Generation**—each consisting of a **Development** and a **Test** phase. Participants will be provided with compromised model checkpoints and evaluation inputs, and are expected to submit their restored predictions or outputs. Performance will be assessed using two primary metrics: **Attack Success Rate (ASR)** and **Clean Task Utility (CTU)**. An overview of each track is provided below.

### Track A – Classification Backdoor Mitigation

This track evaluates defenses on standard classification tasks using compromised models. Participants aim to recover clean label predictions while suppressing attack behaviors.

**Development Phase:**
- Access to clean and poisoned validation sets and an evaluation script to compute CTU and ASR.
- Leaderboard feedback is provided based on predicted labels submitted for input-only test sets.

**Test Phase:**
- New model checkpoints and test inputs (without ground-truth labels) will be released.
- Final submissions include predicted labels for clean and poisoned inputs.

### Track B – Multilingual Backdoor Mitigation

This track focuses on multilingual LLMs compromised across multiple languages. Participants aim to neutralize malicious behaviors while preserving clean utility across diverse language settings.

**Development Phase:**
- Clean and poisoned validation sets with evaluation scripts for CTU and ASR.
- Input-only test sets are available for leaderboard submission during development.

**Test Phase:**
- Participants receive new multilingual model checkpoints and test inputs.
- Final submissions include label predictions for clean and poisoned examples.

### Track C – Generation Backdoor Mitigation

This track evaluates defenses in generative tasks, where compromised models exhibit undesired generation behaviors. Participants are challenged to restore intended output quality while neutralizing malicious triggers.

**Development Phase:**
- A utility validation set with ground-truth outputs and an evaluation script for output quality.
- Poisoned validation inputs are provided for ASR computation.
- Leaderboard feedback is based on generated outputs submitted for clean and poisoned test sets.

**Test Phase:**
- New model checkpoints and input sets are released for final evaluation.
- Submissions consist of generated outputs that will be evaluated on both utility and ASR.

## Evaluation Protocol

Submissions will be evaluated based on their ability to mitigate backdoor behavior while preserving clean-task performance:

- **Attack Success Rate (ASR):** The proportion of poisoned inputs that successfully trigger malicious behavior. Lower is better.
- **Clean Task Utility (CTU):** The proportion of clean inputs for which the model performs as expected. Higher is better.

**Scoring:** An **Overall Score** will be computed as:
```
Overall Score = CTU - ASR
```

Participants will be ranked within each track, with final rankings based on aggregated ranks across all three tracks. The competition promotes **training-free, resource-efficient** defenses that generalize across tasks, languages, and threat types, supporting more **trustworthy and robust deployment** of LLMs.