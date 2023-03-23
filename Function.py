def num(num):
    print("With return statement")
    return num**2
print(num(4))

def num(num):
    print("Without return statement")
    num**2
print(num(4))

def greet(name):
    print(f'Hello Team , {name}')
    print("Task completed")
print("Welcome")
greet("Udhaya")