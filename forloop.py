vars = [12,87,29,32]
res=0
for num in vars:
    res+=num
print(f'{res}')

# adding one element to the list


my_list = [3, 5, 6, 8, 4,7]
my_list.append(8)
print("adding one element to the list:",my_list)

# adding one list to another list
var = [12,76,19]
var2 =[23,87]
var.append(var2)
print("adding one list to another list:",var)





values =input("Please enter any characters")
separator = ""

for val in values:
    if not val.isnumeric():
        separator =  val

print(separator)
n=random.randint(0,11)
print(n)
vars = [12,87,29,32]
for num in vars:
    print(num)
    if(num == 29):
        print(num)
    break

for i in range(0,9,3):
    print(i)






