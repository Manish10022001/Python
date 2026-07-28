# To remove the element we can use either remove or discard. if we want response with error use remove, response without error use discard

s1={10,True,44.44,"Python"}
print(s1, type(s1), id(s1))

s1.discard(10)
print(s1)

s1.discard(True)
print(s1)

s1.discard(100) #will not give keyError
# s1.remove(100) #Keyerror:100


set().discard(100)
print(set().discard(100)) #None

set().remove(100) #KeyError: 100