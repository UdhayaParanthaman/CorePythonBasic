num = int(input("Enter number"))
flag=False
if num ==1:
    print("neither and nor a prime number")
elif(num > 1):
    for i in range(2,num):
        if(num % i ==0):
            flag =True
if flag==True:
    print("Not a Prime Number")
else:
    print(num," is a Prime Number")

