#Program for Obtaining only Special Symbols from given line of text or word

line = input("Enter Line or Text:")
nosp=0
print("Given Line=",line)
for ch in line:
    if(not ch.isalnum()):
        nosp = nosp+1
        print("{}".format(ch))
else:
    print("Number of Special Symbols=",nosp)