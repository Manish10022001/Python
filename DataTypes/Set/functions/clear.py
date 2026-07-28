s1 = {10, 'rs', 33.33, True}
print(s1, type(s1), id(s1))

s1.clear()
print(s1)

s1.clear() 
print(s1.clear()) #None
print(set().clear())