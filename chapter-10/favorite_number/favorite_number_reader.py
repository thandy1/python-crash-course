from pathlib import Path
import json

path = Path("chapter-10/favorite_number/favorite_number.json")

# Program uses data for later
if path.exists():
    number = json.loads(path.read_text())
    print(f"I know your favorite number! It's {number}")