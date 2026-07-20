l1=[10,20,30,40,10,20,60,70]
print(l1, id(l1))
print(len(l1))

l1.clear()
print(l1, id(l1))
print(len(l1))

print(l1.clear()) #none
print([].clear()) #none
print(list().clear()) #none