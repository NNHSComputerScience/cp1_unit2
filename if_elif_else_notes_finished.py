# Unit 2 Notes: Intro to modules; Intro to if-elif-else
#   How to use branching logic in Python.

# A) MODULES are files that contain code you can import to use in your own program.

# The RANDOM MODULE contains functions related to generating pseudorandom numbers.
#   Documentation here: https://docs.python.org/3/library/random.html

# Import entire module like this:
import random
# Import one function from a module like this:
from random import randint

# randint() function:
#   Requires 2 int arguments & returns random # between those 2 values (inclusive).
#   e.g. prints a random number between 1 and 10
print(random.randint(1,10))

# randrange() function:
#   Requires 1 int argument & returns random # from a range created from 0 to the int (exclusive).
#   e.g. prints a random number between 0 and 9
print(random.randrange(10))      # 0-9; numbers start from 0!
print(random.randrange(10)+1)    # 1-10

#   Can also call with 2 arguments: start and stop (exclusive)
#   e.g. prints a random number between 1 and 10
print(random.randrange(1, 11)

# Challenge: Dice Challenge 1
#   Create 2 die variables.  Simulate rolling each die by generating a
#   random number between 1 and 6 and printing it. Use 2 diff functions.
die1 = random.randint(1,6)
die2 = random.randrange(6)+1
print("Roll 1 =", die1)
print("Roll 2 =", die2)

# -------------------------------------------------------------
# B) if statement (binary bypass)
#   Block of code executes if condition is true.
#   CONDITIONAL STATEMENT - A true/false statement that can be evaluated and 
#       acted upon in one way if true and another if false.

password = input("Please enter your password: ")

if password == "nnhs":  
    print("\nAccess granted")
    
"""
COMPARISON OPERATORS (aka RELATIONAL OPERATORS) - compare the values on either 
    side of them (operands) and determine their relation.
        == (EQUALITY OPERATOR) Evaluates to True if two values are equal.
        != Evaluates to True if two values are not equal.
        >  Evaluates to True if the left value is greater than the right.
        <  Evaluates to True if the right value is greater than the left.
        >= Evaluates to True if the left value is greater than or equal to the right.
        <= Evaluates to True if the right value is greater than or equal to the left.
        
Evaluating expressions in console:
> 7 == 7
True
> 7 != 7
False
> 7 != 8
True
> 3 < 4
True
> 3 < 3
False
> 3 <= 3
True
"""

# Challenge: Simple if (BINARY BYPASS - one action associated with an condition)
#   Generate a random number, 1-99, and print "You generated a 2 digit number!"
#   if the random number generated is greater than 9.
num = random.randint(1,99)
print(num)
if num > 9:
    print("\nYou generated a 2 digit number!")

# -------------------------------------------------------------
# C)if - else (BINARY CHOICE - two actions associated with a condition)
#   If block executes if condition is true;
#   else block executes if condition is false.
password = input("Please enter your password: ")

if password == "nnhs":
    print("\nAccess GRANTED")
else:
    print("\nAccess DENIED!")

# Challenge: Coin flip
#   Create a coin flipping simulator to randomly flip a coin to be heads/tails.
#   if heads, print "Heads"; if tails, print "Tails"
coin = random.randint(1,2)  # heads = 1; tails = 2
if coin == 1:
    print ("\nHeads")
if coin == 2:
    print ("\nTails")

# -------------------------------------------------------------
# D)if - elif - else (binary bypass & binary choice)
#   If block executes if condition is true;
#   elif block executes if condition is true;
#   else block executes if condition is false.
password = input("Please enter your password: ")

if password == "nnhs":
    print("\nAccess GRANTED")
elif password == "NNHS":
    print("\nAccess GRANTED")
elif password == "Nnhs":
    print("\nAccess GRANTED")   # can have as many elif's as you need!
else:
    print("\nAccess DENIED!")

# What would be a better way to handle variation in the password input?

# Challenge: Ice Cream Challenge
#   Remember our ice cream algorithm? Recreate your own below using at least 4 flavors, e.g.:
#   get flavor from user.
#   if user wants vanilla, "You get Vanilla"
#   elif user wants chocolate, "You get Chocolate"
#   elif user wants strawberry, "You get Strawberry"
#   else, "Sorry we don't have <insert flavor>. Here's your Pistachio."

flavor = input("What flavor of ice cream would you like?").title()

if flavor == "Vanilla":
    print("\nYou get Vanilla")
elif flavor == "Chocolate":
    print("\nYou get Chocolate")
elif flavor == "Strawberry":
    print("\nYou get Strawberry")
else:
    print(f"\nSorry we don't have {flavor}. Here's your Pistachio.")

# Extension: Create a number guessing game using the random module and user input.
#   Allow the user more than one guess and provide the user feedback on whether their first guess is "too high" or "too low".
      
target = random.randint(1,100)
guess = int(input("Guess a number, 1 - 100: "))
      
if guess < target:
      guess = int(input("Too low, guess again: "))
elif guess > target:
      guess = int(input("Too high, guess again: "))

if guess == target:
      print("You guessed it!  the number was", target)
else:
      print(f"You guessed {guess} and the number was {target}")
      
input("\nPress enter to exit.")
