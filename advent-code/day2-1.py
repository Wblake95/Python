# Day 2 of Advent of Code

# Goal, test to see what games are impossible
# Sum the numbers of each game (example: game 1 + game 2 = 3)
import re

score = 0
check = {
    "r": 12,
    "g": 13,
    "b": 14
    }

# I will need about 4 splits starting with : ; , and finally a space.

with open("day2.txt", "r") as file:
    for i in file:
        temp = True
        x = re.findall("\d+ [r|g|b]", i)
        for j in x:
            a = j.split(" ")
            if check[a[1]] < int(a[0]): # example: check[key] < value
                temp = False
                break
        if temp:
            x = re.search("^Game \d+", i)
            a = x.group()
            a = a.split(" ")
            score += int(a[1])
    print(score)
