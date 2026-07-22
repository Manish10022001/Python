#extend is used for merging two lists

lst1= [10,20,40,50]
lst2= ["rs","tr","sr"]
print(lst1,id(lst1))
print(lst2, id(lst2))

lst1.extend(lst2)
print(lst1, id(lst1))

#another way is by using "+", but this will create anther memory address to store the value
lst3 = ['a', 'b', 'c', 'd']
lst4 = [1, 2, 3, 4]
print(lst3, id(lst3))
print(lst4, id(lst4))

lst3 = lst3 + lst4
print(lst3, id(lst3))