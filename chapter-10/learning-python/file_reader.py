from pathlib import Path

path = Path('chapter-10/learning-python/learning_python.txt')
print(path.read_text())

lines = path.read_text().splitlines()
string = " "
for line in lines:
    line = line.replace("Python", "C")
    print(line)


