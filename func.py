#Adding and Multiplying and Substracting the Value

# value1 = int(input("First Value"))
# value2 = int(input("Second Value"))

# def sub_multi(value1,value2):
#     return value1+value2,value1-value2,value1*value2

# print(sub_multi(value1,value2))


#is student in list or not

# def student(stud_id):

#     stud_list = [10,15,46,70,20,14,30]
#     if stud_id in stud_list:
#         print(f"{stud_id} He is Available") 
#     else:
#         print(f"{stud_id} is Not In Available")

# stud_id = int(input("enter student id"))


# student(stud_id)


# Max Of three Numbers

# def max_three(a,b,c):
#     if a>b:
#         print(f"Num {a} is greater")
#     elif b>c:
#         print(f"Num {b} is greater")
#     else:
#         print(f"Num {c} is greater")


# max_three(333,560,980)

#Find Even or Number

# def even_odd(a):
#     if a %2 ==0:
#         print(f"{a} is even")
#     else:
#         print(f"{a} is odd")

# a = int(input("enter the number"))

# even_odd(a)


#Define a function which counts vowels and consonant in a word.


def count(val):
    vov = 0
    con = 0
    for i in range(len(val)):
        if val[i] in ['a','e','i','o','u']:
            vov+=1
        else:
            con+=1
    
    print("Count of Vov",vov)
    print("Count of Con",con)

x = input("enter the value")
count(x)
