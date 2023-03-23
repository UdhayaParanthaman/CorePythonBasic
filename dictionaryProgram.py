digits =input(">")
num = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five"
}
output=""
for ch in digits:
    output+=num.get(ch,"!")
print(output)