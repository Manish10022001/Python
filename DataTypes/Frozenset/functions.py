fs1 = frozenset({10,20,40,20,40})
print(fs1, id(fs1))
fs2 = fs1.copy() #deep copy, it is shallow but only exception is frozen set.
print(fs2, id(fs2))

fs1 = frozenset({10,20,30,10,20,40,60,50,70})
fs2 = frozenset({10,20,30})
fs3 = frozenset({10,2,4})

print(fs1.issuperset(fs2))  #True
print(fs2.issuperset(fs1))  #False
print(fs2.issubset(fs1))    #True
print(fs1.issubset(fs2))    #False

print(fs1.isdisjoint(fs2))  #False
print(fs1.isdisjoint(fs3))  #False

print(fs1.union(fs2))       #frozenset({70, 40, 10, 50, 20, 60, 30})

print(fs1.intersection(fs2))#frozenset({10, 20, 30})

print(fs1.difference(fs2))  #frozenset({40, 50, 60, 70})

print(frozenset({10,20,30,40}).symmetric_difference([10,20,50,60])) # frozenset({40, 50, 60, 30})