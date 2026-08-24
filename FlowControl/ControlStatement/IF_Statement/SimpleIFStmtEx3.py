#Program for finding even and odd number and if -ve then give invalid error
n=float(input("Enter any number:"))
if(n<0):
    print("{} is Invalid Input".format(n))
if(n%2==0) and (n>0):
    print("{} is EVEN".format(n))
if(n%2!=0) and (n>0):
    print("{} is ODD".format(n))