#Program for accepting two numerical value and decide biggest and check for equality also

a=float(input("Enter first value: "))
b=float(input("Enter second value: "))
if(a>b):
    print("Big({},{})={}".format(a,b,a))
if(b>a):
    print("Big({},{})={}".format(a,b,b))
if(a==b):
    print("Both the values are equal")
