lst = [10,'rs', [15,16,17], [88,99,20],'Python']
print(lst)

for val in lst:
    print(val, type(val), type(lst))


print(lst[2])

print(lst[-2])

print(lst[2][::2])
print(lst[2][-2])
print(lst[-2][-2])

lst[-3].append(14)
print(lst)

lst[-2].insert(-2, 43)
print(lst)

lst[2].sort()
print(lst)

lst[-2].sort(reverse=True)
print(lst)

del lst[2][1::2]
print(lst, type(lst))

lst[3].clear()
print(lst)

lst[-2].append(67)
print(lst)