class DeleteContact:

    def delete_contact(self, contacts, first_name):

        for contact in contacts:

            if contact.first_name.lower() == first_name.lower():

                contacts.remove(contact)

                print("\nContact deleted successfully.")
                return

        print("\nContact not found.")