from multiprocessing.sharedctypes import Value
from unittest import result


test = str(input("enter charecters"))

mr = {}

for i in test:
    if i in mr:
        mr[i]+=1
    else:
        mr[i]=1

for key,Value in mr.items():
    print(key, ":" , Value)