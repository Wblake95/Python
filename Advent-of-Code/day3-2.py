# my goal, locate the special characters and find the number around it.

def myFunc(index:int, string:str) -> str:
    part = ""
    if index > 0:
        for x in string[index::-1]:
            if x in listNums:
                index -= 1
            else:
                index += 1 
                break
    if index < 0:
        index = 0
    for x in string[index:]:
        if x in listNums:
                part = part + x
        else:
            break
    if part != temp[-1]:
        return part

def appendToList(myFunc:str) -> list:
    if myFunc != None and myFunc != preList[-1]:
        preList.append(myFunc)

def other(preList:list) -> list:
    print(preList)
    preList.pop(0)
    if len(preList) > 1:
        y = 1
        for i in preList:
            y = y * int(i)
        temp.append(y)


with open("data.txt", "r") as file:
    score = 0
    table = {
            }
    listSymbols = "*"
    listNums = ["1","2","3","4","5","6","7","8","9","0"]
    incr = 0
    temp = [None]
    preList = [None]
    for i in file:
        table.update({incr:""})
        for j in i:
            if j == "\n":
                break
            table[incr] = table[incr] + j
        incr += 1


for i in table.keys():
    y = 0
    for j in range(len(table[i])):
        symbol = table[i][j]
        strLen = len(table[i])-1
        if symbol in listSymbols:
            # up
            if i > 0:
                if table[i-1][j] in listNums:
                    appendToList(myFunc(j,table[i-1]))
                # left up
                if j > 0:
                    if table[i-1][j-1] in listNums:
                        appendToList(myFunc(j-1,table[i-1]))
                # up right
                if j < strLen:
                    if table[i-1][j+1] in listNums:
                        appendToList(myFunc(j+1,table[i-1]))
            # left
            if j > 0:
                if table[i][j-1] in listNums:
                    appendToList(myFunc(j-1,table[i]))
            # right
            if j < strLen:
                if table[i][j+1] in listNums:
                    appendToList(myFunc(j+1,table[i]))
            # down
            #if i < strLen:
            if i < (len(table.keys())-1):
                if table[i+1][j] in listNums:
                    appendToList(myFunc(j,table[i+1]))
                # left down
                if j > 0:
                    if table[i+1][j-1] in listNums:
                        appendToList(myFunc(j-1,table[i+1]))
                # down right
                if j < strLen:
                    if table[i+1][j+1] in listNums:
                        appendToList(myFunc(j+1,table[i+1]))
        y += 1
        if y == 3:
            break
        other(preList)
        preList = [None]

temp.pop(0)
for i in temp:
    score += int(i)
print(score)
