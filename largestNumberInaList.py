number = [2,8,100,37,32,89,12,6]

max_number=number[0]
for numbers in number:
    if numbers>max_number:
        max_number=numbers
print(max_number)

print("Largest Number in a list:",max(number))