# a = int(input("Enter the number"))

# def sanju(a):

#     if a %2 ==0:
#         print("Even Number")
#     else : 
#         print("its Odd")

# sanju(a)

# def max_two(a,b):
#     if a > b:
#         print("a is greater")
#     else :
#         print ("a is smaller")
# max_two(10,20)

# def str1(a,b):
#     print(a+b)
# str1("sanju"," ""sali")


    

# def fib(x):

#     a = 0
#     b = 1

   
#     for i in range(x):

#         c = a+b
#         a = b
#         b = c
#         print(c)
# fib(10)


# def ipo(a):
#     if a >= 18:
#         print("You are eligible")
#     else:
#         print("you are not eligible")


# ipo(int(input("age")))

# def canVote(age):

#     if age>=18:
#         return "yes"
#     else:
#         return "no"

# result = canVote(18)
# print(result)


# def sum_all(a):
#     total = 0
#     for x in numbers:
#         tota

# sum_all(sum())





# list1 = [2,4,5,6,8]
# def given_sq(list1):
#     new_list =[]

#     for i in list1:
#        new_list.append(i**2)
#     return new_list
    
# result = given_sq(list1)
# print(result)

# def pali1(a):

# def pali1(a):
    
#     pali1 = str(input("enter name"))
#     if pali1 == pali1[::-1]:
#         print("polidrome")
#     else: 
#         print("No")


# pali1(pali1)


# def sanju(a,b):
#     print(a+b)
# sanju("sanju ","sali")

# x = str(input("enter string"))
# y = ""

# for i in x:
#     y = i+y

# if y==x:
#     print("is polidrome")
# else:
#     print("not polidrome")


# # sorting without using inbuilt function # 
# old_list = [10,15,5,6,11,12,13,23,17]
# def sort_fun1(new_lst):
#     for i in range(len(new_lst)):
#         for j in range(i + 1, len(new_lst)):
#             if new_lst[i] > new_lst[j]:
#                 new_lst[i], new_lst[j] = new_lst[j], new_lst[i] 
#     return new_lst    

# print(sort_fun1(old_list))

# a = int(input("enter 1st number"))
# b = int(input("enter 2nd number"))

# def add_num(a,b):
#     return (a+b,a-b,a*b,a/b)

# print(add_num(a,b))


# 
# a = str(input("1st string"))
# b = str(input("2nd string"))

# def concat(a,b):
#     return a+" " +b

# print(concat(a,b))


# user_num = int(input("enter multiplaction num"))
# def multi(a):
#     for i in range(1,11):
#         print(user_num,"x",i,"=",user_num*i)

# multi(cuser_num)





# def max_num(a,b,c):
#     if a > b :
#         print("a is greater",a)
#     elif b>c:
#         print("b is greater",b)
#     else:
#         print("c is greater",c)
# max_num(20,30,40)



# def fibo(x):
#     a = 0
#     b = 1
#     for i in range(x):
#         c = a+b
#         a =b
#         b= c
#         print(c)
# fibo(10)

# a = int(input("value1"))
# b =int(input("value2"))

# def sum_add(a,b):
#     print(a+b,a*b,a-b,a/b)

# sum_add(a,b)

# def my_func(name,age):
#     print(name,age)
# my_func("sanju",25)

# def my_num(a,b):
#     print(a,b)

# my_num(80,30)

# def calculation(a,b):
#     print(a+b,a-b)
# calculation(40,10)

# def  factorial_num(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial_num(n-1)

# n = int(input("Enter the Number"))

# print(factorial_num(n))


# def show_employye(name, salary = 9000):
#     print("name :",name,"salary :",salary)

# show_employye("sanju",200000)
# show_employye("madhav",30)


# a = int(input("value 1 :"))
# b = int(input("value 2 :"))

# def add(a,b):
#     return a+b
# print(add(a,b))



# def display_student(name,age):
#     print(name,age)

# new_student = display_student

# new_student("sanju",25)

# num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

# def even_num(num):
#     for i in range (num):
#          if num % 2 ==0:
#              if num>5:
#                  print("even number are",num)
#              else:
#                  print("numbers are odd")
# x = num
# even_num(x)
        
 
class Student:

    def __init__(self,name,grade,bloodgroup,rank, **kwargs):
        self.name = name
        self.grade = grade
        self.bloodgroup = bloodgroup
        self.rank = rank

stud1 = Student(name ="Mark",grade="10th",bloodgroup="O'+ve",rank = "97th")
stud2 = Student(name ="Jhon",grade="10th",bloodgroup="A'+ve",rank = "92th")
stud3 = Student(name ="Rony",grade="10th",bloodgroup="B'+ve",rank = "87th")
stud4 = Student(name ="Steven",grade="10th",bloodgroup="O'-ve",rank = "90th")
stud5 = Student(name ="Hawk",grade="10th",bloodgroup="AB'+ve",rank = "77th")


print(stud1.name)



