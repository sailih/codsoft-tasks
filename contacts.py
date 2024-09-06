1# Contact class to store contact information
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name}: {self.phone}, {self.email}"

# ContactBook class to store a list of contacts
class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        for contact in self.contacts:
            print(contact)

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(contact)
                return
        print("Contact not found!")

# Create a ContactBook instance
contact_book = ContactBook()

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter contact phone: ")
        email = input("Enter contact email: ")
        contact_book.add_contact(name, phone, email)
    elif choice == "2":
        contact_book.view_contacts()
    elif choice == "3":
        name = input("Enter contact name to search: ")
        contact_book.search_contact(name)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again!")