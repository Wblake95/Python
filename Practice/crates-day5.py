project = {
    1 : ["t","p","z","c","s","l","q","n"],
    2 : ["l","p","t","v","h","c","g"],
    3 : ["d","c","z","f"],
    4 : ["g","w","t","d","l","m","v","c"],
    5 : ["p","w","c"],
    6 : ["p","f","j","d","c","t","s","z"],
    7 : ["v","w","g","b","d"],
    8 : ["n","j","s","q","h","w"],
    9 : ["r","c","q","f","s","l","v"]
}

instructionList = []

with open("temp.txt") as file:
    for i in file:
        if i != "\n":
            temp = i.split()
            instructionList.append(temp)


