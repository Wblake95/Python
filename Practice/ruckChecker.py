file = open("temp.txt")

tally = {}

# lower case letters = score 1-26
for i in range(97,(97+26)):
    tally[chr(i)] = (i-96)
# upper case letters = score 27-52
for i in range(65,(65+26)):
    tally[chr(i)] = (i-38)

score = 0

for i in file:
    # grabs line with is a string
    if not i:
        break
    for j in i:
        # literally create temp
        temp = j
        count = 0
        for h in i:
            # compare temp to char in string,
            # if count > 1, break
            if temp == h:
                count +=1
            if count > 1:
                score += tally[h]
                break
