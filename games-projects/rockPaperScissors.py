#! /bin/env python

import random
gameList=['Paper','Scissors','Rock']
win,loss,tie = 0,0,0
def gameCheck():
    global win,loss,tie,playerGuess,cpuChoice
    if playerGuess==gameList.index(cpuChoice):
        tie+=1
    elif playerGuess==gameList.index['Rock'] and cpuChoice==gameList[0]:
        loss+=1
    elif playerGuess==gameList.index['Paper'] and cpuChoice==gameList[2]:
        win+=1
    elif playerGuess>cpuChoice:
        loss+=1
# print(gameList.index('Paper'))
# print(gameList[0])

while True:
    print('Win:',win,'Loss:',loss,'Tie:',tie)
    cpuChoice=random.choice(gameList)
    playerGuess=int(input('Paper[1], Scissors[2], Rock[3] '))
    playerGuess-=1
    gameCheck()
    print('Player guess:',gameList[playerGuess],'\ncpu guess:', cpuChoice)
    if win>loss and win>=2:
        print('Great job, you won!')
        break
    elif loss==2:
        print('You lost! Try again!')
        break
