# is -> "is" Operator returns True Provided  the Both the Objects Contains Same Memory Address  else False
# is not -> "is not " Operator returns True Provided  the Both the Objects Contains Different Memory Address else False

#None
print("-"*10+"None"+"-"*10)
a=None
b=None
print(a, id(a))
print(b, id(b))
print(a is b) #True
print(a is not b) #False
print("*"*25)

#Dict
print("-"*10+"Dict"+"-"*10)
d1={10:"Apple", 20:"Mango"}
d2={10:"Apple", 20:"Mango"}
print(d1, id(d1))
print(d2, id(d2))
print(d1 is d2) #False
print(d1 is not d2) #True
print("*"*25)

#Set
print("-"*10+"Set"+"-"*10)
s1={10,20,30,40}
s2={10,20,30,40}
print(s1, id(s1)) 
print(s2, id(s2))
print(s1 is s2) #False
print(s1 is not s2) #True
print("*"*25)

#List
print("-"*10+"List"+"-"*10)
lst1= [10,'list', 22.22]
lst2= [10,'list', 22.22]
print(lst1, id(lst1))
print(lst2, id(lst2))
print(lst1 is lst2) #False
print(lst1 is not lst2) #True
print("*"*25)

#Range: range can contain same memory address if both variable contains same elements.
print("-"*10+"Range"+"-"*10)
r1=range(10,20)
r2=range(10,20)
print(r1,id(r1))
print(r1,id(r1))
print(r1 is r2) #True
print(r1 is not r2) #False
print("*"*25)

#bytes
print("-"*10+"Bytes"+"-"*10)
b1=bytes(range(10,20))
b2=bytes(range(10,20))
print(b1,id(b1))
print(b2,id(b2))
print(b1 is b2) #False
print(b1 is not b2) #True
print("-"*25)

#String -> if same data in both string then it is in same address
print("-"*10+"String"+"-"*10)
s1="INDIA"
s2="INDIA"
print(s1,id(s1))
print(s2,id(s2))
print(s1 is s2) #True
print(s1 is not s2) #False
print()

s1="THIS"
s2="THSI"
print(s1,id(s1))
print(s2,id(s2))
print(s1 is s2)#False
print(s1 is not s2) #True
print("-"*25)

#Complex
print("-"*10+"Complex"+"-"*10)
a=2+3j
b=2+3j
print(a,id(a))
print(b,id(b))
print(a is b) #False
print(a is not b) #True
print("-"*25)

#Boolean
print("-"*10+"Boolean"+"-"*10)
a=True
b=True
print(a,id(a))
print(b,id(b))
print(a is b) #True
print(a is not b) #False
print("-"*25)

#Float
print("-"*10+"Float"+"-"*10)
a=1.23
b=1.23
print(a,id(a))
print(b,id(b))
print(a is b) #True
print(a is not b) #False
print("-"*25)

#Int
print("-"*10+"Int"+"-"*10)
a=300
b=300
print(a is b)#True
print(a is not b) #False

a=123
b=123
print(a is b) #True
print(a is not b) #False

# -1 to -5 have same memory address
a=-1
b=-1
print(a, id(a))
print(b, id(b))
print(a is b) #True
print(a is not b) #False

a=-6
b=-6
print(a,id(a))
print(b,id(b))
print(a is b) #True
print(a is not b) #False
print("-"*25)

#Special cases
print("-"*10+"Special cases"+"-"*10)
a,b=300,300
print(a,id(a))
print(b,id(b))
print(a is b) #True
print(a is not b) #False

a,b=1.2,1.2
print(a,id(a))
print(b,id(b))
print(a is b) #True
print(a is not b) #False

#only for fundamental data types memory adddrss is same in multiple assignement

lst1,lst2=[10,20],[10,20]
print(lst1,id(lst1))
print(lst2,id(lst2))
print(lst1 is lst2) #False
print(lst1 is not lst2) #True

print("-"*25)