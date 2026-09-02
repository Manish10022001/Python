#Program for Generating 1 to n numbers where n is +ve
n = int(input("Enter how many numbers you want to generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    i=1 #Initialization
    while(i<=n):
        print("\t{}".format(i))
        i=i+1
    print("Other statements in while loop")
print("Program Execution Completed")