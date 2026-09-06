#Program for finding Product of N Natural Numbers where N is +ve
n = int(input("Enter the Value of N for Finding its Product:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    s=1
    for i in range(1,n+1):
        print("\t{}".format(i))
        s=s*i
    else:
        print("Product of {} Numbers={}".format(n,s))