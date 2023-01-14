#! /bin/env/ python

nameUser = ''
passwordUser = ''
Balance = 0
guess = False

def login():
    global nameUser, passwordUser, guess
    nameGuess = input('What is your username? ')
    if nameGuess == nameUser:
        print('correct')
        passwordGuess = input('What is your password? ')
        if passwordGuess == passwordUser:
            print('correct')
            guess = True
    else:
        print('Incorrect username/password')
        guess = False

def Createaccount():
    global nameUser, passwordUser, Balance
    nameUser = input('What is your username? ')
    passwordUser = input('What is your password? ')
    Balance = int(input('How much will you add to your account? '))
    int(Balance)

def Checkbalance():
    global nameUser, passwordUser, Balance, guess
    login()
    if guess == True:
        print(nameUser)
        print(Balance)

def Deposit():
    global Balance, guess
    login()
    if guess == True:
        deposit = input('How much would you like to deposit? ')
        Balance += int(deposit)
        Checkbalance()

def Withdraw():
    global Balance, guess
    login()
    if guess == True:
        withdraw = input('How much would you like to withdraw? ')
        Balance -= int(withdraw)
        Checkbalance()

while True:
    print('Welcome to the bank!')
    print('You can \"create an account[ca]\",\"check your balance[cb]\", \"deposit money[d]\", or \"withdraw money[w]\"')
    print(nameUser)
    print(passwordUser)
    print(Balance)
    print(guess)
    todo = input('What would you like to do? ')
    if todo == 'ca':
        Createaccount()
    elif todo == 'cb':
        Checkbalance()
    elif todo == 'd':
        Deposit()
    elif todo == 'w':
        Withdraw()
    again = input('Would you like to go again? ')
    if again == 'n':
        break
