file = open("temp.txt")

spliter = []
temp = ""
list = []

for i in file:
    if i == "\n":
        break
    spliter = i.split(",")
    for i in range(len(spliter)):
        temp = spliter[i]
        spliter[i] = temp.split("-")
    list.append(spliter)
del temp, spliter
file.close()

score = 0
for i in list:
    if int(i[0][0]) >= int(i[1][0]):
        if int(i[0][1]) <= int(i[1][1]):
            score += 1
    if int(i[1][0]) >= int(i[0][0]):
        if int(i[1][1]) <= int(i[0][1]):
            score += 1

print(score)
