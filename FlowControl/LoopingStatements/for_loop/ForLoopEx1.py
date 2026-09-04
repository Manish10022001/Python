#Program for generation 1 to n Numbers where n is +ve
n = int(input("Enter How Many Numbers you want to generate:"))
if(n<=0):
    print("{} is Invalid Value".format(n))
else:
    print("Numbers within {}".format(n))
    for i in range(1, n+1):
        print("\t",i)