lst1 = [10,20,'rs','python']
print(lst1, id(lst1))

lst2 = lst1.copy()
print(lst2, id(lst2))

lst1.append("HI")
print(lst1,id(lst1))
print(lst2,id(lst2))

lst2.insert(1,"second")
print(lst2, id(lst2))
print(lst1, id(lst1))