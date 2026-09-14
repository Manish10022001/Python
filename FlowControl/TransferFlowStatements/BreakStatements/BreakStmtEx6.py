#Program for deciding whether the number is prime or not
#logic 2
n= int(input("Enter A Number to Decide Prime or not:"))
if(n<=0):
    print("{} is Invalid Input".format(n))

else:
    res = False
    for i in range(2,n):
        if(n%i==0):
            res = True
            break
    if(res):
        print("{} is Not Prime".format(n))
    else:
        print("{} is Prime".format(n))
