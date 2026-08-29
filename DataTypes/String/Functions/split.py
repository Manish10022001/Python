s = "Python is an oop lang"

print(s)
print(s.split())
print(len(s.split()))

x = s.split()
print(x, type(x))
print(len(x))

s = "12-09-2022"
print(s)

dob = s.split("-")
print(dob, type(dob))

print("Day", dob[0])
print("Month", dob[1])
print("Year", dob[2])

s = "Apple#Banana#kiwi/Guava"

words = s.split("#")
print(words)

words = s.split("/")
print(words)

s = "08-07-2023"

x = s.split("-")
print(x)

print("Day=", x[0])
print("Month=", x[1])
print("Year=", x[2])

s = "Apple#Mango#kiwi-Banana"

x = s.split("#")
print(x)

y = s.split("-")
print(y)

print(y[0])

y[0] = y[0].split("#")[0]
print(y)

s = "123$456$678$156$"
print(s.split("$"))

s = "123$456$678$156"
print(s.split("$"))
