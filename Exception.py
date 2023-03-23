string = "Python "
valuedError=""
try:
    for s in string:
        if s != 1:
            print(s)
except valuedError:
    print("invalid")
finally:
    print("Error Occured")


