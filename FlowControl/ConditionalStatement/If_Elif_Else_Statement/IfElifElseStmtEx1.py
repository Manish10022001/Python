#Program for accepting two numerical value and decide biggest and check for equality

a=float(input("Enter First Value: "))
b=float(input("Enter Second Value: "))
if(a>b):
    print("Big({},{})=>{}".format(a,b,a))
elif(b>a):
    print("Big({},{})=>{}".format(a,b,b))
else:
    print("All Values are Equal")
    