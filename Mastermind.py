# Mastermind in Python
# Version 1.0
# (c) 2018 Michaël NASS & Remi GOMEZ
import random
name = input("Hello player, what's your name? ")
colors = int(input("How many colours do you want? "))
size = int(input("How long should the size of the code be? "))
attempts = int(input("How many maximal attemps do you want? "))
code = []
i = 0
while i < size - 1:
    code.append(random.randint(0, colors))
    i += 1








