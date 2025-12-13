from pathlib import Path

path = Path('chapter-10/guest-book/guest-book.txt')
guest_book = []
while True:
    name = input("Enter your name ('q' to quit): ")
    if name.lower() == "q":
        break
    guest_book.append(name)
    
    # Takes each element in the guest book list and joins them into a single string
    # putting a newline between each element
    path.write_text("\n".join(guest_book))  
    