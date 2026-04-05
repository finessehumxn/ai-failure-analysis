import random

responses = [
    "I feel okay today.",
    "I don’t know what to do anymore.",
    "Everything is fine!",
    "I feel lost and overwhelmed.",
    "Life is great."
]

def classify_response(text):
    text = text.lower()

    if any(word in text for word in ["great", "amazing", "happy"]):
        return "Positive"
    elif any(word in text for word in ["lost", "overwhelmed", "don’t know", "dont know"]):
        return "Negative"
    elif any(word in text for word in ["okay", "fine"]):
        return "Neutral"
    else:
        return "Unknown"

def run_tests():
    print("Running AI Failure Analysis...\n")
    for r in responses:
        prediction = classify_response(r)
        print(f"Input: {r}")
        print(f"Prediction: {prediction}\n")

if __name__ == "__main__":
    run_tests()
