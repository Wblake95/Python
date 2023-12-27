# Day 1 of adventive code.
# My solution

with open("day1.txt") as file:
    nums = [x for x in range(10)]
    spelledNums = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "zero": 0
            }
    # grab 5 letters at a time, check to see if a number is first, then check for string.
    # repeat process.
    answer = 0
    for i in file:
        temp = ''
        for j in i:
            if j in str(nums):
                temp += j
                # print(temp)
            if j in spelledNums:
                temp += spelledNums[j]
        if len(temp) > 0:
            numStr = temp[0] + temp[-1]
            # print(numStr)
            answer += int(numStr)
            # print(answer)
    print(answer)

