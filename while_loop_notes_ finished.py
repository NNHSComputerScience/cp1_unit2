# while loop notes
'''
while loop, written in English (PSEUDOCODE):
test the LOOP CONDITION
    while condition is True, run this block of code (LOOP BODY)
    if condition becomes false (SENTINEL VALUE is met), this block is skipped
loop ends and program continues sequentially

# WHILE LOOP - control structure that continues to execute a block of code while a condition is True.
# LOOP CONDITION - conditional expression the loop is based upon.
# LOOP BODY - indented block beneath the while statement. Contains statements to be repeated in loop.
# LOOPING VARIABLE - variable tested in the loop condition; must be updated in the loop body.
# SENTINEL VALUE - the value that will exit the loop by making the loop condition False.
'''
    
# How to use a counter
#   Keeps track of number of times loop is executed.
counter = 0
print ("Let's count to 100!")
input("Press enter to start the counter.")
while counter < 101:    # loop condition; sentinel value is 101 and greater
    print ("The count is at: ", counter) # start of loop body
    counter += 1        # updating the looping variable

# Common mistake: not updating the looping variable (results in infinite loop)

input("Press enter to exit.\n\n\n")

# Countdown Challenge (on own)
#   Make a counter that counts down from 10 and then says "BLAST OFF!" once 0 is displayed

print("Let's count down to BLAST OFF!")
input("Press enter to start the countdown.")
count = 10

while count > 0:
    print(count)
    count -= 1

print("BLAST OFF!")

input("\nPress enter to exit.")

# Count by 5's Challenge(on own)
#   Count 0-100 by 5's
#   Print a message to tell the user when the count is half-way done
#   Try to write it generically so it works for any limit value (not just 100)

count = 0
end = 100

print("\n\nLet's count to 100 by 5's!")
input("Press enter to start the counter.")
 
while count <= end:
    print("The count is at: ", count)
    if count == (end / 2):
        print("Half-way there!")
    count += 5

input("\nPress enter to exit.\n")

# die_roller Challenge (partner)
#   Guess how many rolls it takes to roll a 5?

import random

# initialize variables
guess = int(input("How many rolls to get a 5? "))
rolls = 0
die = 0

# loops if roll is not a 5
while die != 5:
    die = random.randint(1,6)
    print("you rolled a", die)
    rolls += 1      # counts number of rolls
    
print("It took", rolls, "rolls to roll a 5!")

# check if user's guess was correct
if guess == rolls:
    print("Congrats! You guess it right!")
else:
    print("I'm sorry, you guessed incorrectly.")

input("\nPress enter to exit.")

# die_roller2 Challenge (partner)
#   Display how many evens after 5 rolls of a die.
count = 1
evens = 0
while count < 6:
    roll = random.randint(1,6)
    print("You rolled a", roll)
    if roll % 2 == 0:
        evens += 1
    count += 1

print("You rolled", evens, "even numbers")

input("\nPress enter to exit.")





