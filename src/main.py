from model.contact import Contact
from model.address_book import AddressBook
from model.edit_contact import EditContact
from model.delete_contact import DeleteContact
from model.duplicate_contact import DuplicateContact
from model.search_contact import SearchContact
from model.view_contact import ViewContact
from model.count_contact import CountContact


# Dictionary to store multiple Address Books
address_books = {}

# Objects for different operations
edit_contact = EditContact()
delete_contact = DeleteContact()
duplicate_contact = DuplicateContact()
search_contact = SearchContact()
view_contact = ViewContact()
count_contact = CountContact()


while True:

    print("\n===== ADDRESS BOOK SYSTEM =====")
    print("1. Create Address Book")
    print("2. Select Address Book")
    print("3. Display Address Books")
    print("4. Search Person by City")
    print("5. Search Person by State")
    print("6. View Persons by City")
    print("7. View Persons by State")
    print("8. Count Persons by City")
    print("9. Count Persons by State")
    print("10. Exit")

    choice = input("Enter your choice: ")

    match choice:

        # ---------- CREATE ADDRESS BOOK ----------
        case "1":

            book_name = input("Enter Address Book Name: ")

            if book_name in address_books:
                print("Address Book already exists.")

            else:
                address_books[book_name] = AddressBook()

                print(
                    f"Address Book '{book_name}' "
                    "created successfully."
                )


        # ---------- SELECT ADDRESS BOOK ----------
        case "2":

            book_name = input("Enter Address Book Name: ")

            if book_name not in address_books:

                print("Address Book not found.")

            else:

                address_book = address_books[book_name]

                while True:

                    print(
                        f"\n===== {book_name} "
                        "ADDRESS BOOK ====="
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

                            # Check duplicate before
                            # entering remaining details
                            is_duplicate = (
                                duplicate_contact
                                .is_duplicate(
                                    address_book.contacts,
                                    first_name,
                                    last_name
                                )
                            )

                            if is_duplicate:

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


                        # ---------- INVALID ----------
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

            city = input(
                "Enter City to Search: "
            )

            search_contact.search_by_city(
                address_books,
                city
            )


        # ---------- SEARCH PERSON BY STATE ----------
        case "5":

            state = input(
                "Enter State to Search: "
            )

            search_contact.search_by_state(
                address_books,
                state
            )


        # ---------- VIEW PERSONS BY CITY ----------
        case "6":

            city = input(
                "Enter City to View Persons: "
            )

            view_contact.view_by_city(
                address_books,
                city
            )


        # ---------- VIEW PERSONS BY STATE ----------
        case "7":

            state = input(
                "Enter State to View Persons: "
            )

            view_contact.view_by_state(
                address_books,
                state
            )


        # ---------- COUNT PERSONS BY CITY ----------
        case "8":

            city = input(
                "Enter City to Count: "
            )

            count = count_contact.count_by_city(
                address_books,
                city
            )

            print(
                f"\nNumber of Persons "
                f"in {city}: {count}"
            )


        # ---------- COUNT PERSONS BY STATE ----------
        case "9":

            state = input(
                "Enter State to Count: "
            )

            count = count_contact.count_by_state(
                address_books,
                state
            )

            print(
                f"\nNumber of Persons "
                f"in {state}: {count}"
            )


        # ---------- EXIT ----------
        case "10":

            print("\nExiting Address Book...")
            break


        # ---------- INVALID MAIN CHOICE ----------
        case _:

            print(
                "\nInvalid choice. "
                "Please try again."
            )