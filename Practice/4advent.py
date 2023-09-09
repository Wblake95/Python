file = open("temp.txt")

spliter = []
temp = ""
list = []

for i in file:# gets each line
    if i == "\n":# skip last line in file
        break
    spliter = i.split(",")# first split between elve pair
    for i in range(len(spliter)):# I want each elf to be a list pair combo example: [[23,23],[23,34]]
        temp = spliter[i]
        spliter[i] = temp.split("-")
    list.append(spliter)

del temp, spliter# I don't need them anymore
file.close()# don't need this anymore 
score = 0# my scoring system

for i in list:# the actual work
    if int(i[0][0]) >= int(i[1][0]):
        if int(i[0][1]) <= int(i[1][1]):
            score += 1
    if int(i[1][0]) >= int(i[0][0]):
        if int(i[1][1]) <= int(i[0][1]):
            score += 1
    if int(i[1][0]) == int(i[0][0]):
        if int(i[1][1]) == int(i[0][1]):
            score -= 1
    # else:
    #     if int(i[1][0]) >= int(i[0][0]):
    #         if int(i[1][1]) <= int(i[0][1]):
    #             score += 1

print(score)# my answer is 516.
