d1={10:1.2, 20:2.2, 30:3.3, 40:4.4, 50:5.5}
print(d1, type(d1), id(d1))

# d1.pop(key)
print(d1.pop(10))
print(d1, type(d1), id(d1))

print(d1.pop(30))
print(d1, type(d1), id(d1))

print(d1.pop(50))
print(d1, type(d1), id(d1))


# {}.pop(20)    KeyError:20
# dict().pop(20) KeyError:20