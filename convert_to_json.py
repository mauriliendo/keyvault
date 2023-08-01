import json

def convert_to_json(secrets):
    return json.dumps(secrets, indent=4)
