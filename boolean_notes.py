# boolean values and logical operators
import random

# 2 BOOLEAN VALUES: True and False (must be capitalized in Python)
#   test in shell...
'''
>>> True
True
>>> False
False
>>> true
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    true
NameError: name 'true' is not defined
>>> type(True)
<class 'bool'>
>>> type("False")
<class 'str'>
>>>
'''

# a BOOLEAN EXPRESSION is an expression that evaluates to a boolean value.
#  in shell...
'''
>>> 5 == 5
True
>>> 5 != 5
False
>>> 5 < 10
True
>>> 5 >= 10
False
>>> 
'''

# LOGICAL OPERATORS: and, or, not
#   order of precendence is: not, and, or
#   https://runestone.academy/runestone/static/thinkcspy/Selection/PrecedenceofOperators.html

# CHALLENGE: Generate a random number between 1 and 13 and
#            print "Your number is lucky." if the number is 7, 11, or 13.

lucky_num = random.randint(1,13)
print(lucky_num)
if lucky_num == 7 or lucky_num == 11 or lucky_num == 13:
    print("Your number is lucky.")
# if lucky_num == 7 or 11 or 13:  <-- always True!

#  non-zero numbers and non-empty strings are evaluated as True
if 1: # and "Hi" and 5.5
    if "Hi":
        if 5.5:
            print("All evaluated to True.")
if 0 or 0.0 or "":
    print("At least one evaluated to True.")
else:
    print("All evaluated to False.")

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

# Exclusive Network
# Demonstrates logical operators in conditions
#   and, or, not

print ("\tExclusive Computer Network")
print ("\t\tMembers only!\n")

security = 0

username = input("Username: ") 
password = input("Password: ") 

if username == "a_user" and password == "itsasecret":
    security = 1  
elif username == "s_meier" and password == "civilization":
    security = 1 
elif username == "s_miyamoto" and password == "mariobros":
    security = 1 
elif username == "w_wright" and password == "thesims":
    security = 1 
elif username == "guest" or password == "guest":
    security = 1 
else:
    print ("Login failed.  You're not so exclusive.\n")

if security == 1: 
    print("Welcome to the Exclusive Computer Network", username) 

input("Press enter to exit.")
