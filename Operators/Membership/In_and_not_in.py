s='PYTHON'
print(s,type(s))

print("P" in s) #True
print("O" in s) #True
print("N" not in s) #False
print("P" not in s) #False
print("P" not in s) #False
print("*"*50)

s="python"
print("pyt" in s) #True
print("pyt" not in s) #False
print("pto" in s) #False
print("pon" not in s) #True
print("pyt" not in s) #True
print("noh" in s) #False
print("noh" in s[::-1]) #False
print("*"*50)

print("hon"[::-1] in s[::-1]) #True
print("pto" in s[::2]) #True
print("pto" not in s[::2][::-1]) #True
print("pto"[::-1] in s[::2]) #False
print("*"*50)

lst=[10,"Rossum", 23.45, 2+3j]
print(lst)
print("Rossum" in lst) #True
print("Ross" in lst) #False
print("Ross" not in lst) #True
print("Ross" in lst[1]) #True
print("Rossum"[::-1] not in lst[-3][::-1]) #False
print("Rossum"[::-1] in lst[-3][::-1]) #True
print("*"*50)

d={10:"Apple", 20:"Mango", 30:"Kiwi"}
print("Apple" not in d) #True
for val in d:
    print(val)

print(10 in d) #True;
print("20" in d) #False
print("20" in d.keys()) #False
print(20 in d.keys()) #True
print(d[10] not in d) #True
print(d[10][::-1] in d.get(10)) #False
print("*"*50)

print("mis" in "mississippi") #True
print("iip" in "mississippi") #False
