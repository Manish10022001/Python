#Prgram to find Biggest of two numbers  and check for equality
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
res =a if a>b else b if b>a else "equal" #Nested ternary Operator

print("Big({},{})={}".format(a,b,res))