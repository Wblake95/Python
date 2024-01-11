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
    if index < 0:
        index = 0
    for x in string[index:]:
        if x in listNums:
                part = part + x
        else:
            break
    if part != temp[-1]:
        return part

def appendToList(myFunc):
    if myFunc != None:
        temp.append(myFunc)


with open("data.txt", "r") as file:
    score = 0
    table = {
            }
    listSymbols = ["!","@","#","$","%","^","&","*","(",")","-","_","=","+",",","<",">","/","?"]
    listNums = ["1","2","3","4","5","6","7","8","9","0"]
    incr = 0
    temp = [None]
    for i in file:
        table.update({incr:""})
        for j in i:
            if j == "\n":
                break
            table[incr] = table[incr] + j
        incr += 1


for i in table.keys():
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
            if i < strLen:
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
temp.pop(0)
for i in temp:
    score += int(i)
print(score)
