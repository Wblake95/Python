#/usr/bin/env python

def max_sequence(arr):
    if not arr: return 0
    mylist, arrLen = list(), len(arr)
    
    for i in range(arrLen):
        mylist.append(sum(arr[i:arrLen]))


    return max(mylist)

test = [-1,2,3,-5,4,5,5]


print(type(test))
print(max_sequence(test))
