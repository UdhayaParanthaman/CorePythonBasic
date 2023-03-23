number = [1,9,1,9,2,3,8,3,4]
number_unique=[]
for numbers in number:
    if numbers not in number_unique:
        number_unique.append(numbers)
print(number_unique)