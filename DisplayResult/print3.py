# print(Message Cum Value)  OR print(Vlalue Cum Message)

a=100
print("Val of a="+str(a))
print("Val of a=",a)
# print("Val of a="+a) TypeError: can only concatenate str (not "int") to str

a=100
b=200
c=a+b
print("Sum = ",c)
print("Sum = "+str(c))
print(c," is the sum")

print("Sum of ",a," and ",b,"=",c)
print("Sum of "+str(a)+" and "+str(b)+"="+str(c))

