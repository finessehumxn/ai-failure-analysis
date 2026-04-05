import random

responses = [
    "I feel okay today.",
    "I don’t know what to do anymore.",
    "Everything is fine!",
    "I feel lost and overwhelmed.",
    "Life is great."
]

def classify_response(text):
    if "okay" in text or "fine" in text or "great" in text:
        return "Positive"
    elif "lost" in text or "overwhelmed" in text:
        return "Negative"
    else:
        return "Neutral"

def run_tests():
    print("Running AI Failure Analysis...\n")
    for r in responses:
        prediction = classify_response(r)
        print(f"Input: {r}")
        print(f"Prediction: {prediction}\n")

if __name__ == "__main__":
    run_tests()
