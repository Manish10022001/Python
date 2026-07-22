lst = [10,20,14,29,40]
print(lst, id(lst))

lst1 = lst.reverse()
print(lst, id(lst))

print(lst1) # None as it is not storing in new variable

lst1= ["python", "java", "HTML", "C"]
print(lst1, id(lst1))
lst1.reverse()
print(lst1, id(lst1))