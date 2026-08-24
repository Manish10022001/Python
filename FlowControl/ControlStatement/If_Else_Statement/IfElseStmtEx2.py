#Program for accepting two numerical value and decide biggest and check for equality also
a=float(input("Enter First Value: "))
b=float(input("Enter Second Value: "))
#outer if...else
if(a>b):
    print("Big({},{})=>{}".format(a,b,a))
else:
    #Inner if...else
    if(b>a):
        print("Big({},{})=>{}".format(a,b,b))
    else:
        print("Both Values are Equal")