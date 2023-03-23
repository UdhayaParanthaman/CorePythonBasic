from random import random

highest = 20
n=random.randint(1,highest)
print("Enter number between 1 and {}".format(highest))
guess = int(input())
if guess ==n:
    print("guess correctly in first time")
else:
    print("you have not found correct number")

