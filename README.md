# AI Failure Mode Analysis

**Structured evaluation of AI system behavior in emotionally sensitive, human-centered domains.**

[![Language](https://img.shields.io/badge/Language-Python%20%7C%20Jupyter-blue?style=flat)]()
[![Domain](https://img.shields.io/badge/Domain-AI%20Evaluation%20%7C%20Safety--Critical%20Systems-purple?style=flat)]()
[![Status](https://img.shields.io/badge/Status-Active%20Research-yellow?style=flat)]()

---

## Problem Statement

Standard AI evaluation optimizes for accuracy on clean, well-formed inputs. Production systems — especially in mental health and healthcare — encounter inputs that are ambiguous, emotionally loaded, indirect, and structurally atypical.

This project focuses on what happens at that boundary.

The question is not *can the model get it right on a benchmark?* The question is *what does the model do when the input is messy and the cost of a wrong answer is human?*

---

## Motivation

This research comes from direct production experience: 7+ years building and operating AI systems in emotionally high-stakes environments — including a live youth suicide prevention platform across 8+ countries and a deployed healthcare AI assistant.

In those systems, false negatives on distress signals, miscalibrated confidence on emotionally ambiguous inputs, and guardrail failures under edge-case load are not abstract concerns. They are operational risk.

This project builds the structured evaluation foundation to identify, categorize, and track those failure patterns before deployment — and to feed findings back into guardrail design.

---

## Project Structure

```
ai-failure-analysis/
├── src/
│   ├── model_simulation.py       # Baseline classifier implementation
│   ├── evaluation.py             # Scoring, metrics, and failure logging
│   ├── improved_model.py         # Enhanced rule-based classifier (iterated)
│   └── failure_cases.md          # Documented failure cases with analysis
├── notebooks/
│   └── experiment_1_analysis.ipynb   # Full experiment walkthrough
├── results/
│   └── evaluation_summary.md     # Structured output summary
└── README.md
```

---

## Experiment 1: Baseline Rule-Based Classifier

### Objective
Establish a performance floor. Quantify how a naive, keyword-dependent classifier performs on emotionally ambiguous text — specifically text that may signal distress without using explicit distress vocabulary.

### Implementation
Rule-based classifier operating on keyword presence and simple pattern matching — intentionally simplified to surface fundamental failure modes before introducing model complexity.

### Results

| Metric | Value |
|---|---|
| Overall Accuracy | ~40% |
| False Negative Rate (distress) | High |
| Confidence Calibration | Poor — overconfident on surface matches |

### Failure Taxonomy

| Category | Pattern | Risk Level |
|---|---|---|
| **Implicit distress** | Distress framed as fatigue, disengagement, or humor | High |
| **Keyword dependency** | Correct classification only when explicit terms present | High |
| **Ambiguity collapse** | Ambiguous inputs defaulting to neutral/positive classification | Medium-High |
| **Context blindness** | Single-sentence accuracy decoupled from conversational context | Medium |

### Interpretation

A 40% accuracy rate in a general task is a failed model. In a mental health context, it means the majority of non-explicit distress signals produce incorrect outputs — which in a deployed system translates to dismissive or inappropriate responses to people who are struggling.

That is the point of measuring it.

---

## Evaluation Philosophy

This project uses a **human-impact-centered evaluation framework** rather than standard benchmark metrics:

- **False negative cost weighting** — missed distress signals weighted higher than false positives
- **Confidence-accuracy gap tracking** — identifies where model certainty diverges from actual reliability
- **Edge case saturation testing** — inputs designed to stress the boundary conditions, not the center of the distribution
- **Failure mode categorization** — structured taxonomy for cross-model comparison

---

## Experiment Roadmap

| Experiment | Status | Description |
|---|---|---|
| Baseline rule-based classifier | ✅ Complete | Performance floor established |
| Enhanced rule-based classifier | ✅ Complete | Iterated improvements |
| NLP/ML classifier | 🔄 In Progress | BERT-based model on same dataset |
| Production LLM evaluation | 📋 Planned | GPT-4 / Claude on edge case set |
| Guardrail stress testing | 📋 Planned | Safety filter behavior under adversarial input |
| Cross-model failure comparison | 📋 Planned | Structured taxonomy across model types |

---

## Relationship to Production Systems

Findings from this project directly inform:

- Guardrail node design in **[MedCompanionAI](https://github.com/finessehumxn/medcompanion-ai)**
- Prompt engineering and safety routing in live mental health infrastructure
- **[EmoSafe AI](https://github.com/finessehumxn/emosafe-ai)** — LLM behavior observation on emotionally sensitive prompts

---

## Built By

**L. Finesse Humxn** — AI systems engineer. Founder of [Finesse Our Minds](https://finesseourminds.com).

[![LinkedIn](https://img.shields.io/badge/LinkedIn-lfinesse---%230077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/lfinesse-)
