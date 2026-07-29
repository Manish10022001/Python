#This Function returns True Provided  all elements setobj1 must present in setobj2 Otherwise returns False.

s1= {10,20,30,40}
s2= {10,20}
s3= {10,20,30,35}

print(s1.issubset(s2)) #False
print(s2.issubset(s1)) #True
print(s2.issubset(s3)) #True
print(s1.issubset(s3)) #False

#empty sets
print(set().issubset(s1)) # True: empty set is subset of s1, as s1 has value
print(set().issubset(set())) #True
print(s1.issubset(set())) #False