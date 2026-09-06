#Program for finding sum of Cubes of N natural numbers where N is +ve

n = int(input("Enter the Value of N for Finding its Cubes Sum: "))
if(n<=0):
    print("{} is Invalid Input".format(n))

else:
    s=0
    ss=0
    cs=0
    print("\tNatNums\t\tSquares\t\tCubes")
    for i in range(1,n+1):
        print("\t{}\t\t{}\t\t{}".format(i,i*i, i*i*i))
        s=s+i
        ss=ss+i**2
        cs=cs+i**3
    else:
        print("-"*50)
        print("\t{}\t\t{}\t\t{}".format(s,ss,cs))