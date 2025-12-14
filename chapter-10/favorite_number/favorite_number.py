from pathlib import Path
import json

path = Path('chapter-10/favorite_number/favorite_number.json')

# Program creates data
fav_num = int(input("What is your favorite number? "))
contents = json.dumps(fav_num)
path.write_text(contents)





