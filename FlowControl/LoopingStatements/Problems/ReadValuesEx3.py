#Program which will accept list of values from keyboard and find their sum and average

nov = int(input("Enter How Many Values You want to Enter:"))
if(nov<=0):
    print("{} is Invalid Input".format(nov))
else:
    lst=[]
    for i in range(1,nov+1):
        val = float(input("Enter {} value: ".format(i)))
        lst.append(val)
    else:
        sum = sum(lst)
        avg = sum/nov

        print("List of Values = {}".format(lst))
        print("Sum of List values = {}".format(sum))
        print("Average of List Values = {}".format(avg))