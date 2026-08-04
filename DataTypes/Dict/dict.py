d1={10:1.2, 20:2.2, 30:3.3, 40:4.4}
print(d1, type(d1))

d2 = {"python":1, "C":2, "C++":2, "Java":3}
print(d2, type(d2))

d1={10:1.2, 20:2.2, 30:3.3, 40:4.4}
print(d1[10])
print(d1[20])

d1={10:1.2,10:2.3,10:3.4,10:0.5}
print(d1) # {10: 0.5}

d2={}
print(d2, type(d1), id(d1)) #{}
d2[10]=100
d2[20]=200
print(d2,type(d2), id(d2))

d2[10]=1000
print(d2)

d2[30]="Java"  # Inserted Entry
d2[40]="HTML" # Inserted Entry
print(d2)