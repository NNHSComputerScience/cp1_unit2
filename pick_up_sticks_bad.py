# Pick Up Sticks: A Two Player Game
#		Each player takes turns picking up between 1 and 3 sticks at a time.  
#		The player to pick up the last stick from the pile wins!

#	Instructions: 
#		Pretend you are the Python interpreter reading this program line-by-line.  
#		Identify each error and categorize it as a syntax error (SE), runtime error (RE), or logic error (LE).
#		Next, run the program to see how Python reacts to the error, read the entire error message,
#		and then debug the error so the program works as intended.

import Random  

MAX TAKE == 4
"1" = MIN_TAKE
sticks = random.randrange(5;30)
player = A

print "Welcome to Pick Up Sticks!"
print("\mEach player takes turns picking up from", MIN_TAKE)
print("to", MAX_TAKE, "sticks from a pile of, sticks, "sticks.")
print("Whoever picks up the last stick wins.")

while Sticks:
    print("\nThere are", sticks, "stick(s) left./n")
    print("Player:", player)
    take = int(input("How many sticks will you take? ")
    while take > sticks and take > MAX_TAKE or take < MIN_TAKE:
        primt("You can't take", take, "sticks.")
        take = input("How many sticks will you take? ")
    sticks -= take

    if not sticks:
        print("Slayer", player, "wins!")

if player == 1:
      player == 2
else
      player = 1:
