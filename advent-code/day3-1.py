# my goal, locate the special characters and find the number around it.

def myfunc(index, string):
    global temp
    other = ""
    indexFound = False
    target = string[index]
    while True:
        if string[index-1] in nums:
            index -= 1
        else:
            break
    for x in range(index,len(string)):
        if string[x] not in nums:
            other = ""
        if string[x] in nums:
            other = other + string[x]
        if string[x] == target: 
            indexFound = True
        if indexFound:
            try:
                if string[x+1] not in nums:
                    temp.add(other)
                    break
                elif index == len(string)-1:
                    temp.add(other)
                    break
            finally:
                print("fail")
                break

with open("data.txt", "r") as file:
    score = 0
    table = {
            }
    symbols = ["!","@","#","$","%","^","&","*","(",")","-","_","=","+",",","<",">","/","?"]
    nums = ["1","2","3","4","5","6","7","8","9","0"]
    incr = 0
    temp = set()

    for i in file:
        table.update({incr:""})
        for j in i:
            if j == "\n":
                break
            table[incr] = table[incr] + j
        incr += 1
    for i in table:
        for j in range(len(table[i])):
            try:
                # left up
                if table[i][j] in symbols and table[i-1][j-1] in nums:
                    myfunc((j-1),table[i-1])
                # up
                if table[i][j] in symbols and table[i-1][j] in nums:
                    myfunc(j,table[i-1])
                # up right
                if table[i][j] in symbols and table[i-1][j+1] in nums:
                    myfunc((j+1),table[i-1])
                # left
                if table[i][j] in symbols and table[i][j-1] in nums:
                    myfunc((j-1),table[i])
                # right
                if table[i][j] in symbols and table[i][j+1] in nums:
                    myfunc((j+1),table[i])
                # left down
                if table[i][j] in symbols and table[i+1][j-1] in nums:
                    myfunc((j-1),table[i+1])
                # down
                if table[i][j] in symbols and table[i+1][j] in nums:
                    myfunc(j,table[i+1])
                # down right
                if table[i][j] in symbols and table[i+1][j+1] in nums:
                    myfunc((j+1),table[i+1])
            finally:
                None
    for i in temp:
        score += int(i)
    print(score)
