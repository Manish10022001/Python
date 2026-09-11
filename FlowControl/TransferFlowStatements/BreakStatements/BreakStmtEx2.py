# program to display "pyth" without using indexing or slicing
s="python"

i=0
while(i<len(s)):
    if(s[i]=="o"):
        break
    print(s[i], end=" ")
    i=i+1