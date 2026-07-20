lst1 = [10,"RS", 34.44]
print(lst1, id(lst1))

lst1.append("Python")
print(lst1, id(lst1))

lst1.append(1.2)
print(lst1, type(lst1))


lst2=[];
print(lst2, type(lst2))
lst2.append(100)
print(lst2, type(lst2))
lst2.append(23.11)
print(lst2, type(lst2))
lst2.append("Python")
print(lst2, type(lst2))