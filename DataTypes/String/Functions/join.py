lst = ["HYD", "BANG", "AP", "DELHI"]

print(lst, type(lst))

s = ""
print(s.join(lst))

s = " "
print(s.join(lst))

t = ("Rossum", "is", "Father", "of", "Python")

k = " "
print(k.join(t))

lst = ["apple", "mango", "kiwi", "guava"]

k = ""
k = k.join(lst)

print(k)
print(type(k))

lst = ["apple", "mango", "kiwi", "guava"]

k = " "
k = k.join(lst)

print(k)

lst = ["Python", "is", "an", "oop", "lang"]

k = " "
k = k.join(lst)

print(k)
print(type(k))

print(k.split())
