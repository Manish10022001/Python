lst1 = [10,20,30,'manish',33.12];
print(lst1, type(lst1));

print(lst1[0]);
print(lst1[-1]);
print(lst1[::2]); #Slicing

lst1[1]="GUIDO"
print(lst1);

lst1[2:4]=[44.33, False];
print(lst1)

#Empty List 1
lst2 = []
print(lst2, type(lst2))
print(len(lst2))

#Empty List 2
lst3 = list();
print(lst3, type(lst3));
print(len(lst3))

s = "NISSAN"
print(s, type(s))
lst4 = list(s)
print(lst4, type(lst4))