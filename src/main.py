from model.contact import Contact
from model.address_book import AddressBook
from model.edit_contact import EditContact


address_book = AddressBook()
edit_contact = EditContact()


while True:

    print("\n===== ADDRESS BOOK =====")
    print("1. Add Contact")
    print("2. Edit Contact")
    print("3. Display Contacts")
    print("4. Exit")

    choice = input("Enter your choice: ")

    match choice:

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

        case "2":
            print("\n--- Edit Contact ---")

            if not address_book.contacts:
                print("No contacts available to edit.")
            else:
                first_name = input(
                    "Enter First Name of Contact to Edit: "
                )

                edit_contact.edit_contact(
                    address_book.contacts,
                    first_name
                )

        case "3":
            print("\n--- Contact List ---")

            if not address_book.contacts:
                print("No contacts available.")
            else:
                address_book.display_contacts()

        case "4":
            print("\nExiting Address Book...")
            break

        case _:
            print("\nInvalid choice. Please try again.")