from model.contact import Contact
from model.add_contact import AddContact


address_book = AddContact()

print("Enter Contact Details")

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

print("\nContacts in Address Book:")
address_book.display_contacts()

print("\n--- Edit Contact ---")

name = input("Enter First Name of Contact to Edit: ")

address_book.edit_contact(name)

print("\nUpdated Contact Details:")
address_book.display_contacts()