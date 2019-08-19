#This program tests to see if a password is secure.
#Author: Daniel Jones
#last edited Mon August 19 4:51 PM

#re is the library that searches for regular expressions.
import re

print("Hello! This program is designed to see if you have a secure password. \nIt is advisable to have a password more than 12 characters long, have at least one number, \nat least one capital letter, at least one lower case number, and at least one special character.\n")
#stores password in variable
password = input('what is your password?\n')

#next four lines store what to search for.
special = re.compile(r'([!@#$%^&*?.<>])')
number = re.compile(r'(\d)')
cap = re.compile(r'[A-Z]')
lower = re.compile(r'[a-z]')

#8 characters is no longer considered secure. Must be at least 12 long.
if len(password) >= 12:
	#searches for numbers.
	isnum = number.search(password)
	if isnum == None:
		print('Please enter at least one number.')
		exit()
	#searches for capitalization.
	iscap = cap.search(password)
	if iscap == None:
		print('Need at least one capital letter.')
		exit()
	#looks for lower case letters.
	islower = lower.search(password)
	if islower == None:
		print('Need at least one lower case letter.')
		exit()
	#searches for special characters.
	isspecial = special.search(password)
	if isspecial == None:
		print('You need at least one special character.')
		exit()
	print("You have a secure password! Congrats!")
else:
	print('not long enough. Enter at least 12 digits.')
