#values() is used to obtain values of value and stored in variable and has class <dict_values>
d1 = {"python":1, "C":2, "C++":2, "Java":3}
print(d1, type(d1))

val = d1.values()
print(val, type(val))

for val in val:
    print(val)

for val in d1.values():
    print(val)