#!/usr/bin/env python
#! python3
# -*- coding: utf-8 -*-

import re

#Define function to test password strength
def testPassword(inputPass):
	hasDigit = re.compile(r"(.*)\d+(.*)")
	hasLowercase = re.compile(r"(.*)[a-z]+(.*)")
	hasUppercase = re.compile(r"(.*)[A-Z]+(.*)")

	rDig = hasDigit.search(inputPass)
	rLow = hasLowercase.search(inputPass)
	rUp = hasUppercase.search(inputPass)

	if len(inputPass) < 8:
		return "Password too short!"
	if rDig == None:
		return "Password has no digits!"
	if rLow == None:
		return "Password has no lowercases!"
	if rUp == None:
		return "Password has no uppercases!"

	return "Your password is strong!"

#Get user input

password = input("Enter the password to test: ")


#Write result to console

print(testPassword(password))
