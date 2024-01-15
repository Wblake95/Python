from random import randint

def dice(face:int=20) -> int:
    '''
    Simple dice roller.
    :param: face = the number of faces the dice will have, default = 20
    '''
    return randint(1,face)

def listDice(face:int=20, numOfDice:int=1, drop:str="") -> list:
    '''
    Create a list of rolled dice.
    :param: face = the number of faces the dice will have, default = 20
    :param: numOfDice = the number of dice to roll, default = 1
    :param: drop = option to drop lowest/highest value, default = empty
    '''
    total = []
    for x in range(numOfDice):
        total.append(randint(1,face))
    if drop.lower() == "low":
        total.remove(min(total))
    elif drop.lower() == "high":
        total.remove(max(total))
    return total
