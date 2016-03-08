#!/usr/bin/env python
# -*- coding: utf-8 -*-

# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.


import shelve, pyperclip

mcbShelf = shelve.open("..\\Clipboard\\mcb")

# Save clipboard content.
needInput = True

while needInput == True:
	userInput = input("Command: ")
	inputArg = userInput.split()


	if len(inputArg) == 2:
		if inputArg[0].lower() == "save":
			mcbShelf[inputArg[1]] = pyperclip.paste()
			needInput = False
		elif inputArg[0].lower() == "del":
			del mcbShelf[inputArg[1]]
			print(str(list(mcbShelf.keys())))
		elif inputArg[0].lower() == "show":
			print(mcbShelf[inputArg[1]] + "\n")
	elif len(inputArg) == 1:
		#List keywords and load content.
		if inputArg[0].lower() == "list":
			print(str(list(mcbShelf.keys())))
		elif inputArg[0].lower() == "help":
			print("Commands:\n--save [keyword]: Save current clipboard\n--[keyword]: Copy saved data to the clipboard\n")
			print("--show [keyword]: Show the contents of the saved keyword'\n--list: List all keywords\n--del [keyword]: Delete saved data\n--help: Open the instructions")
		elif inputArg[0] in mcbShelf:
			pyperclip.copy(mcbShelf[inputArg[0]])
			needInput = False

	else:
		needInput = False


mcbShelf.close()