#Program for generating odd numbers within n in reverse order where n is +ve

n=int(input("Enter a Number in which we generate Odd Numbers:"))

if(n<=0):
    print("{} is Invalid Number".format(n))
else:
    print("Odd Numbers within : {}".format(n))

    i=n-1 if(n%2==0) else n
    while(i>=1):
        print("\t\t",i)
        i-=2
    else:
        print("-"*50)