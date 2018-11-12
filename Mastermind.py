# Mastermind in Python
# Version 1.0
# (c) 2018 Michaël NASS & Remi GOMEZ
import random
import time

# Getting some basic informations about the player and his preferences.
name = input("Hello player, what's your name? ")
colors = int(input("How many colours do you want? "))
size = int(input("How long should the size of the code be? "))
attempts = int(input("How many maximal attemps do you want? "))

# Code generation
code = []
i = 0
while i < size:
    code.append(random.randint(0, colors))
    print(code[i])
    i += 1

# The game can now start, we start the timer
count = 0
t0 = time.time()

# We initialize our perfect and partial pegs counter
pepegs = 0
papegs = 0

# Simple indicator to know if the player won or not
win = False

# The actual game process:
while count < attempts and win == False:
    count += 1
    gcode = input("Attempt number " + str(count) + ": Enter the code: ")
    # Read the code provided by the user
    acode = gcode.split()
    cnt = 0
    # Here, we check for the number of perfects pegs.
    while cnt < size:
        if acode[cnt]==code[cnt]:
            pepegs += 1
        cnt += 1
    
    # Here, we check for the number of partial pegs.
    generalcounter = 0
    while generalcounter < size:
        specificcounter = 0
        while specificcounter < size:
            if acode[generalcounter] == code[specificcounter] and acode[generalcounter] != code[generalcounter]:
                papegs += 1
            specificcounter += 1
        generalcounter += 1
    
    # If there are as much perfect pegs as the size of the code, well the player won. Else, we inform him about how he performed.
    if pepegs == size:
        win = True
    else:
        print("You have found ", pepegs, " perfect pegs and ", papegs, " partial pegs. You have ", attempts-count, " attempts left.")
            
# We stop the timer here.
t1 = time.time()
total = t1 - t0

# Finally, we check if the user won or not and inform him about the score.
if win == True:
    print("Congratulations! You won the game in ", count, " attempts and it took you ", total, " seconds to finish the game.")
else:
    print("Oh no! You didn't make it. Next time, you'll surely perform better! Just to inform you, it took you ", total, " seconds to finish the game.")







