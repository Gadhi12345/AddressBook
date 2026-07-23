class EditContact:

    def edit_contact(self, contacts, first_name):

        for contact in contacts:

            if contact.first_name.lower() == first_name.lower():

                print("\nEnter New Contact Details")

                contact.last_name = input("Enter New Last Name: ")
                contact.address = input("Enter New Address: ")
                contact.city = input("Enter New City: ")
                contact.state = input("Enter New State: ")
                contact.zip_code = input("Enter New Zip Code: ")
                contact.phone_number = input("Enter New Phone Number: ")
                contact.email = input("Enter New Email: ")

                print("\nContact updated successfully.")
                return

        print("\nContact not found.")