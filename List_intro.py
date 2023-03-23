Shoe_brand =['VKC Pride',
             'Walkaro',
             "Tiger",
             12,
             ]
Shoe_brand[3] = 67   # List is a Mutable
for Shoe in Shoe_brand:
    print(Shoe)

print(Shoe_brand[0:3])
print(Shoe_brand[-1])
print(Shoe_brand[::1])

a = [ 1, 2, "Ram", 3.50, "Rahul", 5, 6 ]
b = [ 1, 2, "Ram", 3.50, "Rahul", 5,6 ]
print(a == b)