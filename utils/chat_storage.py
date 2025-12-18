import json
import os

CHAT_FILE = "chat_history.json"

def load_file():
    if os.path.exists(CHAT_FILE):
        with open(CHAT_FILE, "r") as f:
            return json.load(f)
    return []
def save_file(messages):
    with open(CHAT_FILE, "w") as f:
        json.dump(messages, f)