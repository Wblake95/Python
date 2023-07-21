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
            print("Even number:", number//2)
        else:
            print("Odd number:", number*3+1)

except KeyboardInterrupt:
    print("This game was interrupted by the keyboard, Good bye!")
