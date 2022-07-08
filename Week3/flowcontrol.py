#!/usr/bin/env python3

#Author: Jack Erickson
#Flow Control Assignment

print("""You enter a doark room with three doors.
Do you go through door #1 or door #2 or door #3?""")

door = input("-> ")

# == Door number 1 logic ================
if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?\n")

    print("1. Take the cake.")
    print("2. Scream at the bear.")

    # == Bear logic ====================
    bear = input("-> ")

    if bear == "1":
        print("1) The bear eats your face off. Good job!")
    elif bear == "2":
        print("2) The bear eats your legs off. Good job!")
    else:
        print(f"N)Well, doing {bear} is probably better.")
        print("Bear runs away.")

# == door number 2 logic ===================
elif door == "2":
    print("You look a room with a lion chained to a wall, with food just out of it's reach.")
    print("What do you do?\n")

    print("1. Shut the door. ")
    print("2. Push the food closer, so the lion can eat.")
    print("3. walk closer to get a better look.")

    # == insanity logic ==================
    lion = input("-> ")

    if lion == "2" or lion == "3":
        print("1) The lion breaks off the chain and eats you.")
        print("1) Good job!")
    else:
        print("N) You chose to mind your own buisiness.")
        print("N) Good job!")

# == Door number 3 logic ===================
elif door == "3":
    print("You look into a room pitch black room.")
    print("What do you do?")

    print("1. Walk inside.")
    print("2. close the doorand walk away.")

    # == something logic =================
    darkroom = input("-> ")

    if not darkroom == "2":
        print("What are you thinking? Something bites your leg and drags you away.")

    else:
        print("Good job you know better than to enter a completely dark room.")



else:
    print("You did not select a door??? Good Call :)")