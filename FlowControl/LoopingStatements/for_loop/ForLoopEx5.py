#Program for finding the sum of Square of N Natural Numbers where N is +ve
n=int(input("Enter The Value of N for Finding its Square's Sum"))

if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    s=0 #for number
    ss=0 #for square 
    print("\tNumber\t\tSquare")
    for i in range(1,n+1):
        print("\t{} \t\t{}".format(i,i*i))
        s=s+i
        ss=ss+i**2
    else:
        print("-"*50)
        print("\t{}\t\t{}".format(s,ss))
    