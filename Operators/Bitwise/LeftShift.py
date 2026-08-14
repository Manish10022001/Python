#LeftShift = Given Number * 2**bits number

a=10    #given number
b=3     #no. of bits
c=a<<b # 10 * 2**3 => 10*8 => 80
print(c) #80

print(4<<3) #32
print(9<<2) #36
print(10<<0) #10
#print(10.3<<2) #TypeError: unsupported operand type(s) for <<: 'float' and 'int'