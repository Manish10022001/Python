print(10>20 and 3>1) #false
print(2>3 and 4>2 and 3>2) #False
print(2>1 and 3>2 and -3>4) #False
print(2>1 and 3>2 and -3>-4) #True
print(True and 34 > 56 and 3>2 and 3>7) #False

#Special POINTS of "and": compare non zero and zero, if nonzero and nonzero then non zero(last value as result) . if zero value then it is the result
print("*"*50)
print("Special points of 'and': ")
print(100 and -100) #-100
print(100 and 0 and -100) #0
print("Python" and "HTML" and "Django") #Django
print("False" and "False" and "True" and "False") #False
print("False" and "False" and "True" and "Python") #Python