class DuplicateContact:

    def is_duplicate(self, contacts, first_name, last_name):

        for contact in contacts:

            if (
                contact.first_name.lower() == first_name.lower()
                and contact.last_name.lower() == last_name.lower()
            ):
                return True

        return False