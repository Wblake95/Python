#!/usr/bin/env python
import sys
try:
    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("That is not a number!")
            continue
    while number>1: # This is the math for the collatz. Apparently, it will always end in 1.
        if number%2==0: # Test for even.
            number=number//2
            print(number)
        else: # Else it will be odd.
            number=number*3+1
            print(number)

except KeyboardInterrupt:
    print("This game was interrupted by the keyboard, Good bye!")
