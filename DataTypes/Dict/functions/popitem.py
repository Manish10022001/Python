#popitem: removes last key,value from the dict

d1={10:1.2, 20:2.2, 30:3.3, 40:4.4, 50:5.5}
print(d1, type(d1), id(d1))

print(d1.popitem())
print(d1.popitem())
print(d1.popitem())
print(d1.popitem())
print(d1.popitem())

# print(d1.popitem())     KeyError: 'popitem():dictionary is empty 

# print({}.popitem())     KeyError: 'popitem():dictionary is empty
# print(dict().popitem()) KeyError: 'popitem():dictionary is empty
