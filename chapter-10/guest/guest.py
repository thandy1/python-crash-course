from pathlib import Path

path = Path('chapter-10/guest/guest.txt')
name = input("Enter your name: ")
path.write_text(name)