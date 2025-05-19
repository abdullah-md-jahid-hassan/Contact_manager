import csv

FILE_NAME = "contacts.csv"

def save_to_file(contact):
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(contact)

def load_from_file():
    contacts = []
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            contacts = [row for row in reader]
    except FileNotFoundError:
        open(FILE_NAME, mode='w').close()
    return contacts

def overwrite_file(contacts):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)