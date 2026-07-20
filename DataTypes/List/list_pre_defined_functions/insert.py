lst = [10,'rs', 34.33]
print(lst)
lst.insert(2,'python')
print(lst)
lst.insert(1,'Guido')
print(lst)

lst1 = [10, 'rs', 34.56]
lst1.insert(-1, 'NL')
print(lst1)
lst1.insert(-2, 'python')
print(lst1)


lst1.insert(100, 'Hundred')
print(lst1)
lst1.insert(-100, "negative")
print(lst1)