message =input(">")
words=message.split()
emoji ={
    ":)": "😄",
    ":(": "🥱"
}
output=""
for msg in words:
    output+=emoji.get(msg,msg)+" "
print(output)
