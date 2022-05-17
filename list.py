#1sum of elements in list---------------------------- 

#1.1

from cgitb import small
from operator import mul


list_a = [4,5,7,9,10,12]
print(sum(list_a))

#1.2

list1 = [11, 5, 17, 18, 23,52,45,60]

def sum_List(list, size):
   if (size == 0):
     return 0
   else:
     return list[size - 1] + sum_List(list, size - 1)
  
# Drive_code    
total = sum_List(list1, len(list1))
 
print("Sum of all elements in list: ", total)

#1.3
x=[1,2,3,4,5]
sum=0
for each in range(0,len(x)):
   sum=sum+x[each]
print (sum)  

#1.4


#2Multiply of Elements in List------------------------------


#1.1

from functools import reduce
list1 = [1, 2, 3]
list2 = [3, 2, 4]
 
 
result1 = reduce((lambda x, y: x * y), list1)
result2 = reduce((lambda x, y: x * y), list2)
print(result1)
print(result2)

#1.2

def multiplyList(myList) :
     
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x
    return result
     
# code
list1 = [1, 2, 3, 5,3,]
list2 = [3, 2, 4,9,7,5]
print(multiplyList(list1))
print(multiplyList(list2))

#1.3

import math
list1 = [1, 2, 3,4]
list2 = [3, 2, 4,5]
 
 
result1 = math.prod(list1)
result2 = math.prod(list2)
print(result1)
print(result2)

#1.4


#3.Largest Numbers from List----------------------------

#1.1

ln_1 = [1,5,9,78,8,3,9]
print(max(ln_1))

#1.2

ln_2 = [14,52,78,94,5,1,3,47,98]
ln_2.sort()

print("the largest number is : ",ln_2[-1])

#1.3
# Find max list element on inputs provided by user
#giving elements, ex = 5 times
#output


list_1 = []

num = int(input("enter the numbers"))

for i in range(1, num +1):
    ele = int(input("Enter elements: "))
    list1.append(ele)
      
# print maximum element
print("Largest element is:", max(list1))


#1.4
def My_max(list1):
    max = list1[0]

    for x in list1:
        if x > max :
            max = x
    return max

list1 = [12,35,44,66,97,99,120,4,445]
print("my max number is : ", My_max(list1))


#4.Find the Smallest numbers in list--------------------------------

#1.1

list_a = [12,41,13,17,20,24,30]
list_a.sort()
print("Im the smallest", list_a[0])







list1 = [1,2,3,4,5,6]
sum(list1)

