#Temperature Conversion Calculator

print("-"*50)
print("TEMPERATURE CONVERSION CALCULATOR")
print("-"*50)

print("\t 1.F to C")
print("\t 2.F to K")
print("\t 3.C to F")
print("\t 4.C to K")
print("\t 5.K to C")
print("\t 6.K to F")
print("\t 7.Exit")
print("-"*50)

choice = int(input("Enter Your Choice:"))

match(choice):
    case 1:
        print("Enter the temperature:")
        temp = float(input())
        print("{} Fahrenheit degrees to Celcius is {} C degrees".format(temp,((temp-32)*(5/9))))
    case 2:
        print("Enter the temperature:")
        temp = float(input())
        print("{} Fahrenheit degrees to Kelvin is {} K degrees".format(temp,((temp-32)*(5/9)+273.15)))
    case 3:
        print("Enter the temperature:")
        temp = float(input())
        print("{} Celciuas degrees to Fahrenheit is {} F degrees".format(temp,temp*(9/5)+32))
    case 4:
        print("Enter the temperature:")
        temp = float(input())
        print("{} Celcius degrees to Kelvin is {} K degrees".format(temp,temp +273.15))
    case 5:
        print("Enter the Temperature:")
        temp = float(input())
        print("{} Kelvin to Celcius is {} C degrees".format(temp, temp-273.15))
    case 6:
        print("Enter the Temperature:")
        temp = float(input())
        print("{} Kelvin to Fahrenheit is {} F degrees".format(temp, (temp-273.15)*(9/5)+32)) 
    case 7:
        print("Thank You for Using Temperature Conversion Calculator!")

    case _:
        print("Invalid Value! Please Try Again.")