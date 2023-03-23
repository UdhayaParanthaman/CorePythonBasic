name = input("Enter name ")

if "help" in name.lower():
    print("""
start -  to start the car
stop - to stop the car
Quit - to exit""")
elif "start" in name.lower():
    print("Car started Ready to go....")
elif "stop" in name.lower():
    print("Car stopped")
elif "quit" in name:
    print("Quit")


else:
    print("I don't understand that...")
