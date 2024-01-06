# We have a list of parts that we need to identify and figure out which one is missing.
# If a number is adjacent to a symbol, except for a period, it is a part number.
# after that, sum the total of part numbers.

def funcPrescore(prescore):
    index = table[i].find(table[i][j])
    while index > 0 and (table[i][index-1] != "." or table[i][index-1] not in symbol):
        index -= 1
    for h in range(index,len(table[i])):
        if table[i][index] != ".":
            prescore = prescore + table[i][index]
    return prescore


with open("temp.txt", "r") as file:
    score = 0
    symbol = ["!","@","#","$","%","^","&","*","(",")","-","_","=","+",",","/","?"]
    table = {
            }
    incr = 0
    prescore = ""

    for i in file:# transfer file to dict aka table
        table.update({incr:i})
        incr += 1

    for i in range(len(table)):# line # in table
        prescore = ""# here???
        for j in range((len(table[i]))):# char # in line
            if table[i][j] == "." or table[i][j] in symbol:# skip periods
                break
            if table[i][j] in prescore:
                break
            #up left diagnal
            if i > 0 and j > 0 and table[i-1][j-1] in symbol:
                funcPrescore(prescore)
            #up
            elif i > 0 and table[i-1][j] in symbol:
                prescore = funcPrescore(prescore)
            #up right diagnal
            elif i > 0 and j <= len(table[i])-1 and table[i-1][j+1] in symbol:
                prescore = funcPrescore(prescore)
            #left
            elif j > 0 and table[i][j-1] in symbol:
                prescore = funcPrescore(prescore)
            #right
            elif j < len(table[i])-1 and table[i][j+1] in symbol:
                prescore = funcPrescore(prescore)
            #down left diagnal
            elif i < len(table)-1 and j > 0 and table[i+1][j-1] in symbol:
                prescore = funcPrescore(prescore)
            #down
            elif i < len(table)-1 and table[i+1][j] in symbol:
                prescore = funcPrescore(prescore)
            #down right diagnal
            elif i < len(table)-1 and j <= len(table[i])-1 and table[i+1][j+1] in symbol:
                prescore = funcPrescore(prescore)
            else:
                print("i", i,"\n", table[i],"\n", prescore)

        #answer
        score += int(prescore)
