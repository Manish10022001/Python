print(0&1) #0
print(1&0) #0
print(0&0) #0
print(1&1) #1

a=4
b=3
c=a&b
print(c) #0
print(10&15) #10
print(15&10) #10
print(30&20) #20

print(30 and 20) #20
print(20 and 30) #30


s1={10,20,30}
s2={15,20,35}
s3=s1&s2
print(s3, type(s3)) # {20} <class 'set'>

s1={"Apple","Mango", "Orange"}
s2={"Mango","Kiwi", "Banana"}
s3=s1&s2 
print(s3) #{'Mango'} <class 'set'>

s1={1.2,3.4}
s2={4.5,6.7}
s3=s1&s2
print(s3,type(s3)) #set() <class 'set'>