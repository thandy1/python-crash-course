from pathlib import Path

dog_path = Path('chapter-10/cats-and-dogs/dogs.txt')
cat_path = Path('chapter-10/cats-and-dogs/cats.txt')

try:
    print(dog_path.read_text())
except FileNotFoundError:
    pass

try:
    print(cat_path.read_text())
except FileNotFoundError:
    pass

