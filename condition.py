
#divisible by number 7 (0 to 100)
for i in range(0,101,7):
    print(i)
for i in range(101)[::7]:
    print(i)
for i in range(0,100):
    if i%7==0:
        print(i)

age = int(input("How Old are you?"))
print(age)
if age in range(0,9): #age<=0 and age<9
    print(age)