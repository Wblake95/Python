#!/usr/bin/env python3

from ttrpg import *

def encounter_test(func, numOfTest:int, x, y) -> float:
    success = 0

    for i in range(numOfTest):
        test = func(x,y)
        
        if test > 0:
            success +=1
        else:
            continue

    result = success / numOfTest

    return result


run_test = (encounter_test(encounter,100000,4,4) * 100)

print("With a defense of a d4 and an attacker with damage of a d4, the attacker will succeed {:.2f}% of the time.".format(run_test))

run_test = (encounter_test(encounter,100000,4,6) * 100)

print("With a defense of a d4 and an attacker with damage of a d6, the attacker will succeed {:.2f}% of the time.".format(run_test))

run_test = (encounter_test(encounter,100000,4,8) * 100)

print("With a defense of a d4 and an attacker with damage of a d8, the attacker will succeed {:.2f}% of the time.".format(run_test))

run_test = (encounter_test(encounter,100000,4,10) * 100)

print("With a defense of a d4 and an attacker with damage of a d10, the attacker will succeed {:.2f}% of the time.".format(run_test))

run_test = (encounter_test(encounter,100000,6,6) * 100)

print("With a defense of a d6 and an attacker with damage of a d6, the attacker will succeed {:.2f}% of the time.".format(run_test))

run_test = (encounter_test(encounter,100000,6,8) * 100)

print("With a defense of a d6 and an attacker with damage of a d8, the attacker will succeed {:.2f}% of the time.".format(run_test))

run_test = (encounter_test(encounter,100000,6,10) * 100)

print("With a defense of a d6 and an attacker with damage of a d10, the attacker will succeed {:.2f}% of the time.".format(run_test))
