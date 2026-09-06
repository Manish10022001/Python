#Program for finding Factorial of Number
n = int(input("Enter the Value of N for Finding Its Factorial:"))

if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    fact=1
    for i in range(1,n+1):
        print("\t{}".format(i))
        fact=fact*i
    else:
        print("Factorial({})={}".format(n,fact))
