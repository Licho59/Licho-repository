#! python3
# Project: Generating Random Quiz Files
'''
Say you’re a geography teacher with 35 students in your class and you want
to give a pop quiz on US state capitals. Alas, your class has a few bad eggs
in it, and you can’t trust the students not to cheat.
You’d like to randomize the order of questions so that each quiz is unique,
making it impossible for anyone to crib answers from anyone else

The task is to prepare quiz and answers in random order, along with the answer key
'''
# Step 1 - storing the quiz data in a dictionary
import random

# the quiz data
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
    'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


# Step 2 - generating 3 quiz data - can be prepared for any number of quizes
for quizNum in range(3):
    # create the quiz and answer key files
    quizFile = open('capitalsquiz{:d}.txt'.format(quizNum + 1), 'w')
    answerKeyFile = open('capitasquiz_answers{:d}.txt'.format(quizNum + 1), 'w')

    # write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form {:d})'.format(quizNum + 1))
    quizFile.write('\n\n')
    
    # shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    # Step 3 - loop through all 50 states, making a question for each
    for questionNum in range(50):
        # get right and wrong answers
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Step 4 - write content to the quiz and answer key files:
        # write the question and answer options to the quiz file
        quizFile.write('{}. What is the capital of {}\?\n'.format(questionNum +1, states[questionNum]))

        for i in range(4):
            quizFile.write(' {}. {}\n'.format('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')
        
        # write the answer key to a file
        answerKeyFile.write('{}. {}\n'.format(questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
        

