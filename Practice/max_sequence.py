#/usr/bin/env python

#def max_sequence(arr):
#    if not arr: return 0
#    mylist, arrLen = list(), len(arr)
#    
#    for i in range(arrLen):
#        mylist.append(sum(arr[i:arrLen]))
#
#
#    return max(mylist)
#
#test = [-1,2,3,-5,4,5,5]
#def max_sequence(arr):
#    if not arr: return 0
#    mySet, arrLen = set(), len(arr)
#    
#    for i in range(arrLen):
#        # end to begin
#        mySet.add(sum(arr[i:]))
#        # front to end
#        mySet.add(sum(arr[:arrLen-i]))
#        # middles
#        mySet.add(sum(arr[i:arrLen-i]))
#        print(i,arrLen-i,arr[i:arrLen-i])
#        
#    result = max(mySet)
#        
#    return result if result >= 0 else 0


# This is my attempt at a divide and conquer.
# I divided the input array into all possible combinations,
# retieved the sum of that sub array and put them in a set to prevent duplicates.
# according to codewars.com, it is too slow.
def max_sequence(arr):
    if not arr: return 0
    mySet, arrLen = set(), len(arr)

    for i in range(arrLen):
        sum = 0
        for j in range(i, arrLen):
            sum += arr[j]
            mySet.add(sum)

    result = max(mySet)

    return result if result >= 0 else 0

test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sequence(test))
