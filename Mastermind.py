# Mastermind in Python
# Version 1.0
# (c) 2018 Michaël NASS & Remi GOMEZ
import random

# The timer support is considered as the first improvement over the basic requirements
import time

# The main menu is considered as the second improvement over the basic requirements.
showMainMenu = True

while showMainMenu == True:
    # We are declaring the default values needed for the user settings.
    isPlaying = True
    save = "no"
    winG = 0
    lostG = 0
    choice = str(input("Welcome in the Mastermind game. Type \"play\" to start playing the game or type \"about\" to learn more about the rules of the mastermind, or type \"exit\" to exit the program: "))
    if choice == "play" or choice == "Play" or choice == "" or choice == "PLAY" or choice == "Game" or choice == "game" or choice == "GAME" or choice == "Go" or choice == "go" or choice == "GO":
        while isPlaying == True:
            # Getting some basic informations about the player and his preferences. This is considered as the third improvement over the basic requirements
            if save == "no":
                name = input("Hello player, what's your name? ")
                colors = int(input("How many colours do you want? "))
                size = int(input("How long should the size of the code be? "))
                attempts = int(input("How many maximal attemps do you want? "))
                # The aibility to continue playing without restarting the game and giving the possibility to change the settings for the next game or save them, helping to show a global scoreboard at the end of the program is considered as the fourth improvement over the basic requirements.
                save = str(input("Do you wish to save those settings for the rest of the execution of the program? This means that if you reply \"yes\", you will have to quit the program to change these settings. If not, then reply \"no\" and we will ask you at every new game to enter the settings again: "))
            elif save == "yes":
                save = "yes"
                # Not really usefull, but we needed an indented block, and our IDE takes an empty block as en empty line, so we had to fill something in the block.
            else:
                print("An unknown error occured while retriving the save status of your settings. The programm will likely crash.")

            # Code generation
            code = []
            i = 0
            while i < size:
                code.append(random.randint(0, colors))
                # For diagnostics purposes only: print(code[i])
                i += 1

            # The game can now start, we start the timer
            count = 0
            t0 = time.time()

            # We initialize our perfect and partial pegs counter
            pepegs = 0
            papegs = 0
            
            # We initialize our Arrays that will be useful to avoid to count two times the same peg. They will be filled once the peg have been taken into account to allow us to check if we already did the verification or not.
            Apepegs = []
            Apapegs = []
            hs = 0
            while hs < size:
                Apapegs.append(-1)
                Apepegs.append(-1)
                # For diagnostics purposes only: print(code[i])
                hs += 1

            # Simple indicator to know if the player won or not
            win = False

            # The actual game process:
            while count < attempts and win == False:
                count += 1
                gcode = input("Attempt number " + str(count) + ": Enter the code: ")
                # Read the code provided by the user
                acode = list(gcode)
                cnt = 0
                # Here, we check for the number of perfects pegs.
                while cnt < size :
                    # For diagnostics purposes only: print (code[cnt])
                    # For diagnostics purposes only: print (acode[cnt])
                    # For diagnostics purposes only: print(acode[cnt], " match ", code[cnt])
                    if int(acode[cnt]) == int(code[cnt]) and int(acode[cnt]) != int(Apepegs[cnt]):
                        # For diagnostics purposes only: print("found one match.")
                        pepegs += 1
                        Apepegs[cnt] = acode[cnt]
                    cnt += 1
                
                # Here, we check for the number of partial pegs. This script is slower than the previous one but is way more accurate.
                
                generalcounter = 0
                while generalcounter < size:
                    specificcounter = 0
                    alreadyFound = False
                    while specificcounter < size and alreadyFound == False:
                        if int(acode[generalcounter]) == int(Apapegs[specificcounter]):
                            alreadyFound = True
                        specificcounter += 1
                    specificcounter = 0
                    while specificcounter < size and alreadyFound == False:
                        if int(acode[generalcounter]) == int(code[specificcounter]):
                            Apapegs[papegs] = acode[generalcounter]
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
                winG += 1
            else:
                print("Oh no! You didn't make it. Next time, you'll surely perform better! Just to inform you, it took you ", total, " seconds to finish the game.")
                lostG += 1

            # Now it's time to ask the user what does he want to do next and do what he wants.
            end = str(input("\n\nWhat do you want to do next? Reply \"replay\" to play a new game, reply \"menu\" to go back to the main menu or reply \"exit\" to quit the program: "))
            if end == "replay":
                isPlaying = True
                showMainMenu = True
                # Not really usefull, but we needed an indented block, and our IDE takes an empty block as en empty line, so we had to fill something in the block.
            elif end == "menu":
                isPlaying = False
            elif end == "exit":
                isPlaying = False
                showMainMenu = False
            else:
                isPlaying = False
    
    # We display the rules here
    elif choice == "about" or choice == "About" or choice == "info" or choice == "Info" or choice == "INFO" or choice == "ABOUT" or choice == "rules" or choice == "Rules" or choice == "RULES" or choice == "help" or choice == "Help" or choice == "HELP":
        print("\nMastermind is a code-breaking game for two players, it was invented in 1970 by Mordecai Meirowitz. The computer will be the codemaker, and the player will be the codebreaker. At the beginning of the game, the computer secretly chooses the code: a sequence of numbers (that can be repeated). The goal of the codebreaker will be to find this code by making successive attempts; for each try, a hypothesis will be provided by this player. Once the codebreaker finished proposing a hypothesis, the computer provides feedback by indicating—compared to the code—how many pegs of the right number are correctly placed (perfect pegs), and how many pegs of the right number are in the wrong place (partial pegs). If the player succeeds in finding the right code before exhausting this maximum number of attempts, he wins the game. Otherwise, the computer wins.\n\n")
    
    # We exit the loop to quit the program
    elif choice == "exit" or choice == "Exit" or choice == "HALT" or choice == "Halt" or choice == "HALT" or choice == "EXIT" or choice == "stop" or choice == "Stop" or choice == "STOP" or choice == "End" or choice == "end" or choice == "END":
        isPlaying = False
        showMainMenu = False
    else:
        print("Selection not recognized. Please try again.")

# End of the program, it's time to show the final scoreboard

if winG + lostG == 0:
    winG = 0
    lostG = 0
    # Not really usefull, but we needed an indented block, and our IDE takes an empty block as en empty line, so we had to fill something in the block.
else:
    print("\nThank you for playing Mastermind! On a total of ", winG + lostG, " games, you won ", winG, " of them and lost ", lostG, " of them. Bye!")

# Program ended.



