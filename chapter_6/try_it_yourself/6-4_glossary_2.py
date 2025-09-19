glossary = {
    "loop": "process of completing an action x times.",
    "tuple": "a tuple is ordered and immutable.",
    "set": "unordered collection with no duplicated items.",
    "list": "a list is ordered and mutable, and it does allow duplicates.",
    "conditional": "decision making process.",
    "items method": "grabs the key-value pair and assigns them to variables",
    "keys method": "grabs the key and assigns it to a variable",
    "values method": "grabs the value of a key and assigns it to a variable",
    "sorted function": "returns item(s) in alphabetical order",
    "get method": "set a default value if a key doesn't exist, used to avoid KeyError",
}

for name, definition in sorted(glossary.items()):
    print(f"{name.title()}: {definition}\n")