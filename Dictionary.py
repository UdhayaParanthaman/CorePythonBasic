customer = {
    "name":"Udhaya",
    "email":"udhaya@gmail.com",
    "age":23,
    "age":90,
    "age":19,
    "phoneNumber":9876543212
}

print(customer['name'])
customer["name"] ='Manikandan'  # update the name from Udhaya to Manikandan
print(customer['name'])         # print updated number to the dictionary
print(customer)
print(customer.get("ages"))
print(customer.get("birthYear","2000"))