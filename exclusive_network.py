# Exclusive Network
# Demonstrates logical operators in conditions
#   and, or, not

print ("\tExclusive Computer Network")
print ("\t\tMembers only!\n")

security = 0

username = ""
while not username:
    username = input("Username: ")

password = ""
while not password:
    password = input("Password: ")

if username == "Mike" and password == "secret":
    print ("Hi, Mike.")
    security = 1
elif username == "S.Meier" and password == "civilization":
    print ("Howdy, Sid.")
    security = 1
elif username == "S.Miyamoto" and password == "mariobros":
    print ("What's up, Shigeru?")
    security = 1
elif username == "W.Wright" and password == "thesims":
    print ("How goes it, Will?")
    security = 1
elif username == "guest" or password == "guest":
    print ("Welcome, guest.")
    security = 1
else:
    print ("Login failed.  You're not so exclusive.\n")
    
if security == 1:
    print("Welcome to the Exclusive Computer Network", username)
