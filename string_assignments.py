#2.length of String Name

#1.1
str1 = "Hello Python"
print(len(str1))

#1.2
def find_Len(lnstr1):
    count = 0    
    for i in lnstr1:
        count += 1
    print (count)
lnstr1 = "Sanju01"
print(find_Len(lnstr1))

#1.3
def fin_Len(lnstr2):
    counter = 0
    while lnstr2[counter]:
        counter += 1
    print (counter)

lnstr2 = "Sanju1111"
print(fin_Len(lnstr2))