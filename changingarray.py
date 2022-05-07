list_of_lists = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
print(list_of_lists)
new1 = [[row[i] for row in list_of_lists] for i in range(len(list_of_lists[0]))]

print(new1)

