my_list1 = [4, 5, 6]
my_list2 = [6, 8, 9]

print(" list 1 : " + str(my_list1))
print(" list 2 : " + str(my_list2))

res_list = []
for i in range(0, len(my_list1)):
       res_list.append(my_list1[i] + my_list2[i])

print(" result list is : " + str(res_list))
