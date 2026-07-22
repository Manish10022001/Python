lst = [10,20,30,40,50,10,60,10,20,30]
print(lst)

print(lst.count(10))
print(lst.count(30))
print(lst.count(40))
print(lst.count(50))
print(lst.count(60))
print(lst.count(160))
print([].count(10))
print(list().count(20))

s="MISSISSIPPI"
lst = list(s)
print(lst)

print(lst.count("I"))
print(lst.count("S"))
print(lst.count("M"))
print(lst.count("D"))

#Imp
print(list("NISSON").count("S"))

print(["ABRAKADABRA"].count("A")) # output: 0, as "ABRAKADABRA" IS ONE LIST ITEM NOT SEPARATE

print(["A","B","R","A","K","A","D","A","B","A","R","A"].count("A"))

print(list(["ABRAKADABRA"][0]).count("R"))

print(["ABRAKADABRA"][0])