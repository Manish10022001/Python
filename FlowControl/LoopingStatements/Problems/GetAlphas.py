#Program for Obtaining Only Alphabets from give line of Text/ word
#Line = "Py3th$o6n"

line = input("Enter Line or Text:")
print("Given Line:{}".format(line))
for ch in line:
    if(ch.isalpha()):
        print("{}".format(ch))
    