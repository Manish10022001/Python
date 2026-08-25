#Program deciding whether the value is Palindrome or Not
n = input("Enter a value: ").lower()
if(n==n[::-1]):
    print("{} is Palindrome".format(n))
if(n!=n[::-1]):
    print("{} is Not Palindrome".format(n))