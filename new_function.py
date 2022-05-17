# def voting_eligiblity(a):

#     if age>=18:
#         print("you are eligible")
#     else:
#         print("you are not eligible")

# age= int(input("enter your age"))

# voting_eligiblity(age)


# class Student:
#    def __init__(self, fname, lname, age, section):
#        self.firstname = fname
#        self.lastname = lname
#        self.age = age
#        self.section = section 

       


# p1 = Student("Jack's","The Sea Bird",44,"Python Developer")    


# print(p1.firstname)
# print(p1.lastname)
# print(p1.age)
# print(p1.section)

# def string1(a,b):
#     a = [1,2,3,4,5,6,7,8,9]
#     b = [4,5,6,7,9,4,7,23]
   
#     for i in a==b:
#         i = c
#         print(i)

# string1(c)


# import random

# def lottery():
#     # returns 6 numbers between 1 and 40
#     for i in range(6):
#         yield random.randint(1, 40)

#     # returns a 7th number between 1 and 15
#     yield random.randint(1, 15)

# for random_number in lottery():
#        print("And the next number is... %d!" %(random_number))


# def feb(x):
#     a = 0
#     b = 1

#     for i in range (x):

#         c = a+b
#         a = b
#         b = c
#         print(c)

# feb(10)


# a = int(input("enter the 1st number"))
# b = int(input("enter the 2nd number"))
# c = int(input("enter the 3rd number"))

# def max_num(a,b,c):

#     if a >b:
#         print("a is greater",a)
#     elif b>c:
#         print("b is greater",b)
#     else:
#         print("c is greater",c)

# max_num(a,b,c)


# def mult_all(numbers):

#     total = 1

#     for each in numbers:
#         total *= each
#     return total

# print(mult_all((8,2,4,30,12,10,23,78,60,14)))


def samp1(a):

    str = ""
    for i in a:
        str = i + str
    return str

a = "1234abcdef"
print(samp1(a))