# 2. Shallow Copy

lst1 = [1,2,3,4]
lst2 = lst1.copy()
lst2[1] = 5000
print(lst2, lst1)

#### Shallow copy with respect to Nested List####
lst1 = [[1,2,3,4],[4,5,6,7]]
lst2 = lst1.copy()
print(lst1)

print(lst2)

lst2[1][2] = 9999

print(lst1)

print(lst2)

lst1.append([2,3,4,5])

print(lst1)

print(lst2)