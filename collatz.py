#!/usr/bin/env python
import sys
try:
    while True:
        try:
            number = int(input("Enter a number: "))
            break
            # print(number)
        except ValueError:
            print("That is not a number!")
            continue
    while number>1:
        if number%2==0:
            number=number//2
            print("Even number:", number)
        else:
            number=number*3+1
            print("Odd number:", number)

except KeyboardInterrupt:
    print("This game was interrupted by the keyboard, Good bye!")
