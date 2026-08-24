#Program for accepting two numerical value and decide biggest
a=float(input("Enter First Value: "))
b=float(input("Enter Second Value: "))
if(a>b):
    print("Big({},{})=>{}".format(a,b,a))
else:
    print("Big({},{})=>{}".format(a,b,b))
print("Program Execution Completed")