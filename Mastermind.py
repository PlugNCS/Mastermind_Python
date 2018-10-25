# Mastermind in Python
# Version 1.0
# (c) 2018 Michaël NASS & Remi GOMEZ
import random
import time
name = input("Hello player, what's your name? ")
colors = int(input("How many colours do you want? "))
size = int(input("How long should the size of the code be? "))
attempts = int(input("How many maximal attemps do you want? "))
code = []
i = 0
while i < size - 1:
    code.append(random.randint(0, colors))
    i += 1
count = 0 
t0 = time.time()
pepegs = 0
win = False
while count < attempts and win == False:
    count += 1
    gcode = input("Attempt number ", count, ": Enter the code: ")
    acode = gcode.split()
    cnt = 0
    while cnt < size:
        if acode[cnt]==code[cnt]:
            pepegs += 1
        cnt += 1
    if pepegs == size:
        win = True
            
t1 = time.time()
total = t1 - t0







