file = open("temp.txt")

tally = {}

# lower case letters = score 1-26
for i in range(97,(97+26)):
    tally[chr(i)] = (i-96)
# upper case letters = score 27-52
for i in range(65,(65+26)):
    tally[chr(i)] = (i-38)

score = 0
count = 0
list = []
temp = []

# all of this creates a list of 3 lits
for i in file:
    temp.append(i)
    count += 1
    if count % 3 == 0:
        list.append(temp)
        temp = []

del temp, count
file.close()

temp = ""
count = False

for i in list:# list of 3
    for j in i:# list of 1 in 3, will only go once
        for h in j:# letter in i[0]
            if h in i[1] and h in i[2]:# check if in both
                score += tally[h]
                count = True
                break
        if count:
            count = False
            break

print(score)
