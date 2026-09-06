#Program for Obtaining only Special Symbols without spaces from given line of text or word

line = input("Enter Line or Text:")
nosp=0
print("Given Line=",line)

words = line.split()

for word in words:
    for ch in word:
        if(not ch.isalnum()):
            print("{}".format(ch))
            nosp = nosp+1
else:
    print("Number of Special Symbols=",nosp)