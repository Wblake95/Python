#! /bin/env/ python

nameUser = ''
passwordUser = ''
Balance = 0
guess = False

def login():
    global nameUser, passwordUser, guess
    name_guess = input('What is your username? ')
    if name_guess == nameUser:
        print('correct')
        password_guess = input('What is your password? ')
        if password_guess == passwordUser:
            print('correct')
            guess = True
    else:
        print('Incorrect username/password')

def create_account():
    global nameUser, passwordUser, Balance
    nameUser = input('What is your username? ')
    passwordUser = input('What is your password? ')
    Balance = int(input('How much will you add to your account? '))
    int(Balance)

def check_balance():
    global nameUser, passwordUser, Balance, guess
    login()
    if guess:
        print(nameUser)
        print(Balance)


def deposit():
    global Balance, guess
    login()
    if guess:
        a_deposit = input('How much would you like to deposit? ')
        Balance += int(a_deposit)
        check_balance()


def withdraw():
    global Balance, guess
    login()
    if guess:
        a_withdraw = input('How much would you like to withdraw? ')
        Balance -= int(a_withdraw)
        check_balance()


while True:
    print('Welcome to the bank!')
    print(
        'You can \"create an account[ca]\",\"check your balance[cb]\", \"deposit money[d]\", or \"withdraw money[w]\"')
    print(nameUser)
    print(passwordUser)
    print(Balance)
    print(guess)
    todo = input('What would you like to do? ')
    if todo == 'ca':
        create_account()
    elif todo == 'cb':
        check_balance()
    elif todo == 'd':
        deposit()
    elif todo == 'w':
        withdraw()
    again = input('Would you like to go again? ')
    if again == 'n':
        break
