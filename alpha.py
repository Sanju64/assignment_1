from audioop import reverse


test = input("enter the charecters")

freq = {}

for i in test:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("chare : " + str(freq))