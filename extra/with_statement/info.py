import json

with open('extra/with_statement/info.json', 'w') as file: 
    # Takes the python object, converts it into a json string 
    # and writes the data into the opened file object
    json.dump({"name": "Alice","age": 25,}, file, indent=2)

with open('extra/with_statement/info.json', 'r') as f:
    loaded_data = json.load(f)
print(loaded_data)
