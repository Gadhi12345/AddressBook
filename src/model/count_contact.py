class CountContact:

    def count_by_city(self, address_books, city):

        count = 0

        for book_name, address_book in address_books.items():

            for contact in address_book.contacts:

                if contact.city.lower() == city.lower():
                    count += 1

        return count


    def count_by_state(self, address_books, state):

        count = 0

        for book_name, address_book in address_books.items():

            for contact in address_book.contacts:

                if contact.state.lower() == state.lower():
                    count += 1

        return count