# Maitre D'
# Demonstrates treating a value as a condition
#   for numbers, 0 evaluates to False, everything else to True
#   for strings, "" evaluates to False, everything else to True

print ("Welcome to the Chateau D' Food")
print ("\nIt seems we are quite full this evening.")

money = int(input("\nHow many dollars do you tip: "))

if money:   # no comparison, but same as "if money != 0"
    print ("Right this way to your table.")
else:
    print ("Please, wait.  It may be a while.")

input("\n\nPress the enter key to exit.")

