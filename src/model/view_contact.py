class ViewContact:

    def view_by_city(self, address_books):

        city_dictionary = {}

        for address_book in address_books.values():

            for contact in address_book.contacts:

                city = contact.city

                if city not in city_dictionary:
                    city_dictionary[city] = []

                city_dictionary[city].append(contact)

        if not city_dictionary:
            print("No contacts available.")
            return

        print("\n--- Persons Grouped By City ---")

        for city, contacts in city_dictionary.items():

            print(f"\nCity: {city}")

            for contact in contacts:
                print(
                    f"{contact.first_name} "
                    f"{contact.last_name}"
                )


    def view_by_state(self, address_books):

        state_dictionary = {}

        for address_book in address_books.values():

            for contact in address_book.contacts:

                state = contact.state

                if state not in state_dictionary:
                    state_dictionary[state] = []

                state_dictionary[state].append(contact)

        if not state_dictionary:
            print("No contacts available.")
            return

        print("\n--- Persons Grouped By State ---")

        for state, contacts in state_dictionary.items():

            print(f"\nState: {state}")

            for contact in contacts:
                print(
                    f"{contact.first_name} "
                    f"{contact.last_name}"
                )