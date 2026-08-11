#Program for demonstrating Square root of given number without using sqrt() method

n = float(input("Enter a number : "))
res = n**0.5  # or n**(1/2)
              # for cube root: n**(1/3)
print("Square Root of {} = {}".format(n,res))