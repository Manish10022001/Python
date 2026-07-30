# This Function removes the common elements from setobj1 and setobj2 and Takes the Remaining Elements from setobj1 and place them in setobj3
s1 = {10,20,30,40}
s2 = {10,20,35,45}
s3 = s1.difference(s2) # {30,40}
print(s3)
s4 = s2.difference(s1) # {35,45}
print(s4)

x = {"Python", "HTML", "Django"}
y = {"CSS", "RestAPI", "MySQL"}
z= x.difference(y) # {'Django', 'HTML', 'Python'}
print(z) 
z = y.difference(x) # {'CSS', 'RestAPI', 'MySQL'}
print(z)

k={10,20,30}
v={10,20,30}
r=k.difference(v) #empty set(set()) as there is no difference
print(r)