a = str(input("enter the charecters"))
b = a

count = sum(map(lambda x : 1 if b in x else 0, a))
print("count of given charecter :" + str(count))



