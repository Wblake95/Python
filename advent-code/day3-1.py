# my goal, locate the special characters and find the number around it.

def myFunc(index, string):
    part = ""
    if index > 0:
        for x in string[index::-1]:
            if x in listNums:
                index -= 1
            else:
                index += 1
                break
    for x in range(index,len(string)):
        if string[x] in listNums:
            part = part + string[x]
        else:
            break
    return part


with open("temp.txt", "r") as file:
    score = 0
    table = {
            }
    listSymbols = ["!","@","#","$","%","^","&","*","(",")","-","_","=","+",",","<",">","/","?"]
    listNums = ["1","2","3","4","5","6","7","8","9","0"]
    incr = 0
    temp = set()
    for i in file:
        table.update({incr:""})
        for j in i:
            if j == "\n":
                break
            table[incr] = table[incr] + j
        incr += 1


for i in range(len(table)):
    for j in range(len(table[i])):
        symbol = table[i][j]
        strLen = len(table[i])-1
        if symbol in listSymbols:
            # up
            if i > 0:
                if table[i-1][j] in listNums:
                    temp.add(myFunc(j,table[i-1]))
                # left up
                if j > 0:
                    if table[i-1][j-1] in listNums:
                        temp.add(myFunc(j-1,table[i-1]))
                # up right
                if j < strLen:
                    if table[i-1][j+1] in listNums:
                        temp.add(myFunc(j+1,table[i-1]))
            # left
            if j > 0:
                if table[i][j-1] in listNums:
                    temp.add(myFunc(j-1,table[i]))
            # right
            if j < strLen:
                if table[i][j+1] in listNums:
                    temp.add(myFunc(j+1,table[i]))
            # down
            if i < strLen:
                if table[i+1][j] in listNums:
                    temp.add(myFunc(j,table[i+1]))
                # left down
                if j > 0:
                    if table[i+1][j-1] in listNums:
                        temp.add(myFunc(j-1,table[i+1]))
                # down right
                if j < strLen:
                    if table[i+1][j+1] in listNums:
                        temp.add(myFunc(j+1,table[i+1]))
print(temp)
for i in temp:
    if i == '':
        continue
    score += int(i)
print(score)
