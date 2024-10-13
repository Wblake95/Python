#!/usr/bin/env python3

from random import randint

def dice(num: int):
    x = randint(1,num)
    return x

def encounter(x: int, y: int):
    defender = dice(x) 
    attacker = dice(y) 

    if attacker > defender:
        result = attacker - defender
        return result
    else:
        return 0


