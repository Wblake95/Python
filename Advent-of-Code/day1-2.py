# Day 1 of adventive code.
# My solution

with open("day1.txt") as file:
#with open("temp.txt") as file:
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
    answer = 0
    for i in file:
        temp = {}
        low = ""
        high = ""
        for j in nums:
            begNum = i.find(str(j))
            if begNum != -1:
                temp.update({begNum:j})
        for j in nums:
            endNum = i.rfind(str(j))
            if endNum != -1:
                temp.update({endNum:j})
        for k in spelledNums:
            begSpell = i.find(k)
            if begSpell != -1:
                temp.update({begSpell:spelledNums[k]})
        for k in spelledNums:
            endSpell = i.rfind(k)
            if endSpell != -1:
                temp.update({endSpell:spelledNums[k]})
        low = min(temp.keys())
        high = max(temp.keys())
        temp = str(temp[low]) + str(temp[high])
        answer += int(temp)
    print(answer)
