myString = ""
with open("store.txt") as file:
    for i in file:
        myString += i

store = ''
count = 0
for i in myString:
    store += i
    if len(store) == 4:
        count = 0
        for j in store:
            temp = store.find(j, count)
            if
