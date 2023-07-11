#! /usr/bin/env python
while True:
    answerThing=input('Enter Hello, Good bye, or Good evening: ')
    if answerThing.lower()=='hello' or answerThing=='good bye' or answerThing=='good evening':
        break
    else:
        continue
match answerThing.lower():
    case 'hello':
        print('Hello there!')
    case 'good bye':
        print('Good bye!')
    case 'good evening':
        print('Good evening!')
