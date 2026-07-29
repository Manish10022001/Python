# This Function returns True provided Both sets are not containing Common Elements
# This Function returns False provided Both sets are containing at least one Common Element(s)
s1 = {10,20,40,30}
s2 = {15,25,35}
s3 = {15,10,56}

print(s1.isdisjoint(s2)) #True: no common elements
print(s1.isdisjoint(s3)) #false: at least one common element
print(s2.isdisjoint(s3))
print(s2.isdisjoint(s1)) 

#with empty sets
s3= set()
s4 = set()
print(s3.isdisjoint(s4)) # True : as both are empty nothing to compare
print(set().isdisjoint(set())) #True
print(set().isdisjoint({10,20,10})) # True
