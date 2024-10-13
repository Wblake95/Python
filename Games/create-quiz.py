# /usr/bin/env python

# Goals
# create x differen quizzes
#   write each quiz to file
# Creates 50 multiple-choise questions for each quiz, in random order
#   write answer key to each quiz

from random import choice

myDict = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
   'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
   'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta',
   'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing',
   'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
   'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
   'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
   'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
   'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# this is because dictionaries are not subscriptable apparenlty.
myList = list(myDict.keys())

quizCount= int(input("How many quizes: "))
quizName: str = input("What is the quiz name: ")

for x in range(quizCount):
    with open("{}{}.txt".format(quizName, x + 1),"w") as quiz:
        for state in myDict.keys():
        # gen random list of answers with one real one.
        # list[ 1, 2, 3, real]
        # 1. make sure correct answer is in there.
        # 2. no duplicate answers.
            # initialize list with correct answer.
            answers = [myDict[state]]

            # generate wrong answers without duplicates
            while len(answers) < 4:
                city = myDict[choice(myList)]
                if city not in answers:
                    answers.append(city) 

            # format good, just need answers
            quiz.write("""{}. What is the capital of {}?
            A. {}
            B. {}
            C. {}
            D. {}
            
            """.format(x + 1, state, answers[0], answers[1], answers[2], answers[3])
            )
