#Program to find Biggest of three numbers  and check for equality
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
res = a if b<=a>c else b if a<=b>c else c if a<=c>b else "All are equal"
print("Big({},{},{})={}".format(a,b,c,res))
