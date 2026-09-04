#Program for generation 1 to n Numbers where n is +ve
n=int(input("Enter How Many Numbers you want to generate:"))
if(n<=0):
    print("{} is Invalid Value")
else:
    for i in range(n,0, -1):
        print("\t",i)
