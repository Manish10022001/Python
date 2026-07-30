# This Function removes the common elements from setobj1 and setobj2 and Takes the Remaining Elements from Both 
s1={10,20,30,40}
s2={10,20,25,35}
s1.symmetric_difference_update(s2)
print(s1)