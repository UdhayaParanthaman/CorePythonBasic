
# 1. from 0 to 20 print all numbers which is not divisible by either 3 or 5 ,0 not included
for i in range(1,20):
    if i%3==0 or i%5==0:
        continue
    print(i)

# 2. from 0 to 100 print all numbers which is greater than 0 and if exactly divisible by 11,print that  number is lasted.

for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break








bikes =["Duke","ktm","fz","passion"]

# for name in bikes:
#   if name != "Duke":
#      print(name)
bikes =["Duke","ktm","fz","passion"]
for name in bikes:
    if name=="ktm":
       continue #skip after every operation
    print(name)


