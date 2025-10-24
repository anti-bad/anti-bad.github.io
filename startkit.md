---
layout: default
title: Starter Kit
permalink: /startkit/
---

## Starter Kit

The **Anti-Backdoor (Anti-BAD) Challenge Starter Kit** provides everything you need to participate — including datasets, backdoored models, scripts, and submission templates.  
It is designed to help participants reproduce the competition setup and start building their defences quickly.

---

## Repository

All materials are publicly available on GitHub:  
[https://github.com/anti-bad/anti-bad-challenge](https://github.com/anti-bad/anti-bad-challenge)

The repository contains detailed setup instructions, environment configuration, baseline examples, and scripts for preparing and submitting results.

---

## What’s Included

* **Datasets** — input-only test sets for each task (no ground truth).  
* **Models** — three backdoored models per task, based on popular architectures such as *Llama* and *Qwen*.  
* **Code Scripts** — to make predictions on the test inputs and submit to the CodaBench to get scores.
* **Submission Templates** — JSON and CSV examples for all tracks.  
* **Baseline Implementation** — a reference defense based on Weight Averaging (WAG).

---

## Tracks and Tasks

The challenge features **three tracks** with **six tasks** in total:

| Track          | Tasks | Models per Task          |
| -------------- | ----- | ------------------------ |
| Generation     | 2     | 3 backdoored models each |
| Classification | 2     | 3 backdoored models each |
| Multilingual   | 2     | 3 backdoored models each |

For each task, participants receive several backdoored models of the same architecture and a test dataset (inputs only).  
Your goal is to defend the models, generate predictions, and submit your results for evaluation on **Codabench**.

---

## Submission Overview

1. Generate predictions for selected tasks.  
2. Package the prediction files into a single ZIP archive.  
3. Upload the ZIP file through the **My Submissions** tab on **Codabench**.

**Submission limits:**

* **Development phase:** up to **3 submissions per day**, **270 total**.  
* **Test phase:** up to **2 submissions per day**, **14 total**.  

During the **test phase**, top-performing teams must submit both prediction results and executable code for reproducibility verification.  
The code must reproduce the submitted results within **24 hours on a single NVIDIA A100 80GB GPU**.  
All submitted code will remain private and used only for verification purposes.

---

## Baseline Method

The Starter Kit includes a baseline defense using **Weight Averaging (WAG)** across all tracks.  
Implementation and usage examples are available in the repository.

If you reference this method, please cite:

> **Ansh Arora, Xuanli He, Maximilian Mozes, Srinibas Swain, Mark Dras, and Qiongkai Xu.** (2024). *[Here's a Free Lunch: Sanitizing Backdoored Models with Model Merge](https://aclanthology.org/2024.findings-acl.894/).* *Findings of the Association for Computational Linguistics: ACL 2024.*

---

For more information on submission formats and evaluation rules, see the [**Competition Platform**](#) or visit the [**Starter Kit on GitHub**](https://github.com/anti-bad/anti-bad-challenge).