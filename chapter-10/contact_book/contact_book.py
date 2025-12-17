from pathlib import Path
import json

# File to store contacts
contacts_path = Path('chapter-10/contact_book/contacts.json')


# Load the contact list from file, or create and empty list if the file
# doesn't exist
if contacts_path.exists():
    contacts_list = json.loads(contacts_path.read_text())
    # Check if it returned a dict instead of a list
    if isinstance(contacts_list, dict):
        # Wrap it in a list if it's a single contact dict
        # so .append() will work
        contacts_list = [contacts_list]
else:
    contacts_list = []


def add_contact():
    """Creates a new contact entry"""

    contact = {
        'name': input("Enter your name: "),
        'phone': input("Enter your phone number: "),
        'email': input("Enter your email address: ")
    }
    contacts_list.append(contact)

    # Write the ENTIRE contact list back to the file, not just the new contact
    contacts_path.write_text(json.dumps(contacts_list, indent=2))
    print(f"{contact['name']} added!")


def view_contacts():
    """View all contacts in the contact list"""
    if not contacts_list:
        print("No contacts yet.")
        return
    for contact in contacts_list:
        print(f"{contact['name']}--{contact['phone']}--{contact['email']}")


def delete_contact():
    contacts_list = json.loads(contacts_path.read_text())
    name = input("Which contact would you like to delete? ").lower()
    for contact in contacts_list:
        if contact["name"].lower() == name:
            contacts_list.remove(contact)
            contacts_path.write_text(json.dumps(contacts_list, indent=2))
            print(f"{contact['name']} has been removed.")
    print("Contact not found.")     


# Main loop
while True:
    action = input("[a]: Add new contact\n"
                   "[v]: View contacts\n"
                   "[d] Delete contact by name\n"
                   "[q]: Quit\n")
    if action.lower() == 'a':
        add_contact()
    if action.lower() == 'v':
        view_contacts()
    if action.lower() == 'd':
        delete_contact()
    if action.lower() == 'q':
        break