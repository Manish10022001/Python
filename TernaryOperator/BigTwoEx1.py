#Prgram to find Biggest of two numbers 
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
bv = a if a>b else b
print("Big({},{})={}".format(a,b,bv))