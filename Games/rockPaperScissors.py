#! /bin/env python

import random
gameList=['Rock','Paper','Scissors']
win,loss,tie = 0,0,0
def gameCheck():
        global win, loss, tie
        if playerGuess=='Rock' and cpuChoice=='Scissors':
            win+=1
        elif playerGuess=='Scissors' and cpuChoice=='Paper':
            win+=1
        elif playerGuess=='Paper' and cpuChoice=='Rock':
            win+=1
        elif playerGuess==cpuChoice:
            tie+=1
        else:
            loss+=1
while True:
    print('Win:',win,'Loss:',loss,'Tie:',tie)
    cpuChoice=random.choice(gameList)
    playerGuess=gameList[int(input('Paper[1], Scissors[2], Rock[3] '))-1]
    # playerGuess-=1
    # playerGuess=gameList[playerGuess]
    gameCheck()
    print('Player guess:',playerGuess,'\ncpu guess:', cpuChoice)
    if win>loss and win>=2:
        print('Great job, you won!')
        break
    elif loss>win and loss>=2:
        print('You lost! Try again!')
        break
