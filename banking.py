#! /bin/env/ python

nameUser = ''
accountUser = ''
passwordUser = ''
Balance = ''
guess = ''

def login():
    global nameUser, accountUser, passwordUser
    nameGuess = input('What is your username? ')
    passwordGuess = input('What is your password? ')
    if nameGuess == nameUser:
        if passwordGuess == passwordUser:
            guess = True
        return guess
    else:
        print('Incorrect username/password')
        guess = False
        return guess

def Createaccount():
    global nameUser, accountUser, passwordUser, Balance
    nameUser = input('What is your username? ')
    passwordUser = input('What is your password? ')
    Balance = input('How much will you add to your account? ')

def Checkbalance():
    global Balance, guess
    login()
    if guess == True
        print(nameUser)
        print(accountUser)
        print(Balance)

def Deposit():
    global Balance, guess
    login()
    if guess == True
        deposit = input('How much would you like to deposit? ')
        Balance += int(deposit)
        return Balance
        checkbalance()

def Withdrawl():
    global Balance, guess
    login()
    if guess == True
        withdrawl = input('How much would you like to withdrawl? ')
        Balance -= int(withdrawl)
        return Balance
        checkbalance()

while True:
    print('Welcome to the bank!')
    print('You can \"create an account[ca]\",\"check your balance[cb]\", \"deposit money[d]\", or \"withdrawl money[w]\"')
    todo = input('What would you like to do? ')
    if todo == 'ca':
        Createaccount()
    elif todo == 'cb':
        Checkbalance()
    elif todo == 'd':
        Deposit()
    elif todo == 'w':
        Withdrawl()
    again = input('Would you like to go again? ')
    if again == 'y':
        return False
