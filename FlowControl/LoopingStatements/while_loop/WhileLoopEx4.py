#Program for generating even numbers within n where n is +ve

n = int(input("Enter a Number in which we generate Even Numbers: "))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("Even Numbers within: {}".format(n))
    i=2
    while(i<=n):
        print("\t\t",i)
        i+=2
    else:
        print("="*50)