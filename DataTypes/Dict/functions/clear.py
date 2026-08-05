d1={10:1.2, 20:2.2, 30:3.3, 40:4.4}
print(d1, type(d1), id(d1))
print(len(d1))

d1.clear()
print(d1, type(d1), id(d1)) #{}
print(len(d1))  #0

#dict is empty, if call clear again, it will return none
print(d1.clear()) #None
print({}.clear()) #None
print(dict().clear()) #None