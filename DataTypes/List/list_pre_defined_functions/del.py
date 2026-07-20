l1=[10,20,30,40,10,20,60,70]
print(l1, id(l1))

del l1[4]
print(l1, id(l1))

del l1[-3]
print(l1, id(l1))

del l1[1:4]
print(l1, id(l1))

l1=[10,20,30,40,10,20,60,70]
print(l1,id(l1))

del l1[::2]
print(l1, id(l1))

del l1  # deletes whole list, do not even keep empty list
# print(l1, id(l1)) -- NameError: name 'l1' is not defined