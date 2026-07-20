lst1=[10,20,30,40,10,50,60,20,70]
print(lst1)

lst1.remove(10)
print(lst1)
lst1.remove(10)
print(lst1)
# lst1.remove(10) --ValueError: list.remove(x): x not in list

lst2 = [10, "Rossum", 53.33, 4+3j]
print(lst2)
lst2.remove(53.33)
print(lst2)
lst2.remove(4+3j)
print(lst2)


#We cannot remove values from empty list
lst3=[]
print(lst3)
# lst3.remove(100) --ValueError: list.remove(x): x not in list
#[].remove(100)     --ValueError: list.remove(x): x not in list

lst4 = list()
print(lst4)
# lst4.remove(100)    --ValueError: list.remove(x): x not in list
#list().remove("Python") --ValueError: list.remove(x): x not in list