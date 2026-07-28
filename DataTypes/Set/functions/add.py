s1= {10,'rs',23.21}
print(s1,type(s1))

s1.add('Python')
print(s1, type(s1))

s1.add("NL")
print(s1, type(s1))

s1.add(True)
print(s1, type(s1))

s2=set()
print(s2, type(s2))
s2.add(100)
s2.add("MS")
s2.add(True)
s2.add(2+1.1j)
print(s2, type(s2))