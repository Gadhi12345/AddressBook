from model.contact import Contact
from model.address_book import AddressBook
from model.edit_contact import EditContact
from model.delete_contact import DeleteContact


address_book = AddressBook()
edit_contact = EditContact()
delete_contact = DeleteContact()


while True:

    print("\n===== ADDRESS BOOK =====")
    print("1. Add Contact")
    print("2. Edit Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    match choice:

        # ---------- ADD CONTACT ----------
        case "1":
            print("\n--- Add Contact ---")

            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            address = input("Enter Address: ")
            city = input("Enter City: ")
            state = input("Enter State: ")
            zip_code = input("Enter Zip Code: ")
            phone_number = input("Enter Phone Number: ")
            email = input("Enter Email: ")

            contact = Contact(
                first_name,
                last_name,
                address,
                city,
                state,
                zip_code,
                phone_number,
                email
            )

            address_book.add_contact(contact)


        # ---------- EDIT CONTACT ----------
        case "2":
            print("\n--- Edit Contact ---")

            first_name = input(
                "Enter First Name of Contact to Edit: "
            )

            edit_contact.edit_contact(
                address_book.contacts,
                first_name
            )


        # ---------- DELETE CONTACT ----------
        case "3":
            print("\n--- Delete Contact ---")

            first_name = input(
                "Enter First Name of Contact to Delete: "
            )

            delete_contact.delete_contact(
                address_book.contacts,
                first_name
            )


        # ---------- DISPLAY CONTACTS ----------
        case "4":
            print("\n--- Contact List ---")

            address_book.display_contacts()


        # ---------- EXIT ----------
        case "5":
            print("\nExiting Address Book...")
            break


        # ---------- INVALID CHOICE ----------
        case _:
            print("\nInvalid choice. Please try again.")