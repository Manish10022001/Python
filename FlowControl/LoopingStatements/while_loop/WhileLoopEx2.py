#Program for Generating n to 1 numbers where n is +ve
n=int(input("Enter How Many Numbers u want to Generate in backward Direction:"))

if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    i=n 
    while(i>=1):
        print("\t{}".format(i))
        i-=1 #short hand for -(minus) operator
    else:
        print("{} is from else part of while loop")
    print("Out of while loop -other statements")
print("Program Execution Completed")