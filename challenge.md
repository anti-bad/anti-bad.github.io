---
layout: default
title: Challenge
permalink: /challenge/
---

## Tasks and Application Scenarios

Participants are invited to develop methods for mitigating backdoor behaviors in language models under realistic post-deployment constraints. The Anti-BAD challenge addresses the practical constraints faced by end-users, where existing defenses—while suitable for well-resourced developers with access to large-scale data and compute for retraining or outlier detection—may fail to reflect realistic deployment scenarios. The goal is to improve model trustworthiness without access to training data, known triggers, or clean reference checkpoints—reflecting practical challenges faced when models are obtained from public or third-party sources.

The competition features three tracks—**Classification**, **Multilingual** and **Generation**—each consisting of a **Development** and a **Test** phase. Participants are provided with compromised model checkpoints (using open-source models such as LLaMA 3.1 8B, Qwen 3 8B, and EMMA-500 7B) and evaluation inputs, and are expected to submit their restored outputs or predictions. Performance will be assessed using two main metrics: **Attack Success Rate (ASR)** and **Clean Task Utility (CTU)**. Task details for each track are summarized below.

### Track A – Classification Backdoor Mitigation

Models are trained on standard classification datasets including SST-2, MultiNLI, and AG News, with backdoors injected using methods like BadNets, InsertSent, and HiddenKiller.

**Development Phase:**
- Clean and poisoned validation sets with an evaluation script to compute both CTU and ASR.
- Clean and poisoned test sets (input only); participants may submit predicted labels for leaderboard feedback.

**Test Phase:**
- Participants are provided with new model checkpoints and test inputs (without ground-truth labels).
- Final submissions are evaluated based on predicted labels for both clean and poisoned examples.

### Track B – Multilingual Backdoor Mitigation

Multilingual LLMs are fine-tuned on datasets such as Taxi1500, SIB-200, and XNLI, with backdoors injected using methods like BadNL, RIPPLES, and LWS. Attacks target selected language groups, while clean utility is evaluated on unpoisoned languages.

**Development Phase:**
- Clean and poisoned validation sets with an evaluation script to compute both CTU and ASR.
- Clean and poisoned test sets (input only); participants may submit predicted labels for leaderboard feedback.

**Test Phase:**
- Participants are provided with new model checkpoints and test inputs (without ground-truth labels).
- Final submissions are evaluated based on predicted labels for both clean and poisoned examples.

### Track C – Generation Backdoor Mitigation

Compromised LLMs are constructed by fine-tuning on instruction datasets (e.g., UltraChat, HH-RLHF) with backdoors such as content injection, over-refusal, sentiment steering, and Sleeper agents. The Alpaca dataset is used to measure clean task utility.

**Development Phase:**
- A utility validation set with ground-truth outputs and an evaluation script for assessing output quality.
- A poison validation set accompanied by metadata specifying target responses for ASR computation.
- Clean and poisoned test sets (no ground-truth or metadata); participants may submit generated outputs to receive leaderboard feedback.

**Test Phase:**
- Participants receive new model checkpoints and corresponding test inputs (clean and poisoned).
- Final submissions consist of generated outputs evaluated on utility and ASR criteria.

## Evaluation Protocol

We evaluate submissions based on their ability to mitigate backdoor behavior while preserving clean-task performance using:

- **Attack Success Rate (ASR)**: The proportion of poisoned inputs that successfully trigger the attacker's intended behavior. Lower ASR indicates stronger robustness.
- **Clean Task Utility (CTU)**: The proportion of clean inputs for which the model output aligns with the expected result.

**Scoring**: A unified **Overall Score** is used to rank submissions within each track:
```
Overall Score = CTU - ASR
```

Participants are ranked in each track, with final rankings based on aggregated ranks across all tracks. The challenge targets **training-free, resource-efficient** defenses that generalize across tasks, languages, and attack types.