print(10>2 or 30>20 or 40>60) #True
print(10>20 or 4>3 or 5>6 or 6>4) #True
print(10>20 or 40>50 or 20>30) #False
print(True or 3!=3 or 4!=5 or 6!=6) #True
print(True or False or True or False) #True

print("*"*50)
#Special POINTS of "or": compare non zero and zero, if nonzero and nonzero then non zero(first value as result as it only needs one true(or nonzero)) . if zero value then it is the result

print(100 or 200) #100
print(100 or 0 or 200) #100
print(False or True or 10>20) #True
print("Python" or "Java" or "DSC") #Python