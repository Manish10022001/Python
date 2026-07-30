s1 = {10, 20 ,30, 40}
s2 = {10, 20, 35, 45}
s3 = s1.intersection(s2)
print(s3)

x = {"Python", "HTML", "Django"}
y = {"CSS", "RestAPI", "MySQL"}
z = x.intersection(y) # set() empty set
print(z) 

#special case
s1={10,20,30}
s2={30,40,50}
s3={13,14,15}
s4=s1.intersection(s2,s3)
print(s4) #set() as s1.intersecton(s2)= {10,20}.intersection(s3) => empty set()