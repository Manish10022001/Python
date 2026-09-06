#Program for Finding Sum of Digits of Given Number --Logic 1
num = int(input("Enter a Number:"))

sum = 0
tn = num
while(num>0):
    #get digits
    d=num%10 #here d = 8
    sum = sum+d
    num =num//10  #when it becomes 0, condition becomes false and go out of loop
else:
    print("Sum of Digits of {} = {}".format(tn, sum))