# approach to get index values of same values appearing multiple times

lst = [10,20,10,30,10,50,20,60]
for i,v in enumerate(lst):
    print(i,"--->",v)


for x,y in enumerate(lst):
    if(y == 10):
        print(x,"---->",y)

for x,y in enumerate(lst):
    if(y==20):
        print(x,"--->",y)

s="MISSISSIPPI"
for index,value in enumerate(s):
    if(value == "S"):
        print(index, "---> ", value)