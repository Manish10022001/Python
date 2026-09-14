#Program for deciding whether the number is prime or not
#logic 3
n= int(input("Enter A Number to Decide Prime or not:"))
if(n<=0):
    print("{} is Invalid Input".format(n))

else:
    res = False
    for i in range(2,n):
        if(n%i==0):
            res = True
            break

    res = "Not Prime" if res else "Prime"
    print("{} is {}".format(n, res))
    
