#count of the charecters

#1

from collections import Counter

char_count = input("Enter the charecters to Count")

my_counter = Counter (char_count)
print(my_counter)


#2
Count_string = 'Hello World This is the Python code'
print(Count_string.count(input('o')))


#3
# using lambda
test_str = "Python_classes"
count = sum(map(lambda x : 1 if 's' in x else 0, test_str))
  
# result 
print ("Count of s is : "   +  str(count))