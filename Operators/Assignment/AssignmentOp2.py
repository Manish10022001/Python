#Program for swapping/interchanging of two values
#Logic-1
a,b=input("Enter value of a: "),input("Enter value of b: ")

print("*"*50)
print("\tOriginal value of a:{}".format(a))
print("\tOriginal value of b:{}".format(b))
print("*"*50)

#Swapping logic
x=a #Here  x is Temp Variable
a=b
b=x
print("*"*50)
print("\tSwapped value of a:{}".format(a))
print("\tSwapped value of b:{}".format(b))
print("*"*50)