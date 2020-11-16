'''
  Maitre D'
  Demonstrates treating a value as a condition & the 'in' operator

  Values as conditions review
    for numbers: 0 or 0.0 evaluates to False, everything else evaluates to True
    for strings: "" evaluates to False, everything else evaluates to True

  'in' operator
    Searches in a sequence(e.g. a string is a sequence of characters) for a 
      value and returns True if found, False if not found.
    May be combined with the 'not' operator to check if a value is 'not in' a 
      sequence.
'''
# e.g. the following prints that there's a fun in fundamentals:
if "fun" in "fundamentals":
    print("There's a 'fun' in fundamentals.")
        
# e.g. the following prints that there's no i in team: 
if "i" not in "team":
    print("There's no 'i' in team.")
else:
    print("There's an 'i' in team.")  

'''
CHALLENGE: Finish the program to check if the patron is a doctor 
          (check for "Dr." and "Doctor").  If they are, tell them that 
          they may be seated right away.  Doctor's don't have to tip if 
          they don't want to.
''' 
print ("Welcome to the Chateau D' Food")
print ("\nIt seems we are quite full this evening.")

name = input("\nWhat is the name?: ").title()
money = int(input("\nHow many dollars do you tip?: "))

# no comparison, but same as "if money != 0"; True if a tip is given
if money:   
    print ("Right this way to your table,", name + ".") 
else:
    print ("Please, wait.  It may be a while.")

input("\n\nPress the enter key to exit.")

