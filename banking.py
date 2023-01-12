#! /bin/env/ python
def Balance():
    nameUser = None
    ageUser = None
    passwordUser = None
    Balance = 500

def WhatToDo():
    if check == 'c':
        nameUser = input('What will be your username? ')
        print(nameUser)
        ageUser = input('What is your age? ')
        passwordUser = input('Create a password ')
    if check == 'd':
        deposit = input('How much would you like to deposit? ')
        deposit.int()
        Balance += int(deposit)

check = input('What would you like to do? ([C]reate account, [D]eposit money, [W]ithdraw money, or C[H]eck your balance)')
check.casefold()
