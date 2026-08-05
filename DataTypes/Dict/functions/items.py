#items() used to obtain (key,value) from dict obj and placed in varname and whose type is <class 'dict_items'>

d1 = {"python":1, "C":2, "C++":2, "Java":3}
print(d1, type(d1))

dit = d1.items()
print(dit, type(dit))
print()
for its in dit:
    print(its, type(its))

for ks in d1.items():
    print(ks, type(ks))

for k,v in d1.items():
    print(k," ---> ",v)