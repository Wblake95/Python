# the algorithm for sqaure root is a binary search
def multi(num1,num2):
    sum = 0
    for i in range(num2):
        sum = num1 + num1
        return sum

def div(num1,num2):
    sum = 0
    for i in range(num2):
        sum = num1 - num1
        return sum

def square(base):
    # binary
    for i in range(base):
        num = base/2
        if multi(num, num) == base:
            return num
