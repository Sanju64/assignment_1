

#using while loop------------------------

list1 = [1,2,3,4,5,6]

list2 =len(list1)

i = 0

while i < list2:
    print(i)
    i+=1

#1.2 using for loop----------------------

list1 = [2,4,6,7,8,10]

for i in list1:
    print(i)
    i+=1

#disply only even  numbers-------------------

list_even = [2,44,3,12,41,47,33,30,6,8,10]

for each in list_even:
    if (each) %2 == 0:
        print(each)

#Disply elements by index wise------------------

list_index = [2,3,-4,6,-2,1,-7,4]

for each in list_index:
    if each >0:
        print("+Ve number", each)
    else:
        print("-ve number",each)


#Information about list (len),(count),(index), Function-------------------



list1 = [1,2,4,5,4,6,8,9,10,4,23,5]

x = list1.count(4)
print("The lenght of the list is",len(list1))
print("count of charecters is",x)
print("Index of the charecter is ",list1.index(4))


#append Method----------

list1 = [5,4,6,8,9,10,4,23,5]

list1.append(22)
print(list1)

  
#insert Method---------------

list1 = [5,4,6,8,9,10,4,23,5]

print(list1)
list1.insert(5,-11)
print(list1)

#Difference Between append and insert--------

#1.append will add the element at the end of the list(Which one items you add in the element it's directly goes to the last of the list)
#Vs
#1.Specially we use "Insert Method" for targeting the items in list, it needs two arguments to pass the values(one is the 
#   indexing where to insert the item, other one is which items we going to add) ex :--- name.insert(2,22) 


#extend-----------------------

#extend method adds all the elements of an iterable (list,tuple,string) to the end of the list.

list1 = [1,4,5]
list2 = [2,6,5,7]

list2.extend(list1)

print("after the Extend method",list2)


#remove-------------------------------

#Remove() method Removes the first matching element from the list

list1 = [1,4,5,2,6,4,7,6]

list1.remove(6)
print(list1)

#pop()--------------------
#pop() method will removes the given index from the list and returns the  removed item

list1 = [1,4,5,2,6,4,7,6]
list1.pop(1)
print(list1)

#Difference Bitween remove() Vs pop()---------------------
#remove() removes the perticular or first matching element 
#Vs
#pop() removes the value by indexing 


#Ordering elements of the List
#Reverse():----------------------------------------

#reverse() It reverse the Sequance of a list 

list1 = [1,4,5,2,6,7,6]
list1.reverse()
print(list1)


#sort()---------------------------------

#sort() method sorts the items of a list in ascending or descending order.

list1 = [1,4,5,2,6,7,6]
list1.sort()
print(list1)


#Aliasing and Cloning of List objects:----------------------------
c = [21,23,20]
d = [21,23,20]

#1
print(c == d) #true
print(c is d) # false

#2
c == d
print(c == d) #true
print(c is d) #true




#By using Slice Operator---------------------------------------

#The slice() method can be used with string, list, tuple, set, bytes, or range.
#slicing is taking part of the statement
#example1
list_b = (1,2,6,7,3,4,5,6,8,9,10)
x = slice(4)
print(list_b[x])

#example 2
list_b = (1,2,6,7,3,4,5,6,8,9,10)
x = slice(4,6)
print(list_b[x])


#copy()------------------------------------
#the copy() method return a shallow copy of the list,
#The copy() method returns a new list. It doesn't modify the original list.

my_list = ['cow','bird',4,78,6.1]
new_list = my_list.copy()
print("this is new copy",new_list)


#Nested list as Matrix-------------------------
#for Get 2D or 3D Dimensional Array we have to Import Numpy library(it will helps us to work with the array)

import numpy as np

my_matrix= np.array([[10,20,30],[40,50,60],[70,80,90]])
print(my_matrix)


#nested array( matrix )using for loop-----------


#list Comprehesions----------------------

list1 = "the quick brown fox jumps over the lazy dog"

new_list = [[[word, len(word)] for word in  list1.split() ]]

print(new_list)

#Write a Python program to convert a given list of tuples to a list of lists.-------------

tupl1 = [(1,2),(2,3),(3,4)]

print([list(new1) for new1 in tupl1])

#finding Common items from two lists

list1 = [10,15,45,11,33,77,14,12,17]
list2 = [11,22,10,33,144,14,46,0.7,]

print([x for x in list1 if x in list2])

#Replace the last element in a list with another list-----------------------

list1 = [10,15,45,11,33,77]
list2 = (11,22,10,33,144,14,46)

list1.extend(list2)
print(list1)



#Tuple -----------------------------------
# Accessing elements of tuple:
# 	1. By using index:
# 	2. By using slice operator:
# Mathematical operators for tuple:
# 	+ and * operators for tuple

tup1 = (1,2,44,3,4,12,11,10)
#indexing
print(tup1[2])
#slicing
print(tup1[1:5])

#addition
tup1 = (1,2,44,3,4,12,11,10)
print(sum(tup1))

#multiplication
tup1 = [(2,4),(5,6),(7,9),(10,50)]

x = [(a*b) for a,b in tup1]
print(x)

#.Write a Python program to check if a specified element presents in a tuple of tuples.-------------------------









#.Write a Python program to convert a given tuple of positive integers into an integer-------------------------------

