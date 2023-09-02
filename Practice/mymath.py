# the algorithm for sqaure root is a binary search
def multi(num1,num2):
    sum = 0
    if num2 > num1:
        temp, num1 = num1, num2
        num1 = temp
    for i in range(num2):
        sum = num1 + num1
        return sum

def div(num1,num2):
    sum = 0
    count = 0
    while True:
        num1 = num1 - num2
        count += 1

def mysqrt(num1):
    hi = 0
    low = 0
    temp = num1
    while True:
        if multi(temp,temp) > num1:
            hi = temp
            temp = temp//2
        elif multi(temp,temp) < num1:
            low = temp
            temp = (hi+low)//2
        elif multi(temp,temp) == num1:
            return temp
            break
        else:
            print("Something went wrong")
