# Day 2 of Advent of Code

# Goal, get highest number of each color, multiply, then add each game
import re

score = 0

with open("day2.txt", "r") as file:
    for i in file:
        x = re.findall("\d+ [r|g|b]", i)
        red = [0, "r"]
        blue = [0, "b"]
        green = [0, "g"]
        for j in x:
            a = j.split(" ")
            check = int(a[0])
            match a[1]:
                case "r" if check >= red[0]:
                        red[0] = check
                case "b" if check >= blue[0]:
                        blue[0] = check
                case "g" if check >= green[0]:
                        green[0] = check
                case _:
                    print("Check", check, "num, color", a)
        score += (red[0]*blue[0]*green[0])
    print(score)
