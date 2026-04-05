def classify_response(text):
    text = text.lower()

    if any(word in text for word in ["great", "amazing", "happy"]):
        return "Positive"
    elif any(word in text for word in ["lost", "overwhelmed", "don’t know", "dont know", "anymore"]):
        return "Negative"
    elif any(word in text for word in ["okay", "fine"]):
        return "Neutral"
    else:
        return "Unknown"
