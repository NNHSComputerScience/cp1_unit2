"""
Name: 
Title: Unit 2 Notes - boolean values and logical operators
Description: boolean values and logical operators
"""
import random

# 2 BOOLEAN VALUES: True and False (must be capitalized in Python)
#   in console...
print(True)
print(False)

var = True
print(var)

# a BOOLEAN EXPRESSION is an expression that evaluates to either True or False.
#  in console...
print(5 == 5)  # True
print(5 != 5)  # False

# CHALLENGE: Generate a random number between 1 and 13 and print "Your number is lucky." if the number is 7, 11, or 13.

num = random.randint(1, 13)
print(num)
if num == 7:
	print("Your number is lucky.")
elif num == 11:
	print("Your number is lucky.")
elif num == 13:
	print("Your number is lucky.")
else:
	print("Your number is not lucky")

# LOGICAL OPERATORS: and, or, not
#   order of precendence is: not, and, or

if num == 7 or num == 11 or num == 13:
	print("Your number is lucky.")
else:
	print("Your number is not lucky.")

# TRAP: 
if num == 7 or 11 or 13:  # 11 and 13 are evaluated as expressions
	print("Your number is lucky.")
else:
	print("Your number is not lucky.")

# non-zero numbers are evaluated as True; zero is evaluated as False
if 0:
	print("Evaluated as True")
else:
	print("Evaluated as False")

# any non-empty string value is evaluated as True; empty strings are False
if "":
	print("Monty Evaluated as True")
else:
	print("Monty Evaluated as False")

# Nesting if statements
num = 10
if "1" in str(num):
	if "0" in str(num):	
		print("One and Zero zero are in the number")
  else:
    print("One and Zero are not in the number")  # BUG
  
# nested code only runs if the outer if statement is True

# CHALLENGE: Exclusive Network
'''
With a partner, write a Python program to grant access to an exclusive computer network.
- Get a username and password from the user
- Check to see if the username/password matches any of the exclusive member username/passwords
- Allow guest access if ‘guest’ is the username OR the password
- Print a message including the username if they gained access
- Print message denying access if the login credentials are incorrect

Extension challenges:
- Can you loop the program to allow the user to try entering the password again if they fail?
- Can you make the program only give them 3 opportunities to re-enter their password?
- Can you make the program check their password to be sure it's secure? (check for at least
    8 characters, at least one numeric, and at least one special character (!, $, &) )
- What other features would an exclusive network have?

'''
