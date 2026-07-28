s1={10,'rs',34.22,True, 2+3j}
print(s1, type(s1), id(s1))
s1.remove(10)
print(s1, type(s1), id(s1))
s1.remove(34.22)
print(s1, type(s1), id(s1))

s1.remove(100) # KeyError: 100

s=set()
s.remove(1000) #KeyError: 1000
set().remove(12.22) # KeyError: 12.22