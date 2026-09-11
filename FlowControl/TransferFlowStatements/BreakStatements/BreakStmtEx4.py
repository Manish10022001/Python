#program for displaying "miss" without indexing and slicing
#logic 1 - for loop
s="mississippi"

ni=0 #to count occurrence of i
for i in range (len(s)):
    if(s[i]=='i'):
        #increment count of i
        ni=ni+1
        if(ni==2):
            break
    print(s[i], end="")
