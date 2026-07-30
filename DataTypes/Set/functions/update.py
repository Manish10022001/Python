# This Function is used for Merging OR Adding the Elements of setobj2 to setobj1

s1= {10,20,30,40}
s2= {10,20,25,35}
s3= s1.update(s2) # it is like union but instead of storing in s3, it will store in s1 only
print(s1) # {35, 40, 10, 20, 25, 30}
print(s3) # None

x={10,20}
y={10,20}
x.update(y)
print(x) # {10, 20}

s1=set()
s1.update({10,20,20,'A'})
print(s1) # {'A', 10, 20}