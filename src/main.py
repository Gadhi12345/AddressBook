from model.contact import Contact
from model.address_book import AddressBook
from model.edit_contact import EditContact
from model.delete_contact import DeleteContact
from model.duplicate_contact import DuplicateContact
from model.search_contact import SearchContact


# Dictionary to store multiple Address Books
address_books = {}

# Objects for different operations
edit_contact = EditContact()
delete_contact = DeleteContact()
duplicate_contact = DuplicateContact()
search_contact = SearchContact()


while True:

    # ================= MAIN MENU =================

    print("\n===== ADDRESS BOOK SYSTEM =====")
    print("1. Create Address Book")
    print("2. Select Address Book")
    print("3. Display Address Books")
    print("4. Search Person by City")
    print("5. Search Person by State")
    print("6. Exit")

    choice = input("Enter your choice: ")

    match choice:

        # ---------- CREATE ADDRESS BOOK ----------
        case "1":

            book_name = input("Enter Address Book Name: ")

            if book_name in address_books:

                print("\nAddress Book already exists.")

            else:

                address_books[book_name] = AddressBook()

                print(
                    f"\nAddress Book '{book_name}' "
                    "created successfully."
                )


        # ---------- SELECT ADDRESS BOOK ----------
        case "2":

            book_name = input("Enter Address Book Name: ")

            if book_name not in address_books:

                print("\nAddress Book not found.")

            else:

                # Get selected Address Book
                address_book = address_books[book_name]

                while True:

                    # ============= CONTACT MENU =============

                    print(
                        f"\n===== {book_name} ADDRESS BOOK ====="
                    )

                    print("1. Add Contact")
                    print("2. Edit Contact")
                    print("3. Delete Contact")
                    print("4. Display Contacts")
                    print("5. Back")

                    contact_choice = input(
                        "Enter your choice: "
                    )

                    match contact_choice:

                        # ---------- ADD CONTACT ----------
                        case "1":

                            print("\n--- Add Contact ---")

                            first_name = input(
                                "Enter First Name: "
                            )

                            last_name = input(
                                "Enter Last Name: "
                            )

                            # UC6 - Check duplicate contact
                            if duplicate_contact.is_duplicate(
                                address_book.contacts,
                                first_name,
                                last_name
                            ):

                                print(
                                    "\nContact already exists. "
                                    "Duplicate contact not allowed."
                                )

                            else:

                                address = input(
                                    "Enter Address: "
                                )

                                city = input(
                                    "Enter City: "
                                )

                                state = input(
                                    "Enter State: "
                                )

                                zip_code = input(
                                    "Enter Zip Code: "
                                )

                                phone_number = input(
                                    "Enter Phone Number: "
                                )

                                email = input(
                                    "Enter Email: "
                                )

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

                                address_book.add_contact(
                                    contact
                                )


                        # ---------- EDIT CONTACT ----------
                        case "2":

                            print("\n--- Edit Contact ---")

                            if not address_book.contacts:

                                print(
                                    "\nNo contacts available "
                                    "to edit."
                                )

                            else:

                                first_name = input(
                                    "Enter First Name of "
                                    "Contact to Edit: "
                                )

                                edit_contact.edit_contact(
                                    address_book.contacts,
                                    first_name
                                )


                        # ---------- DELETE CONTACT ----------
                        case "3":

                            print("\n--- Delete Contact ---")

                            if not address_book.contacts:

                                print(
                                    "\nNo contacts available "
                                    "to delete."
                                )

                            else:

                                first_name = input(
                                    "Enter First Name of "
                                    "Contact to Delete: "
                                )

                                delete_contact.delete_contact(
                                    address_book.contacts,
                                    first_name
                                )


                        # ---------- DISPLAY CONTACTS ----------
                        case "4":

                            print("\n--- Contact List ---")

                            address_book.display_contacts()


                        # ---------- BACK ----------
                        case "5":

                            break


                        # ---------- INVALID CONTACT CHOICE ----------
                        case _:

                            print(
                                "\nInvalid choice. "
                                "Please try again."
                            )


        # ---------- DISPLAY ADDRESS BOOKS ----------
        case "3":

            print("\n--- Available Address Books ---")

            if not address_books:

                print("No Address Books available.")

            else:

                for book_name in address_books:

                    print(book_name)


        # ---------- SEARCH PERSON BY CITY ----------
        case "4":

            print("\n--- Search Person by City ---")

            city = input(
                "Enter City to Search: "
            )

            search_contact.search_by_city(
                address_books,
                city
            )


        # ---------- SEARCH PERSON BY STATE ----------
        case "5":

            print("\n--- Search Person by State ---")

            state = input(
                "Enter State to Search: "
            )

            search_contact.search_by_state(
                address_books,
                state
            )


        # ---------- EXIT ----------
        case "6":

            print("\nExiting Address Book...")
            break


        # ---------- INVALID MAIN CHOICE ----------
        case _:

            print(
                "\nInvalid choice. "
                "Please try again."
            )