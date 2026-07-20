#1. pop(index) => index based removal

l1=[10,20,40,30,50,60]
print(l1)

l1.pop(4)
print(l1)

l1.pop(-3)
print(l1)

# [].pop(0) ----IndexError: pop from empty list
# list().pop(1)  ----IndexError: pop from empty list

#2. pop()
l2 = [10,20,30,40,50,80,390]
print(l2, id(l2))

l2.pop()
print(l2, id(l2))

l2.pop()
print(l2, id(l2))

# [].pop() ----IndexError: pop from empty list
# list().pop()  ----IndexError: pop from empty list
