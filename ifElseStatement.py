weight  =int(input("Enter weight"))
unit =input("Enter weight in (K)g or (L)bs:")
if "L" in unit.upper():
    print("Weights in lbs:",weight * 0.45)
elif "K" in unit.upper():
    print("Weights in kgs:",weight / 0.45)
else:
    print("Invalid")