s1 = {10, 20,40,20,10,49.20,30,60}
print(s1)
s2 = {"Python", "HTML", "CSS", 33,54.33,True}
print(s2, type(s2))

#immutable
# s2[0]=20      TypeError: 'set' object is not subscriptable
# s2[0:3]       TypeError: 'set' object is not subscriptable
s2.add("Java")  # mutable
print(s2, id(s2))


#Empty Set
s3={}
print(s3, type(s3)) # {} <class 'dict'>

s3 = set()
print(s3, type(s3)) #set() <class 'set'>
print(len(s3)) #0

#get unique values
lst = [10,20,30,40,50,10,10]
print(lst,type(lst))
s1 = set(lst)
print(s1, type(s1))
l2 = list(s1)
print(l2, type(l2))

s="MISSISSIPPI"
print(s, type(s))
s2 = set(s)
print(s2, type(s2))