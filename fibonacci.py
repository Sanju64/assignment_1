# #Fibonacci Series 

# value = 20
# def fibonacci(n):
#     pre_value, last = 0,1
#     for each in range(n):
#         yield pre_value
#         pre_value,last = last,pre_value + last

# #output

# print(list(fibonacci(value)))



#fibo 




def fib(x):
    
    a = 0
    b = 1

    print(a)
    print(b)
    for i in range(x):
        c = a +b
        a = b
        b = c
        print(c)
fib(5)

# str1 = str(input(""))
# str2 = str(input(""))

# def concat(str1):
#     str1+=str2
    
#     return str1
# concat(str1)