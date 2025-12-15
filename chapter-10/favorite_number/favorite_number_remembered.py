from pathlib import Path
import json

path = Path("chapter-10/favorite_number/favorite_number.json")

# Same functionality, just in one file
if path.exists():
    number = json.loads(path.read_text())
    print(f"I know your favorite number! It's {number}")
else:
    fav_num = int(input("What is your favorite number? "))
    contents = json.dumps(fav_num)
    path.write_text(contents)