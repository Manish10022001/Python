s1 = {10, 20, 30, 10, 20, 60, 70}
print(s1, type(s1))

fs1 = frozenset(s1)
print(fs1, type(fs1))

s2 = [1,2,"kdk"]
print(s2, type(s2))

fs2 = frozenset(s2)
print(fs2)

s3 = ("tuple",23,True,33.33)
print(s3,type(s3))

fs3 = frozenset(s3)
print(fs3)

fs4 = frozenset({"kdf","kd",33})
print(fs4)