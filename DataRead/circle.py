#write a python program which will calculate area of circle
radius = float(input("Enter the radius of circle: "))
area = 3.14 * radius * radius
print("The area of circle is {}".format(area))

print("-----------OR-----------")
print("The area of circle = %0.2f" %area)

print("-----------OR-----------")
print("The area of circle = {}".format(round(area)))