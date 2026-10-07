# AI Failure Mode Analysis

An early experiment (April 2026) in how a keyword-based classifier fails on emotionally ambiguous text. It asks whether such a classifier can tell distress from neutral language when nobody uses the obvious words.

## What is here

```
src/
  failure_analysis.py   baseline keyword classifier over labelled samples
  improved_model.py     second iteration with more patterns
  evaluate_model.py     accuracy and per-sample output
  failure_cases.md      the misses, written up one by one
notebooks/
  experiment_1_analysis.ipynb
results/
  evaluation_summary.md
```

## Result

```bash
cd src && python3 evaluate_model.py
```

The current code scores **4 of 5 (80%)** on five hand-labelled sentences. The one miss is `"Everything is fine!"`, labelled Negative, which the classifier calls Neutral. It has no way to see suppression or sarcasm behind a positive word.

`results/evaluation_summary.md` reports 40%. That came from the first version of the keyword rules. I widened the rules afterwards while looking at the same five sentences, and the score doubled.

That is the real finding. A classifier tuned while looking at its own test set will look good on it. Five sentences I wrote myself cannot tell me whether the rules generalise. They can only tell me the rules match what I already expected.

`src/failure_cases.md` has the original write-ups of the ambiguous cases ("I feel okay today.", "I don't know what to do anymore.", "Everything is fine!").

## What it led to

Two conclusions shaped what I built afterwards:

1. A keyword classifier should never be the primary safety layer. It is useful as a high-precision **backstop** when the real classifier is down, and nowhere else.
2. A test set you tune against is not an evaluation. The next version needed a larger labelled set, written before the rules, and a CI gate that fails on any missed crisis case.

Both are implemented in **[failclosed-guardrail](https://github.com/finessehumxn/failclosed-guardrail)**. See also **[emosafe-ai](https://github.com/finessehumxn/emosafe-ai)**, which probes the output side.

## Limits

Five samples. No ML model is included. The roadmap items from the first draft of this README (a BERT classifier, cross-model comparison) were not built here. That work moved to the repo above.

L.Finesse Humxn · [finessehumxn.com/work](https://finessehumxn.com/work)
