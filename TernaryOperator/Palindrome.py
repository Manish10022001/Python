#Program for accepting a word/value and decide whether it is a Palindrome or no
value = input("Enter a value: ")
res = "PALINDROME" if value==value[::-1] else "NOT PALINDROME"
print("{} is {}".format(value,res))