#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

   # The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#Generate 35 Quizzes
for quizNum in range(5):
	quizFile = open("..\\quizes\\%s-CapitalsQuiz.txt" %(quizNum + 1), 'w')
	answerFile = open("..\\quizes\\%s-QuizAnswers.txt" %(quizNum +1), 'w')

	quizFile.write("Name:\n\nDate:\n\nPeriod:\n\n")
	quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)\n\n' % (quizNum + 1))

	states = list(capitals.keys())
	random.shuffle(states)

	# Create 50 multiple-choice questions for each quiz, in random order


	for questionNum in range(50):

		correctAnswer = capitals[states[questionNum]]
		wrongAnswers = list(capitals.values())
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		wrongAnswers = random.sample(wrongAnswers, 3)

		#Provide the correct answer and three random wrong answers for each question, in random order.
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions)

		#Write the quizzes to 35 text files.
		quizFile.write(" %s. What is the capital of %s?\n" % (questionNum + 1, states[questionNum]))

		for i in range(4):
			quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
		quizFile.write("\n")

		#Write the answer keys to 35 text files.
		answerFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

	quizFile.close()
	answerFile.close()