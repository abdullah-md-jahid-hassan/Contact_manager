from contact_manager import add_contact, view_contacts, search_contact, remove_contact
from invalid_input_manager import validate_name, validate_email, validate_phone

def main_menu():
    while True:
        print("\n=== Contact Book Menu ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Remove Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            phone = input("Enter Phone: ")
            address = input("Enter Address: ")

            if not validate_name(name):
                print("Contact must have a name")
            elif not validate_email(email):
                print("Invalid email. Must include '@' and end with '.com'.")
            elif not validate_phone(phone):
                print("Invalid phone. Must be numeric.")
            else:
                print(add_contact(name, email, phone, address))

        elif choice == "2":
            print("\nContacts:\n")
            print(view_contacts())

        elif choice == "3":
            term = input("Enter search term: ")
            print("\nSearch Results:\n")
            print(search_contact(term))

        elif choice == "4":
            phone = input("Enter Phone Number of Contact to Remove: ")
            print(remove_contact(phone))

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()
