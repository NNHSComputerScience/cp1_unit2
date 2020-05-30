# Exclusive Network
# Demonstrates logical operators in conditions
#   and, or, not

print ("\tExclusive Computer Network")
print ("\t\tMembers only!\n")

security = 0

username = input("Username: ") 
password = input("Password: ") 

if username == "Mike" and password == "secret":
    security = 1  
elif username == "S.Meier" and password == "civilization":
    security = 1 
elif username == "S.Miyamoto" and password == "mariobros":
    security = 1 
elif username == "W.Wright" and password == "thesims":
    security = 1 
elif username == "guest" or password == "guest":
    security = 1 
else:
    print ("Login failed.  You're not so exclusive.\n")

if security == 1:
    #write code
    print("Welcome to the Exclusive Computer Network", username) 

input("\n\nPress the enter key to exit.")
