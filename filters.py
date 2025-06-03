import json

with open("data/blocked_words.json", "r", encoding="utf-8") as f:
    BLOCKED = json.load(f)

def is_message_allowed(message, country):
    blocked_words = BLOCKED.get(country, [])
    for word in blocked_words:
        if word.lower() in message.lower():
            return False
    return True