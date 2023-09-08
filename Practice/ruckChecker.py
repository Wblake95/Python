file = open("temp.txt")

tally = {}

# lower case letters = score 1-26
for i in range(97,(97+26)):
    tally[chr(i)] = (i-96)
# upper case letters = score 27-52
for i in range(65,(65+26)):
    tally[chr(i)] = (i-38)

score = 0

for i in file:# this is a string
    if not i:
        break
    ruck1 = ""
    ruck2 = ""
    for j in range(len(i)):# split string in half
        if j < len(i)//2:# first half of string
            ruck1 += i[j]
        else:# second half of string
            ruck2 += i[j]
    # print("ruck1:", len(ruck1))
    # print("ruck2:", len(ruck2))
    for h in ruck1:# grab letter
        if h in ruck2:# check letter in ruck2
            score += tally[h]
            break

print(score)
