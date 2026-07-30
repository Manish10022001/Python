# This Function removes the common elements from setobj1 and setobj2 and Takes the Remaining Elements from Both setobj1 and setobj2 and place them in setobj1 and setobj3 contains None

s1= {10,20,30,40}
s2= {10,20,35,45}
s3= s1.symmetric_difference(s2) # {35, 40, 45, 30}
print(s3)

x = {"Python", "HTML", "Django"}
y = {"CSS", "RestAPI", "MySQL"}
z = x.symmetric_difference(y) # {'MySQL', 'HTML', 'Python', 'RestAPI', 'Django', 'CSS'}
print(z)

k={10,20,30}
v={10,20,30}
r= k.symmetric_difference(v) #set()
print(r)

s1= {10,20,30,40}
s2= {10,20,25,35}
s3=(s1.union(s2)).difference(s1.intersection(s2))
print(s3) # {40, 25, 35, 30}