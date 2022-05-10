#0.1Write a Function to take number as input and print its square value

def squarval(x):
    return x**2

xy = int(input("Enter the Number : "))
print("The Squareroot of", xy, "is", squarval(xy))


#0.2

def sum_two(x,y):
    return x+y

x = int(input("X = "))
y = int(input("Y = "))

print("Sum ", x , "and", y, "is", sum_two(x,y))

#0.3return sum,sub

def add_sub(x,y):
    return x+y, x-y

x = int(input("x = "))
y = int(input("y = "))
print(add_sub(x,y))


#1 table of given number 

def print_table(num):

    for i in range(1,11):
        print(num, 'x',i,'=', num*i)

n = int(input("enter the number"))

print_table(n)



#2.Sum all Numbers in list,tuple,set

#2.1 sum all the numbers in a list
list1 = [11, 50, 13, 20, 23]

def sum_List(l,s):
   if (s == 0):
    return 0
   else:
     return l[s - 1] + sum_List(l, s - 1)
   
total = sum_List(list1, len(list1))
 
print("Sum of all elements in given list: ",total)

#2.2 sum all the numbers in a Tuple

l1 = [(1, 16), (13, 40), (50, 8)]
print ("The original list is : " + str(l1))
res = [sum(i) for i in zip(*l1)]
print ("The position summation of tuples  : " + str(res))


#3mutiply all the numbers in list,tuple,set

#3.1
def mult(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(mult([8, 2, 13, 10, 7]))


#3.2 numbers in tupple
def multi_tup(nums):
    temp = list(nums)
    product = 1 
    for x in temp:
        product *= x
    return product

nums = (12, 31, 14 ,10,8)
print ("The Original Tuple: ")
print(nums)
print("The Product of given tuple is :",multi_tup(nums))


#4 Accepts a string and calculate the number of upper-case letters and lower case 

str2=str(input("Enter string:"))
def stringCount(s):
    a={"Upper":0, "Lower":0}
    for c in s:
        if c.isupper():
            a["Upper"]+=1
        elif c.islower():
            a["Lower"]+=1
    else:
        pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", a["Upper"])
    print ("No. of Lower case Characters : ", a["Lower"])

stringCount(str2)


#6.Pascals'tringle

def tringle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,1)):
      print('' ,trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
tringle(10) 

 
#7 Function to check wheather a string is a palindrone or not

str_name=str(input("Enter the input string : "))
def isPalindrome(str_name):
    return str_name == str_name[::-1]
 
temp =isPalindrome(str_name)
if temp:
    print("Yes")
else:
    print("No")




#8.check whether number is in a given range
 
def test_range(n):
    if n in range(3,20):
        print( " %s is in the range"%str(n))
    else :
        print("outside the range.")
test_range(10)




