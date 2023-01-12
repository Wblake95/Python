#! /bin/env/ python

def WhatToDo():
    global Balance
    if check == 'c':
        nameUser = input('What will be your username?: ')
        print(nameUser)
        ageUser = input('What is your age?: ')
        passwordUser = input('Create a password: ')
        print(nameUser)
        print(ageUser)
        print(Balance)
    elif check == 'd':
        deposit = input('How much would you like to deposit?: ')
        Balance += int(deposit)
        print(Balance)
        return Balance
    elif check == 'w':
        withdraw = input('What would you like to withdraw?: ')
        Balance -= int(withdraw)
        print(Balance)
        return Balance
    elif check == 'h':
        print(Balance)


while True:
    Balance = 500
    check = input('What would you like to do? ([C]reate account, [D]eposit money, [W]ithdraw money, or C[H]eck your balance): ')
    check.casefold()
    WhatToDo()
    goAgain = input('y, n: ')
    if goAgain == 'n':
        break
