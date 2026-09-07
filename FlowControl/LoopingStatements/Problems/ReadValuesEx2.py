#Program for Reading List of Values from Keyboard and Display those values
#logic - 2

print("Enter Number of Values and Press @ to stop")
import sys
lst=[]
while(True):
    value=input()

    if(value=="@"):
        if(len(lst)==0):
            print("List is Empty")
        else: 
            print("Content of List= ",lst)
            sys.exit()
    else:
        lst.append(float(value))