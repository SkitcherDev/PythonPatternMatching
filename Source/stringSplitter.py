#!/usr/bin/env python
#! python3
# -*- coding: utf-8 -*-

import re

#TODO: splitter(string,character) to remove all occurences of the characters from the string

def splitter(userString, charReg = " "):

	if charReg == " ":
		i = 0
		while userString[i] == " ":
			i+=1
		userString = userString[i:]
		i = len(userString)-1
		while userString[i] == " ":
			i-=1
		userString = userString[:i+1]
	else:
		splitReg = re.compile(charReg)
		userString = splitReg.sub("", userString)

	return userString

		##splitReg = re.compile(charReg)

#TODO: Take userinput and print strin with removed terms

myInput = input("Enter a string: ")
myChar = input("Enter a character to remove or leave empty: ")
if len(myChar) > 0 :
	print(splitter(myInput,myChar[0]))
else: 
	print(splitter(myInput))