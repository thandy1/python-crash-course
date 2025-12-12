from pathlib import Path

# cd to the scripts current working directory 
# or provide a relative or absolute path to run the code
path = Path("chapter-10/practice/pi_digits.txt")
contents = path.read_text()
lines = contents.splitlines()
for line in lines:
    print(line)