#Program for Generating a chars from word or line of text

word = input("Enter a word OR Line of Text:")
print("Given word = {}".format(word))

i=0
while(i<len(word)):
    print("\t{}".format(word[i]))
    i+=1
print("-----------------------------")

#Reverse
i = len(word)-1
while(i>=0):
    print("\t{}".format(word[i]))
    i-=1
