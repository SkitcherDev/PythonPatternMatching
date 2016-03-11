#!/usr/bin/env python
# -*- coding: utf-8 -*-

inputFile = open("..\\Files\\raw.txt", "r")
inputLines = inputFile.readlines()
inputFile.close()
outputFile = open("..\\Files\\refined.txt", 'w')

for line in inputLines:
	words = line.split()
	print(line, end="")
	for word in words:
		if word[0:4] == "NOUN":
			words[words.index(word)] = input("Replace NOUN with: ")
		elif word[0:4] == "VERB":
			words[words.index(word)] = input("Replace VERB with: ")
		elif word[0:9] == "ADJECTIVE":
			words[words.index(word)] = input("Replace ADJECTIVE with: ")
		elif word[0:6] == "ADVERB":
			words[words.index(word)] = input("Replace ADVERB with: ")
	line = " ".join(words)
	del words
	outputFile.write(line + "\n")

outputFile.close()
