

firstName = input("Enter Your FirstName")
print("python" in firstName)



name= "Udhaya Kumaran"
if len(name) <3:
    print("name must be atleast 3 characters")
elif len(name) >50:
    print("name can be a maximum of 50 characters")
else:
    print("Name Looks Good")

letter = input("Please enter any letter")
if letter in name:
    print("{} is in {}".format(letter,name))
else :
    print("I don't need that letter")