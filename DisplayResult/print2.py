#print(msg)

print("Hello Python")
print('Hello Python')
print(''' Hello Python ''')
print("Hello", "Python")
print("Hello", 'python')
print("Hello"+"Python")
print("Hello"+" "+"Python")

#print("Hello"+3) TypeError: can only concatenate str (not "int") to str
print("Hello"+str(3))
#print("python"+3.12) TypeError: can only concatenate str (not "float") to str
print("Hello"+str(3.12))
print(10+12)
print("10"+"12")
print(str(10)+str(20))