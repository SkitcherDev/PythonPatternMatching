#!/usr/bin/env python
# -*- coding: utf-8 -*-

def isPhoneNumber(text):
	if len(text) != 12:
		return False
	for i in range (0,3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-':
		return False
	for i in range(4,7):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8,12):
		if not text[i].isdecimal():
			return False
	return True

f = open("workfile.txt", "r")
message = f.read()
f.close()

for i in range(len(message)):
	chunck = message[i:i+12]
	if isPhoneNumber(chunck):
		print(chunck)
print("Done")

