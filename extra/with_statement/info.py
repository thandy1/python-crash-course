import json

with open('extra/with_statement/info.json', 'w') as file:
    json.dump({"name": "Alice","age": 25,}, file, indent=2)

with open('extra/with_statement/info.json', 'r') as f:
    loaded_data = json.load(f)
print(loaded_data)
