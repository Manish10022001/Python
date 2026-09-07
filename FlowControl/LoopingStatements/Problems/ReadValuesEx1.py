#Program for Reading List of Values from Keyboard and Display those values
#logic - 1
nov = int(input("How many values you want to enter:"))

if(nov<=0):
    print("{} is Invalid Input".format(nov))
else:
    lst = [] #created empty list for adding the values
    for i in range(1,nov+1):
        val = float(input("Enter {} value: ".format(i)))
        lst.append(val)
    else:
        print("List of Values = {}".format(lst))