print(0|1) #1
print(1|0) #1
print(0|0) #0
print(1|1) #1

#Example 2
a=4 #0100
b=3 #0011
c=a|b #0111
print(c) #7

a=5
b=4
c=a|b
print(c)
print(10|15) #15
print(15|10) #15
print(30|20) #30
print(20|30) #30

#Example-3
s1={10,20,30}
s2={15,20,35}
s3=s1|s2
print(s3)

s1={"Apple","Mango"}
s2={"Mango","Kiwi"}
s3=s1|s2 # # Bitwise OR Operator (|)

s1={1.2,3.4}
s2={4.5,6.7}
s3=s1|s2
print(s3,type(s3)) #{1.2,3.4,4.5,6.7}  <class 'set'>
