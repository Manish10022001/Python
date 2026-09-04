#Program for generating mul table for a given number
n=int(input("Enter a Number for Generating Mul Table:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    for i in range(1,11):
        print("{} x {} = {}".format(n,i,n*i))
    else:
        print("="*50)