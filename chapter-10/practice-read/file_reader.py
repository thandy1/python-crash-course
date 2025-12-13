from pathlib import Path

# cd to the scripts current working directory 
# or provide a relative or absolute path to run the code
path = Path("chapter-10/practice/pi_digits.txt")
contents = path.read_text()
contents.splitlines()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))
