num = (1,2,3,4,5,3)
print(num)
print(num[5])

print(num.index(4))
tuple_name =1,2,'Python',[11,78],'Udhaya'
print(tuple_name)

print('x'* 5)

num = (1,2,3,4,5,3,9,3)
print(num.count(3))

coordinates =(1,2,5)
x,y,z = coordinates
print(x*y*z)

listCoordinates =[1,2,3]
x,y,z = listCoordinates
print(y)

Tuple_data = (0, 1, 2, 3, 1, 3, 1, 3, 12)
# getting the index of 3
res = Tuple_data.index(3)
print('First occurrence of 1 is', res)


# getting the index of 3 after 4th
# index
res1 = Tuple_data.index(3,4)
print('First occurrence of 1 after 4th index is:', res1)

