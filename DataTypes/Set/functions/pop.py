s1={10,'rs',22.22,True, 1+11.1j} # No order of Display
print(s1.pop()) #True
print(s1.pop()) #1+11.1j
print(s1.pop()) #rs
print(s1.pop()) #22.22
print(s1.pop()) #10
#print(s1.pop()) #Key Error: pop from empty set
#print(set().pop()) #Key Error: pop from empty set

s2={10,20,30,40,50,10,20} #Order of Display Given
print(s2, type(s2), id(s2))
s2.pop() #50
s2.pop() #20
s2.pop() #40
s2.pop() #10
s2.pop() #30
print(s2, type(s2), id(s2))

print(s2.pop()) # KeyError: 'pop from an empty set'