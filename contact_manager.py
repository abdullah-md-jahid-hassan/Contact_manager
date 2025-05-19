from contact_file_manager import save_to_file, load_from_file, overwrite_file

def add_contact(name, email, phone, address):
    contacts = load_from_file()
    if any(contact[2] == phone for contact in contacts):
        return "Error: Phone number already exists."
    contact = [name, email, phone, address]
    save_to_file(contact)
    return "Contact added successfully."

def view_contacts():
    contacts = load_from_file()
    if not contacts:
        return "No contacts available."
    return "\n".join([f"Name: {c[0]}, Email: {c[1]}, Phone: {c[2]}, Address: {c[3]}" for c in contacts])

def search_contact(term):
    contacts = load_from_file()
    results = [c for c in contacts if term.lower() in [field.lower() for field in c]]
    if not results:
        return "No matching contacts found."
    return "\n".join([f"Name: {c[0]}, Email: {c[1]}, Phone: {c[2]}, Address: {c[3]}" for c in results])

def remove_contact(phone):
    contacts = load_from_file()
    updated_contacts = [c for c in contacts if c[2] != phone]
    if len(contacts) == len(updated_contacts):
        return "Error: Contact not found."
    overwrite_file(updated_contacts)
    return "Contact removed successfully."
