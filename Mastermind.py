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

# We initialize our perfect pegs counter
pepegs = 0

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
    # If there are as much perfect pegs as the size of the code, well the player won.
    if pepegs == size:
        win = True
            
# We stop the timer here.
t1 = time.time()
total = t1 - t0







