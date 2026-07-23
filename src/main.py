from model.contact import Contact


print("Enter Contact Details")

first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
address = input("Enter Address: ")
city = input("Enter City: ")
state = input("Enter State: ")
zip_code = input("Enter Zip Code: ")
phone_number = input("Enter Phone Number: ")
email = input("Enter Email: ")

contact1 = Contact(
    first_name,
    last_name,
    address,
    city,
    state,
    zip_code,
    phone_number,
    email
)

contact1.display_contact()