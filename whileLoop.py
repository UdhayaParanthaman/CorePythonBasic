i =0
while i<10:
    i += 2    # 0,2,4,6,8,10
    print(i)


numbers =[2,3,4,5,6,7]
sum=0
for i in range (0,len(numbers)):
    sum=sum+numbers[i]
print(sum)

name=["udhaya","learning"," python"]

searched_name=""
while searched_name not in name:
    searched_name=input("Please enter the existing name")
print("Are you glad to inform")

