# while loop notes
'''
while loop, written in English (PSEUDOCODE):
while statement tests the LOOP CONDITION
    while condition is True, run this block of code (LOOP BODY)
    if condition becomes false (SENTINEL VALUE is met), this block is skipped and loop ends
loop ends and program continues sequentially

# WHILE LOOP - control structure that continues to execute a block of code while a condition is True.
# LOOP CONDITION - conditional expression the loop is based upon.
# LOOP BODY - indented block beneath the while statement. Contains statements to be repeated in loop.
# LOOPING VARIABLE - variable tested in the loop condition; must be updated in the loop body.
# SENTINEL VALUE - the value that will exit the loop by making the loop condition False.
'''

import random

# initialize variables
guess = int(input("How many rolls to get a 5? "))
rolls = 0
# !!! INSTRUCTOR NOTE: demonstrate rolling die here first to show infinite loop
die = 0  # LOOPING VARIABLE    

# loops if roll is not a 5
while die != 5:         # LOOP CONDITION (SENTINEL VALUE of 5)
    die = random.randint(1,6)   # updating the LOOPING VARIABLE
    print("you rolled a", die)
    rolls += 1          # end of LOOP BODY

# Common mistake: not updating the looping variable (results in an INFINITE LOOP)

print("It took", rolls, "rolls to roll a 5!")

# check if user's guess was correct
if guess == rolls:
    print("Congrats! You guess it right!")
else:
    print("I'm sorry, you guessed incorrectly.")

input("\nPress enter to continue.\n")

# How to use a counter (accumulation variable)
#   Keeps track of number of times loop is executed.
counter = 0
print ("Let's count to 100!")
input("\nPress enter to start the counter.\n")
while counter < 101: 
    print ("The count is at: ", counter) 
    counter += 1        

input("\nPress enter to continue.\n")

# Countdown Challenge (on own)
#   Make a counter that counts down from 10 and then says "BLAST OFF!" once 0 is displayed

print("Let's count down to BLAST OFF!")
input("\nPress enter to start the countdown.\n")
count = 10

while count > 0:
    print(count)
    count -= 1

print("BLAST OFF!")

input("\nPress enter to continue.\n")

# Count by 5's Challenge(on own)
#   Count 0-100 by 5's
#   Print a message to tell the user when the count is half-way done
#   Try to write it generically so it works for any limit value (not just 100)

count = 0
end = 100

print("\nLet's count to 100 by 5's!")
input("\nPress enter to start the counter.\n")
 
while count <= end:
    print("The count is at: ", count)
    if count == (end / 2):
        print("Half-way there!")
    count += 5

input("\nPress enter to continue.\n")


# die_roller Challenge (partner)
#   Display how many evens after 5 rolls of a die.
count = 1
evens = 0
while count < 6:
    roll = random.randint(1,6)
    print("You rolled a", roll)
    if roll % 2 == 0: # if the roll is an even number
        evens += 1
    count += 1

print("You rolled", evens, "even numbers")

input("\nPress enter to exit.")
