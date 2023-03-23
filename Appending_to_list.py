current_list = "_"
current_parts = []
while current_list!='0':
    if current_list in "123456":
        print("Adding {}".format(current_list))
        if current_list == "1":
            current_parts.append("computer")
        elif current_list == "2":
         current_parts.append("Monitor")
        elif current_list == "3":
         current_parts.append("Mouse")
        elif current_list == "4":
         current_parts.append("Keyboard")
        elif current_list == "5":
         current_parts.append("Mouse mat")
        elif current_list == "6":
            current_parts.append("Hdmi cable")
    else:
        print("Please add options from the list below")
        print("1: Computer")
        print("2: Monitor")
        print("3: Mouse")
        print("4: Keyboard")
        print("5: Mouse mat")
        print("6: Hdmi cable")
        print("0: to finish")
    current_list = input()

print(current_parts)
