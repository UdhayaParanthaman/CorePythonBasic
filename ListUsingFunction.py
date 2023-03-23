def my_list(number):
    print("Hello World")
    square=[]
    for i in number:
        square.append(i**2)
    return square
name=[2,4,6,8]
res=my_list(name)
print(f"Square of the list {name} are : ", res)

