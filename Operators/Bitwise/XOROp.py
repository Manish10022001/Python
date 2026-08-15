print(1^0) #1
print(0^1) #1
print(1^1) #0
print(0^0) #0

print(2^3) #1
print(10^15) #5

s1={10,20,30}
s2={15,20,25}
s3=s1.symmetric_difference(s2)
print(s3,type(s3)) #{10, 15, 25, 30} <class 'set'>

s1={10,20,30}
s2={15,20,25}
s3=s1^s2  # Bitwise XOR Operator (^)
print(s3,type(s3)) #{10, 15, 25, 30} <class 'set'>

s1={"apple","mango","kiwi"}
s2={"Sberry","mango","guava"}
s3=s1^s2   # Bitwise XOR Operator (^)
print(s3,type(s3)) #{'guava', 'apple', 'kiwi', 'Sberry'} <class 'set'>

print({1.2,2.3,3.4}^{1.2,2.3,4.5}) #{3.4, 4.5}