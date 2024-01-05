# Day 1 of adventive code.
# My solution

with open("day1.txt") as file:
    nums = [x for x in range(10)]
    answer = 0
    for i in file:
        temp = ''
        for j in i:
            if j in str(nums):
                temp += j
        if len(temp) > 0:
            numStr = temp[0] + temp[-1]
            answer += int(numStr)
    print(answer)

