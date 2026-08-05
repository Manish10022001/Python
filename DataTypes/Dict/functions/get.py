#get: is used to obtain value of value by passing the value of key

d1={10:1.2, 20:2.2, 30:3.3, 40:4.4, 50:5.5}
print(d1, type(d1), id(d1))

val = d1.get(10)
print(val)

val = d1.get(30)
print(val)

val = d1.get(100)
print(val) #None


#OR
print(d1[10])
print(d1[40])
# print(d1[100]) KeyError:100