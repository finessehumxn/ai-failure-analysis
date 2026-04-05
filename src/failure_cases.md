# Failure Case Log

## Case 1: Ambiguous Distress

**Input:** "I feel okay today."
**Model Output:** Positive  
**Expected Interpretation:** Potentially Neutral / Masked Distress  

**Issue:**
The model assumes "okay" indicates a positive emotional state, ignoring possible emotional masking.

---

## Case 2: Emotional Uncertainty

**Input:** "I don’t know what to do anymore."
**Model Output:** Neutral  
**Expected Interpretation:** Negative / Distress  

**Issue:**
The model fails to detect implicit distress in uncertain language.

---

## Case 3: Surface Positivity

**Input:** "Everything is fine!"
**Model Output:** Positive  
**Expected Interpretation:** Possibly Negative (sarcasm or suppression)  

**Issue:**
The model cannot detect tone, sarcasm, or contradiction.
