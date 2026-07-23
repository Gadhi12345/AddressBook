class SearchContact:

    def search_by_city(self, address_books, city):

        found = False

        for book_name, address_book in address_books.items():

            for contact in address_book.contacts:

                if contact.city.lower() == city.lower():

                    print(f"\nFound in Address Book: {book_name}")
                    contact.display_contact()
                    found = True

        if not found:
            print("No contacts found in this city.")


    def search_by_state(self, address_books, state):

        found = False

        for book_name, address_book in address_books.items():

            for contact in address_book.contacts:

                if contact.state.lower() == state.lower():

                    print(f"\nFound in Address Book: {book_name}")
                    contact.display_contact()
                    found = True

        if not found:
            print("No contacts found in this state.")