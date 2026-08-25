#Program for accepting a Digit and display Digit Name

d = int(input("Enter a Digit:"))
if(d==0):
    print("{} is Zero".format(d))
else:
    if(d==1):
        print("{} is One".format(d))
    else:
        if(d==2):
            print("{} is Two".format(d))
        else:
            if(d==3):
                print("{} is Three".format(d))
            else:
                if(d==4):
                    print("{} is Four".format(d))
                else:
                    if(d==5):
                        print("{} is Five".format(d))
                    else:
                        print("{} is more that 5".format(d))