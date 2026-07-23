class AddressBook:

    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("\nContact added successfully.")

    def display_contacts(self):
        if not self.contacts:
            print("\nNo contacts found.")
            return

        for contact in self.contacts:
            contact.display_contact()