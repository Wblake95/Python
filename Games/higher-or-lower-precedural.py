# HigherOrLower

import random

# Card constants
SuitTuple = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RankTuple = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

NCards = 8

# Pass in a deck and this function returns a random card from the deck
def GetCard(DeckListIn):
    ThisCard = DeckListIn.pop()
    return ThisCard

def shuffle(DeckListIn):
    DeckListOut = DeckListIn.copy()
    random.shuffle(DeckListOut)
    return DeckListOut

# main code
print('Welcome to Higher or Lower.')
print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 pionts; get it wrong and you lose 15 points.')
print('You have 50 points to start.')
print()

StartingDeckList = []
for suit in SuitTuple:
    for ThisValue, rank in enumerate(RankTuple):
        CardDict={'rank':rank, 'suit':suit, 'value':ThisValue+1}
        StartingDeckList.append(CardDict)

Score = 50

while Score > 0:
    print()
    GameDeckList = shuffle(StartingDeckList)
    CurrentCardDict = GetCard(GameDeckList)
    CurrentCardRank = CurrentCardDict['rank']
    CurrentCardValue = CurrentCardDict['value']
    CurrentCardSuit = CurrentCardDict['suit']
    print('Starting card is:', CurrentCardRank + ' of ' + CurrentCardSuit)
    print()

    for CardNumber in range(0, NCards):
        Answer = input('Will the next card be higher or lower than the ' + CurrentCardRank + ' of ' + CurrentCardSuit + '? (enter h or l):')
        Answer = Answer.casefold()
        NextCardDict = GetCard(GameDeckList)
        NextCardRank = NextCardDict['rank']
        NextCardSuit = NextCardDict['suit']
        NextCardValue = NextCardDict['value']
        print('Next card is:', NextCardRank + ' of ' + NextCardSuit)

        if Answer == 'h':
            if NextCardValue > CurrentCardValue:
                print('You got it right, it was higher')
                Score += 20
            else:
                print('Sorry, it was not higher')
                Score -= 15
        elif Answer == 'l':
            if NextCardValue < CurrentCardValue:
                Score += 20
            else:
                print('Sorry, it was not lower')
                score =+ 15
        print('Your score is:', Score)
        print()
        CurrentCardRank = NextCardRank
        CurrentCardValue = NextCardValue
