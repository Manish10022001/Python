t1 = (10,20,30,10,40,20,-23,2.2)
print(t1)
t2 = (10,'rs',343.3,True, 'NL')
print(t2)

t3 = 10,'tr',234,333,False,'PL'
print(t3, type(t3))

t4=(10)
print(t4, type(t4)) # 10 <class 'int'>
t4 = (10,)
print(t4, type(t4)) # (10,) <class 'tuple'>
t4 = 10,
print(t4, type(t4)) # (10,) <class 'tuple'>

t1 = (10,20,30,10,40,20,-23,2.2)
print(t1[0])
print(t1[-1])
print(t1[2])
print(t1[2:])
print(t1[::2])
print(t1[::-1])

print(t1,type(t1), id(t1))
#t1[0] =23   TypeError: 'tuple' object does not support item assignment---IMMUTABLE

#to make changes, need to convert it to list and then make changes
s="MISSISSIPPI"
print(s, type(s))
t= tuple(s)
print(t, type(t))

l1= [10,30,20,40]
print(l1, type(l1))
t1 = tuple(l1)
print(t1, type(t1))
t1 = tuple(range(10,20,2))
print(t1)