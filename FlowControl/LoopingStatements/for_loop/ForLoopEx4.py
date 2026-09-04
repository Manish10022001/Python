#Program for Finding Sum of N Natural Numbers where N is +ve
n=int(input("Enter The Value of N for finding its Sum:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    s=0
    for i in range (1,n+1):
       print("\t",i)
       s=s+i
    else:
        print("Sum of {} Numbers = {}".format(n,s))