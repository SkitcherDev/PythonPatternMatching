#!/usr/bin/env python
#! python3
# -*- coding: utf-8 -*-

import re, pyperclip

#Phoneregex to filter the phone numbers

phoneNumberRegex = re.compile(r"""(
	(\d{3}|\(\d{3}\))?					# area code
	(\s|-|\.)?							# separator
	(\d{3})								# 3 digits
	(\s|-|\.)							# seperator
	(\d{4})								# 4 digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))?    	# extension
	)""",re.VERBOSE)


#Emailregex to filter the emails

emailRegex = re.compile(r"""(
	[A-Za-z0-9._%+-]+					# mail
	@									# at
	[A-Za-z0-9.-]+					# domain
	(\.[a-zA-Z]{2,4})					# .extension
	)""",re.VERBOSE)

#Read from clipboard

textToScan = str(pyperclip.paste())
matches = []

for groups in phoneNumberRegex.findall(textToScan):
 phoneNumber = '-'.join([groups[1], groups[3], groups[5]])
 if groups[8] != '':
 	phoneNumber += ' x' + groups[8]
 matches.append(phoneNumber)
for groups in emailRegex.findall(textToScan):
 matches.append(groups[0])

#Write result to clipboard

if len(matches) > 0:
	pyperclip.copy("\n".join(matches))
	print("Copied the results to the clipboard")
	print("\n".join(matches))
else: 
	print("No matches found!")