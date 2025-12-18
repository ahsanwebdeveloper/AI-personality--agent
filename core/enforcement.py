# Scope checking logic
def is_in_scope(user_input, scope):
    text = user_input.lower()

    if scope == "math":
        return any(char.isdigit() for char in text)

    if scope == "medical":
        keywords = [
            "medical", "health", "doctor", "medicine",
            "symptom", "disease", "fever", "pain"
        ]
        return any(word in text for word in keywords)

    if scope == "travel":
        keywords = [
            "travel", "trip", "tour", "guide",
            "destination", "flight", "hotel"
        ]
        return any(word in text for word in keywords)

    if scope == "cooking":
        keywords = [
            "cook", "recipe", "food", "bake",
            "ingredients", "kitchen"
        ]
        return any(word in text for word in keywords)

    if scope == "tech":
        keywords = [
            "error", "bug", "software", "computer",
        "install", "crash", "issue", "laptop",
        "pc", "windows", "linux", "mac",
        "network", "internet", "wifi",
        "driver", "update", "server"
        ]
        return any(word in text for word in keywords)

    return False
