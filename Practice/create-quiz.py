# /usr/bin/env python

# Goals
# create x differen quizzes
#   write each quiz to file
# Creates 50 multiple-choise questions for each quiz, in random order
#   write answer key to each quiz

from random import shuffle

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New
   Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West
   Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

quizCount: int = input("How many quizes: ")
quizName: str = input("What is the quiz name: ")

for x in range(quizCount):
    with open("{quizName}{quizCount}.txt".format(quizName, quizCount + 1),"a") as quiz:
        # gen random list of answers with one real one.
        # list[ 1, 2, 3, real]
        # 1. make sure correct answer is in there
        # 2. no duplicate answers


        # format good, just need answers
        for state in capitals.keys():
            quiz.write("""{x}. What is the capital of {state}?
            A. {capital}
            B. {rand2}
            C. {rand1}
            D. {rand1}
            
            """.format(x, state, answers[1], answers[2], answers[3], answers[4])
