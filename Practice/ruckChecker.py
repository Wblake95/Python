file = open("temp.txt")

dict = {}

for i in range(97,97+26):
    dict[chr(i)] = i-96
for i in range(65,65+26):
    dict[chr(i)] = i-38


