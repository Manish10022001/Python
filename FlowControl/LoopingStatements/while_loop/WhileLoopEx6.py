#Program for Generating Multiplication table for n where n is +ve

n = int(input("Enter a Number for generating Mul Table:"))

if(n<=0):
    print("{} is Invalid Input".format)
else:
    print("Mul Table for :{}".format(n))
    i=1
    while(i<=10):
        print("\t{} x {} = {}".format(n,i,n*i))
        i+=1
    else:
        print("="*50)