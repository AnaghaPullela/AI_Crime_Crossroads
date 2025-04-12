import json

def get_data():
    with open('simplified-nq-train.jsonl', 'r') as file:
        for line in file:
            data = json.loads(line)