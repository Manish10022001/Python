#copy() used to copy content of one dict obj to another dict obj(shallow copy)

d1={10:1.2, 20:2.2, 30:3.3, 40:4.4, 50:5.5}
print(d1, type(d1), id(d1))

d2 = d1.copy() #Shallow Copy
print(d2, type(d2), id(d2))

d1[40] = 4.93
d2[20] = 1.11
print(d1, type(d1), id(d1))
print(d2, type(d2), id(d2))
