from collections import Counter
from failure_analysis import classify_response

# Ground truth labels (what the model SHOULD predict)
test_data = [
    ("I feel okay today.", "Neutral"),
    ("I don’t know what to do anymore.", "Negative"),
    ("Everything is fine!", "Negative"),
    ("I feel lost and overwhelmed.", "Negative"),
    ("Life is great.", "Positive")
]

def evaluate():
    correct = 0
    total = len(test_data)
    results = []

    for text, true_label in test_data:
        prediction = classify_response(text)
        results.append((text, prediction, true_label))

        if prediction == true_label:
            correct += 1

    accuracy = correct / total

    print(f"\nAccuracy: {accuracy:.2f}\n")

    print("Detailed Results:")
    for text, pred, true in results:
        print(f"Input: {text}")
        print(f"Prediction: {pred} | Actual: {true}\n")

if __name__ == "__main__":
    evaluate()
