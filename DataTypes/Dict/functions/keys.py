#keys: used to object value of key and class type is <dict_keys>

d1 = {"python":1, "C":2, "C++":2, "Java":3}
print(d1, type(d1))

ks = d1.keys()
print(ks, type(ks))

for k in ks:
    print(k)

for k in d1.keys():
    print(k)