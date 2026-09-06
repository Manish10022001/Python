#Program for obtaining only Digits from given line of Text/Word

line = input("Enter Line of Text:")

print("Given Line:{}".format(line))

for d in line:
    if(d.isdigit()):
        print("{}".format(d))