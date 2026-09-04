#Program for generating odd numbers within n

n = int(input("Enter how many numbers you want to generate within range:"))
if(n>=0):
    print("Odd numbers withing 1 to {} : ".format(n))
    i=1
    while(i<=n):
        print("\t\t{}".format(i))
        i+=2
    else:
        print("-")

else:
    print("{} is Invalid Input".format())