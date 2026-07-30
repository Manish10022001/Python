# This Function Takes All unique Elements of both setobj1 and setobj2 and place them setobj3

s1 = {10,20, 30, 40}
s2 = {10, 20, 35, 45}
s3 = s1.union(s2)
print(s3, type(s3))

x = {"Python", "HTML", "Django"}
y = {"CSS", "RestAPI", "MySQL"}
z = x.union(y)
print(z)

#special case
s1={10,20,30}
s2={30,40,50}
s3={13,14,15}
s4=s1.union(s2,s3) #{50, 20, 14, 40, 10, 13, 30, 15}
print(s4) 