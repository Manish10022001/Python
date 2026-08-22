#Program to find Biggest of three numbers  and check for equality
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
res = a if a>=b and a>c else b if b>=a and b>c else c if c>=a and c>b else "All are equal"
print("Big({},{},{})={}".format(a,b,c,res))
