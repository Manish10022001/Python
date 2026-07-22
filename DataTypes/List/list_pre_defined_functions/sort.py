lst1 = [10,20,3,0,-6,100,34]
print(lst1, id(lst1))

lst1.sort()
print(lst1, id(lst1)) #ascending order

lst1.reverse()
print(lst1,id(lst1)) #descending order


lst2 = [1,2,80,30,0,0,22,-123,-3,93]
lst2.sort(reverse=True) #descending order
print(lst2, id(lst2))

lst2.sort(reverse=False) # ascending order
print(lst2, id(lst2))