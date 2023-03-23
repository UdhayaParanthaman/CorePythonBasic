#Sum of a element in a list
number=[11, 5, 17,18, 23]
sum=0
for num in number:
    sum=sum+num
print(sum)

sentence ="Alright, but apart from the Sanitation, the Medicine, Education, Wine, Public Order, " \
          "Irrigation, Roads, the Fresh-Water System, and Public Health, what have " \
          "the Romans ever done for us?"
for caps in sentence:
   # if(caps in("ABCDEFGHIJKLMNOPQRSTUVWXYZ")):
  if caps.isupper():
      print(caps)


for i in range(10):
    print(i)