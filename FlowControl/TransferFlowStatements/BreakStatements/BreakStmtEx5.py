#Program for deciding whether the number is prime or not
#logic 1
n= int(input("Enter A Number to Decide Prime or not:"))
if(n<=0):
    print("{} is Invalid Input".format(n))

else:
    # for i in range(2,n): wrong
    #     if(n%i==0):
    #         print("Not a Prime Number")
    #         break
    # print("Prime Number")
    res="Prime"
    for i in range(2,n):
        if(n%i==0):
            res="Not Prime"
            break
    print("{} is {}".format(i,res))