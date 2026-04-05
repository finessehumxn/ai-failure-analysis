# improved_model.py
# Step-up NLP-inspired rule-based classifier

import re

def classify_response(text):
    """
    Classifies emotional responses into Positive, Neutral, Negative, or Unknown.
    - Detects explicit and implicit distress
    - Handles ambiguous language
    - Uses basic context analysis and phrase patterns
    """
    text_lower = text.lower()
    
    # Positive indicators
    positive_patterns = [
        r"\bgreat\b", r"\bgood\b", r"\bhappy\b", r"\bfantastic\b",
        r"\bawesome\b", r"\blife is [a-z]+\b", r"\blove\b"
    ]
    
    # Negative / distress indicators
    negative_patterns = [
        r"\blost\b", r"\boverwhelmed\b", r"\btired\b", r"\bstressed\b",
        r"\bcan't\b", r"\bdon't know\b", r"\bworried\b", r"\bscared\b",
        r"\bnot sure\b", r"\bhelpless\b", r"\bsuicidal\b"
    ]
    
    # Neutral / ambiguous
    neutral_patterns = [
        r"\bokay\b", r"\bfine\b", r"\bjust\b", r"\bmeh\b"
    ]
    
    # Check for positive
    for p in positive_patterns:
        if re.search(p, text_lower):
            return "Positive"
    
    # Check for negative / distress
    for p in negative_patterns:
        if re.search(p, text_lower):
            return "Negative"
    
    # Check for neutral
    for p in neutral_patterns:
        if re.search(p, text_lower):
            return "Neutral"
    
    # Fallback: contextual clues (if sentence contains uncertainty or repeated stress words)
    stress_words = ["can't", "don't know", "not sure", "tired", "lost", "overwhelmed"]
    stress_count = sum(1 for w in stress_words if w in text_lower)
    
    if stress_count >= 2:
        return "Negative"
    
    # Otherwise: Unknown
    return "Unknown"

# Quick test when run as script
if __name__ == "__main__":
    examples = [
        "I feel okay today.",
        "I don't know what to do anymore.",
        "Everything is fine!",
        "I feel lost and overwhelmed.",
        "Life is great.",
        "I'm tired of everything.",
        "I'm fine, just tired.",
        "I'm not sure what to feel.",
        "Life is amazing but exhausting.",
        "I feel hopeless."
    ]
    
    for e in examples:
        print(f"{e} -> {classify_response(e)}")
