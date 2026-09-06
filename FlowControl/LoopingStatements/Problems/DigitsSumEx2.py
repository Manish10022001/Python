#Program for Finding Sum of Digits of Given Number --Logic 2
num = input("Enter a Number:")

sum = 0
for d in num: #each character
    sum = sum + int(d)
else:
    print("Sum of Digits of {} = {}".format(num,sum))

