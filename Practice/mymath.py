# the algorithm for square root is a binary search
def multi(num1,num2):
    '''
    :param num1: first int
    :param num2: second int
    '''
    sum = 0
    for i in range(num2):
        sum += num1
        if i == num2-1:
            return sum

def div(num1,num2):
    '''
    :param num1: first int
    :param num2: second int
    '''
    count = 0
    while True:
        num1 = num1 - num2
        if num1 >= 0:
            count += 1
        elif num1 <= 0:
            return count
            break

def mysqrt(num1):
    '''
    :param num1: number you are looking for
    '''
    hi = num1
    low = 0
    temp = num1
    while True:
        x = multi(temp,temp)
        if x > num1:
            hi = temp
            temp = div(temp,2)
            # return hi, temp
        if x < num1:
            low = temp
            temp = div((hi+low),2)
            # return low, temp
        if x == num1:
            return temp
            break
