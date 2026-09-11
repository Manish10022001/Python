#program for displaying "miss" without indexing and slicing
#logic 1 - while loop
s="mississippi"

ni=0 #to count occurrence of i
i=0
while(i<len(s)):
    if(s[i]=='i'):
        #increment count of i
        ni=ni+1
        if(ni==2):
            break
    print(s[i], end="")
    i=i+1 #increment index