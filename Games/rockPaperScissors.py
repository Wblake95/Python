# scores
scores = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

file = open("temp.txt")

# score
myScore = 0
# bonus points
winBonus = 6
drawBonus = 3
loseBonus = 0

for i in file:
    temp = i.split()
    if not temp:
        break
    # break down
    # A,B,C = Rock, Paper, Scissors
    # X,Y,Z = Rock, Paper, Scissors
    # wins
    if temp[0] == "A" and temp[1] == "Y":
        myScore += scores[temp[1]] + winBonus
        #print("win", 1)
    if temp[0] == "B" and temp[1] == "Z":
        myScore += scores[temp[1]] + winBonus
        #print("win", 2)
    if temp[0] == "C" and temp[1] == "X":
        myScore += scores[temp[1]] + winBonus
        #print("win", 3)
        # draws
    if temp[0] == "A" and temp[1] == "X":
        myScore += scores[temp[1]] + drawBonus
        #print("draw", 1)
    if temp[0] == "B" and temp[1] == "Y":
        myScore += scores[temp[1]] + drawBonus
        #print("draw", 2)
    if temp[0] == "C" and temp[1] == "Z":
        myScore += scores[temp[1]] + drawBonus
        #print("draw", 3)
        # lose
    if temp[0] == "A" and temp[1] == "Z":
        myScore += scores[temp[1]] + loseBonus
        #print("lose", 1)
    if temp[0] == "B" and temp[1] == "X":
        myScore += scores[temp[1]] + loseBonus
        #print("lose", 2)
    if temp[0] == "C" and temp[1] == "Y":
        myScore += scores[temp[1]] + loseBonus
        #print("lose", 3)
    #print("loop {i} complete"\r)
print(myScore)
