import json

def sanitize_for_json(text):
    return json.dumps(text)

print(sanitize_for_json("dfdgdg"))