# This Function returns True Provided setobj1 contains all the Elements of setobj2. Otherwise It returns False.
s1={10, 20, 30, 40}
s2={10,20}
s3={10,20,30,35}
print(s1.issuperset(s2))
print(s2.issuperset(s3))
print(s3.issuperset(s2))
print(s1.issuperset(s3))

#empty sets
print(set().issuperset(s1)) #False
print(s1.issuperset(set())) #True
set().issuperset(set()) #True