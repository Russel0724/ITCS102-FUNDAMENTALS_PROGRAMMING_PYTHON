

# Python Interactive Menu
# must include all the activities and code challenges
# about python

# modules
from Activities1 import *        #   * = all
from codechallenge import *
import os
import time
import sys

# clearscreen
def clear():
    os.system('cls' )

# design
def separator():
    print("\n\n","=" * 150,"\n\n")

# header
def title(title):
        print("\n\n","=" * 150, "\n\n",f"\t\t\t\t\t\t\t\t{title}","\n\n" ,"=" * 150)

# for delay
def pause():
    time.sleep(0.5)

# for the typing animation
def type_writer(text, speed=0.01):
    for mess in text:
        print(mess, end='', flush=True)
        time.sleep(speed)
    print()

# short message for the user
clear()
title("Main Menu")
separator()
type_writer("Welcome to the PyWorldProject(PWP), Adventurer!\nIn this Recorded World, You will Explore the History and Wonders of Python Programming Language\nMay your Journey Enlighen your Knowledge of Python Programming!")
separator()

# Name of the user
name = input("What shall I call you, Adventurer? --> ")

# If the user want to continue
while True:
    clear()
    title("Main Menu")
    separator()
    type_writer(f"Alright Adventurer do you wish to uncover and learn everything about python, Dear Adventurer {name}?")
    separator()
    welcome = input("What will be your choice Adventurer? (Y/N) --> ").upper()

    if welcome == "Y":
        clear()
        title("Main Menu")
        separator()
        type_writer("I like your determination Adventurer, you may now go\n\nJust press Enter to proceed...")
        separator()
        input()
        break

    elif welcome == "N":
        clear()
        title("Main Menu")
        separator()
        type_writer("I respect your decision Adventurer, May we meet again.")
        separator()
        pause()
        pause()
        clear()
        sys.exit()

    else:
        clear()
        title("Main Menu")
        separator()
        type_writer("There is no such option, Adventurer!\n\nPress Enter to go back...")
        separator()
        input()
        pause()
        clear()
        separator()
        type_writer("Please wait...")
        separator()
        pause()
        clear()
        separator()
        type_writer("Returning to Start...")
        separator()
        pause()
        continue

# for Name of the user
clear()
title("Main Menu")
separator()
type_writer(f"Welcome Adventurer {name} this is a Python Interactive Menu for you to explore!")
separator()
pause()
pause()

# First Choices
a = True
while a == True:
    clear()
    title("Main Menu")
    separator()
    type_writer("Where would you like to go, Adventurer?\n\n\tA - Archive Activities(Activities)\n\tB - Historical Challenges(CodeChallenges)\n\tC - Records & Documentation(Python Background)\n\tD - Depart(Exit)")
    separator()
    buff = input(f"What will be your choice Adventurer {name}? --> ").upper() # the user will input their choice

    # Activities Menu
    if buff == "A":
        while True:
            clear()
            title("Archive Activities (Activities)")
            separator()
            type_writer("Welcome to the world of my Activities, Adventurer!\nBelow are the different sets of Activities you can explore:\n\tA - Activities(1 - 9)\n\tB - Activities(10 - 18)\n\tC - Activities(19 - 25)\n\tD - Exit\n")
            separator()
            act = input("Your Choice --> ").upper()
            
            # activities(1 - 9)
            if act == "A":
                while True:
                    clear()
                    title("Archive Activities (Activities)")
                    separator()
                    type_writer(f"You have leveled up {name}, you can now access the lost remnants\nWelcome to the World 1 of the Activities, Adventurer!\n\tA - Activity1\n\tB - Activity2\n\tC - Activity3\n\tD - Activity4\n\tE - Activity5\n\tF - Activity6\n\tG - Activity7\n\tH - Activity8\n\tI - Activity9\n\tJ - Exit")
                    separator()
                    choi = input("Your Choice --> ").upper()

                    # activity 1
                    if choi == "A":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()                      
                        type_writer(f"\tYou Chose: {choi}\n\tRunning... {choi}\n")
                        separator()
                        mine1()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue
                
                    # activity 2
                    elif choi == "B":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer(f"\tYou Chose: {choi}\n\tRunning... {choi}\n")
                        separator()
                        mine2()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue

                    # activity 3
                    elif choi == "C":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer(f"\tYou Chose: {choi}\n\tRunning... {choi}\n")
                        separator()
                        mine3()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue

                    # activity 4
                    elif choi == "D":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer(f"\tYou Chose: {choi}\n\tRunning... {choi}\n")
                        separator()
                        mine4()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue
                
                    # activity 5
                    elif choi == "E":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer(f"\tYou Chose: {choi}\n\tRunning... {choi}\n")
                        separator()
                        mine5()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue
                
                    # activity 6
                    elif choi == "F":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer(f"\tYou Chose: {choi}\n\tRunning... {choi}\n")
                        separator()
                        mine6()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue

                    # activity 7
                    elif choi == "G":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer(f"\tYou Chose: {choi}\n\tRunning... {choi}\n")
                        separator()
                        mine7()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue
                
                    # activity 8
                    elif choi == "H":                        
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer(f"\tYou Chose: {choi}\n\tRunning... {choi}\n")
                        separator()
                        mine8()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue
                
                    # activity 9
                    elif choi == "I":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer(f"\tYou Chose: {choi}\n\tRunning... {choi}\n")
                        separator()
                        mine9()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue
                
                    # exit
                    elif choi == "J":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer("Are you sure you want to Exit Activities (1 - 9) Menu? (Y/N)")
                        separator()
                        in_chal = input("Your Choice --> ").upper()

                        if in_chal == "Y":
                            clear()
                            title("Archive Activities (Activities)")
                            separator()
                            type_writer("You have exited, nice meeting you Adventurer...")
                            separator()
                            pause()
                            break

                        elif in_chal == "N":
                            clear()
                            title("Archive Activities (Activities)")
                            separator()
                            type_writer("You have chosen to stay, you may browse further...")
                            separator()
                            pause()
                            continue
                
                        else:
                            clear()
                            title("Archive Activities (Activities)")
                            separator()
                            type_writer("There is no such option, Adventurer!\n\nPress Enter to choose again...")                                    
                            separator()
                            input()
                            pause()
                            continue
                
                    else:
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer("There is no such option, Adventurer!\n\nPress Enter to choose again...")                                    
                        separator()
                        input()
                        pause()
                        continue

            # activities(10 - 18)
            elif act == "B":
                while True:
                    clear()
                    title("Archive Activities (Activities)")
                    separator()
                    type_writer(f"You have leveled up {name}, you can now access the lost remnants\nWelcome to the World 2 of the Activities, Adventurer!\n\tA = Activity10\n\tB - Activity11\n\tC - Activity12\n\tD - Activity13\n\tE - Activity14\n\tF - Activity15\n\tG - Activity16\n\tH - Activity17\n\tI - Activity18\n\tJ- Exit")
                    separator()
                    choi = input("Your Choice --> ").upper()

                    # activity10
                    if choi == "A":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer(f"\tYou Chose: {choi}\n\tRunning... {choi}\n")
                        separator()
                        yours1()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue
                    
                    # activity11
                    elif choi == "B":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer(f"\tYou Chose: {choi}\n\tRunning... {choi}\n")
                        separator()
                        yours2()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue
                    
                    # activity12
                    elif choi == "C":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer(f"\tYou Chose: {choi}\n\tRunning... {choi}\n")
                        separator()
                        yours3()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue
                
                    # activity13
                    elif choi == "D":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer(f"\tYou Chose: {choi}\n\tRunning... {choi}\n")
                        separator()
                        yours4()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue

                    # activity14
                    elif choi == "E":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer(f"\tYou Chose: {choi}\n\tRunning... {choi}\n")
                        separator()
                        yours5()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue
                
                    # activity15
                    elif choi == "F":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer(f"\tYou Chose: {choi}\n\tRunning... {choi}\n")
                        separator()
                        yours6()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue

                    # activity16
                    elif choi == "G":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer(f"\tYou Chose: {choi}\n\tRunning... {choi}\n")
                        separator()
                        yours7()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue

                    # activity17
                    elif choi == "H":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer(f"\tYou Chose: {choi}\n\tRunning... {choi}\n")
                        separator()
                        yours8()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue

                    # activity18
                    elif choi == "I":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer(f"\tYou Chose: {choi}\n\tRunning... {choi}\n")
                        separator()
                        yours9()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue

                    # exit
                    elif choi == "J":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer("Are you sure you want to Exit Activities (10 - 18) Menu? (Y/N)")
                        separator()
                        in_chal = input("Your Choice --> ").upper()

                        if in_chal == "Y":
                            clear()
                            title("Archive Activities (Activities)")
                            separator()
                            type_writer("You have exited, nice meeting you Adventurer...")
                            separator()
                            pause()
                            break

                        elif in_chal == "N":
                            clear()
                            title("Archive Activities (Activities)")
                            separator()
                            type_writer("You have chosen to stay, you may browse further...")
                            separator()
                            pause()
                            continue
                
                        else:
                            clear()
                            title("Archive Activities (Activities)")
                            separator()
                            type_writer("There is no such option, Adventurer!\n\nPress Enter to choose again...")                                    
                            separator()
                            input()
                            pause()
                            continue

                    # invalid
                    else:
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer("There is no such option, Adventurer!\n\nPress Enter to choose again...")                                    
                        separator()
                        input()
                        pause()
                        continue

            # activities(19 - 25)
            elif act == "C":
                while True:
                    clear()
                    title("Archive Activities (Activities)")
                    separator()
                    type_writer(f"You have leveled up {name}, you can now access the lost remnants\nWelcome to the World 3 of the Activities, Adventurer!\n\tA - Activity19\n\tB - Activity20\n\tC - Activity21\n\tD - Activity22\n\tE - Activity23\n\tF - Activity24\n\tG - Activity25\n\tH - Exit")
                    separator()
                    choi = input("Your Choice --> ").upper()

                    # activity19
                    if choi == "A":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer(f"You Chose: {choi}\nRunning... {choi}")
                        separator()
                        them1()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue
                
                    # activity20
                    elif choi == "B":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer(f"You Chose: {choi}\nRunning... {choi}")
                        separator()
                        them2()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue

                    # activity21
                    elif choi == "C":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer(f"You Chose: {choi}\nRunning... {choi}")
                        separator()
                        them3()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue
                
                    # activity22
                    elif choi == "D":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer(f"You Chose: {choi}\nRunning... {choi}")
                        separator()
                        them4()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue
                
                    # activity23
                    elif choi == "E":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer(f"You Chose: {choi}\nRunning... {choi}")
                        separator()
                        them5()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue
                
                    # activity24
                    elif choi == "F":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer(f"You Chose: {choi}\nRunning... {choi}")
                        separator()
                        them6()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue
                
                    # activity25
                    elif choi == "G":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer(f"You Chose: {choi}\nRunning... {choi}")
                        separator()
                        them7()
                        separator()
                        type_writer("Press Enter to Exit Memory...")
                        separator()
                        input()
                        continue
                
                    # exit
                    elif choi == "H":
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer("Are you sure you want to Exit Activities (19 - 25) Menu? (Y/N)")
                        separator()
                        in_chal = input("Your Choice --> ").upper()

                        if in_chal == "Y":
                            clear()
                            title("Archive Activities (Activities)")
                            separator()
                            type_writer("You have exited, nice meeting you Adventurer...")
                            separator()
                            pause()
                            break

                        elif in_chal == "N":
                            clear()
                            title("Archive Activities (Activities)")
                            separator()
                            type_writer("You have chosen to stay, you may browse further...")
                            separator()
                            pause()
                            continue
                
                        else:
                            clear()
                            title("Archive Activities (Activities)")
                            separator()
                            type_writer("There is no such option, Adventurer!\n\nPress Enter to choose again...")                                    
                            separator()
                            input()
                            pause()
                            continue
                    
                    # invalid
                    else:
                        clear()
                        title("Archive Activities (Activities)")
                        separator()
                        type_writer("There is no such option, Adventurer!\n\nPress Enter to choose again...")                                    
                        separator()
                        input()
                        pause()
                        continue

            # exit
            elif act == "D":
                clear()
                title("Archive Activities (Activities)")
                separator()
                type_writer("Are you sure you want to Exit Activities Menu? (Y/N)")
                separator()
                in_chal = input("Your Choice --> ").upper()

                if in_chal == "Y":
                    clear()
                    title("Archive Activities (Activities)")
                    separator()
                    type_writer("You have exited, nice meeting you Adventurer...")
                    separator()
                    pause()
                    break

                elif in_chal == "N":
                    clear()
                    title("Archive Activities (Activities)")
                    separator()
                    type_writer("You have chosen to stay, you may browse further...")
                    separator()
                    pause()
                    continue
                
                else:
                    clear()
                    title("Archive Activities (Activities)")
                    separator()
                    type_writer("There is no such option, Adventurer!\n\nPress Enter to choose again...")                                    
                    separator()
                    input()
                    pause()
                    continue

            # invalid
            else:
                clear()
                title("Archive Activities (Activities)")
                separator()
                type_writer("There is no such option, Adventurer!\n\nPress Enter to choose again...")                                    
                separator()
                input()
                pause()
                continue

    # Code Challenges Menu
    elif buff == "B":
        while True:
            clear()
            title("Historical Challenges(CodeChallenges)")
            separator()
            type_writer("Welcome to the world of my Code Challenges, Adventurer!\nBelow are the different sets of CodeChallenges you can Review\n\tA - CodeChallenge1-5\n\tB - CodeChallenge6-10\n\tC - CodeChallenge11-15\n\tD - Exit")          
            separator()
            chal = input("Your Choice --> ").upper()

            # codechallenge(1 - 5)
            if chal == "A":
                while True:
                    clear()
                    title("Historical Challenges(CodeChallenges)")
                    separator()
                    type_writer(f"You have leveled up {name}, you can now access the lost remnants\nWelcome to the World 1 of the CodeChallenges, Adventurer!\n\tA - CodeChallenges1\n\tB - CodeChallenge2\n\tC - CodeChallenge3\n\tD - CodeChallenge4\n\tE - CodeChallenge5\n\tF - Exit")
                    separator()
                    ico = input("Your Choice --> ").upper()

                    # codechallenge1
                    if ico == "A":
                        clear()
                        title("Historical Challenges(CodeChallenges)")
                        separator()
                        type_writer(f"You Chose: {ico}\nRunning... {ico}")
                        separator()
                        from codechallenge import *
                        code1()
                        separator()
                        type_writer("Press Enter to Exit...")
                        input()
                        continue
                
                    # codechallenge2
                    elif ico == "B":
                        clear()
                        title("Historical Challenges(CodeChallenges)")
                        separator()
                        type_writer(f"You Chose: {ico}\nRunning... {ico}")
                        separator()
                        code2()
                        separator()
                        type_writer("Press Enter to Exit...")
                        input()
                        continue

                    # codechallenge3
                    elif ico == "C":
                        clear()
                        title("Historical Challenges(CodeChallenges)")
                        separator()
                        type_writer(f"You Chose: {ico}\nRunning... {ico}")
                        separator()
                        code3()
                        separator()
                        type_writer("Press Enter to Exit...")
                        input()
                        continue

                    # codechallenge4
                    elif ico == "D":
                        clear()
                        title("Historical Challenges(CodeChallenges)")
                        separator()
                        type_writer(f"You Chose: {ico}\nRunning... {ico}")
                        separator()
                        code4()
                        separator()
                        type_writer("Press Enter to Exit...")
                        input()
                        continue
                
                    # codechallenge5
                    elif ico == "E":
                        clear()
                        title("Historical Challenges(CodeChallenges)")
                        separator()
                        type_writer(f"You Chose: {ico}\nRunning... {ico}")
                        separator()
                        code5()
                        separator()
                        type_writer("Press Enter to Exit...")
                        input()
                        continue
                
                    # exit
                    elif ico == "F":
                        clear()
                        title("Historical Challenges(CodeChallenges)")
                        separator()
                        type_writer("Are you sure you want to Exit CodeChallenges (1 - 5) Menu? (Y/N)")
                        separator()
                        in_chal = input("Your Choice --> ").upper()

                        if in_chal == "Y":
                            clear()
                            title("Historical Challenges(CodeChallenges)")
                            separator()
                            type_writer("You have exited, nice meeting you Adventurer...")
                            separator()
                            pause()
                            break

                        elif in_chal == "N":
                            clear()
                            title("Historical Challenges(CodeChallenges)")
                            separator()
                            type_writer("You have chosen to stay, you may browse further...")
                            separator()
                            pause()
                            continue
                
                        else:
                            clear()
                            title("Historical Challenges(CodeChallenges)")
                            separator()
                            type_writer("There is no such option, Adventurer!\n\nPress Enter to choose again...")                                    
                            separator()
                            input()
                            pause()
                            continue

                    # invalid
                    else:
                        clear()
                        title("Historical Challenges(CodeChallenges)")
                        separator()
                        type_writer("There is no such option, Adventurer!\n\nPress Enter to choose again...")                                    
                        separator()
                        input()
                        pause()
                        continue

            # codechallenge(6 - 10)
            elif chal == "B":
                while True:
                    clear()
                    title("Historical Challenges(CodeChallenges)")
                    separator()
                    type_writer(f"You have leveled up {name}, you can now access the lost remnants\nWelcome to the World 2 of the CodeChallenges, Adventurer!\n\tA = CodeChallenge6\n\tB - CodeChallenge7\n\tC - CodeChallenge8\n\tD - CodeChallenge9\n\tE - CodeChallenge10\n\tF - Exit")
                    separator()
                    ico = input("Your Choice --> ").upper()

                    # codechallenge6
                    if ico == "A":
                        clear()
                        title("Historical Challenges(CodeChallenges)")
                        separator()
                        type_writer(f"You Chose: {ico}\nRunning... {ico}")
                        separator()
                        core1()
                        separator()
                        type_writer("Press Enter to Exit...")
                        input()
                        continue
                        
                    # codechallenge7
                    elif ico == "B":
                        clear()
                        title("Historical Challenges(CodeChallenges)")
                        separator()
                        type_writer(f"You Chose: {ico}\nRunning... {ico}")
                        separator()
                        core2()
                        separator()
                        type_writer("Press Enter to Exit...")
                        input()
                        continue

                    # codechallenge8
                    elif ico == "C":
                        clear()
                        title("Historical Challenges(CodeChallenges)")
                        separator()
                        type_writer(f"You Chose: {ico}\nRunning... {ico}")
                        separator()
                        core3()
                        separator()
                        type_writer("Press Enter to Exit...")
                        input()
                        continue
                
                    # codechallenge9
                    elif ico == "D":
                        clear()
                        title("Historical Challenges(CodeChallenges)")
                        separator()
                        type_writer(f"You Chose: {ico}\nRunning... {ico}")
                        separator()
                        core4()
                        separator()
                        type_writer("Press Enter to Exit...")
                        input()
                        continue
                
                    # codechallenge10
                    elif ico == "E":
                        clear()
                        title("Historical Challenges(CodeChallenges)")
                        separator()
                        type_writer(f"You Chose: {ico}\nRunning... {ico}")
                        separator()
                        core5()
                        separator()
                        type_writer("Press Enter to Exit...")
                        input()
                        continue
            
                    # exit
                    elif ico == "F":
                        clear()
                        title("Historical Challenges(CodeChallenges)")
                        separator()
                        type_writer("Are you sure you want to Exit CodeChallenges (6 - 10) Menu? (Y/N)")
                        separator()
                        in_chal = input("Your Choice --> ").upper()

                        if in_chal == "Y":
                            clear()
                            title("Historical Challenges(CodeChallenges)")
                            separator()
                            type_writer("You have exited, nice meeting you Adventurer...")
                            separator()
                            pause()
                            break

                        elif in_chal == "N":
                            clear()
                            title("Historical Challenges(CodeChallenges)")
                            separator()
                            type_writer("You have chosen to stay, you may browse further...")
                            separator()
                            pause()
                            continue
                
                        else:
                            clear()
                            title("Historical Challenges(CodeChallenges)")
                            separator()
                            type_writer("There is no such option, Adventurer!\n\nPress Enter to choose again...")                                    
                            separator()
                            input()
                            pause()
                            continue

                    # invalid
                    else:
                        clear()
                        title("Historical Challenges(CodeChallenges)")
                        separator()
                        type_writer("There is no such option, Adventurer!\n\nPress Enter to choose again...")                                    
                        separator()
                        input()
                        pause()
                        continue

            # codechallenge(11 - 15)
            elif chal == "C":
                while True:
                    clear()
                    title("Historical Challenges(CodeChallenges)")
                    separator()
                    type_writer(f"You have leveled up {name}, you can now access the lost remnants\nWelcome to the World 3 of the CodeChallenges, Adventurer!\n\tA = CodeChallenge11\n\tB - CodeChallenge12\n\tC - CodeChallenge13\n\tD - CodeChallenge14\n\tE - CodeChallenge15\n\tF - Exit")
                    separator()
                    ico = input("Your Choice --> ").upper()

                    # codechallenge11
                    if ico == "A":
                        clear()
                        title("Historical Challenges(CodeChallenges)")
                        separator()
                        type_writer(f"You Chose: {ico}\nRunning... {ico}")
                        separator()
                        care1()
                        separator()
                        type_writer("Press Enter to Exit...")
                        input()
                        continue
                
                    # codechallenge12
                    elif ico == "B":
                        clear()
                        title("Historical Challenges(CodeChallenges)")
                        separator()
                        type_writer(f"You Chose: {ico}\nRunning... {ico}")
                        separator()
                        care2()
                        separator()
                        type_writer("Press Enter to Exit...")
                        input()
                        continue

                    # codechallenge13
                    elif ico == "C":
                        clear()
                        title("Historical Challenges(CodeChallenges)")
                        separator()
                        type_writer(f"You Chose: {ico}\nRunning... {ico}")
                        separator()
                        care3()
                        separator()
                        type_writer("Press Enter to Exit...")
                        input()
                        continue
                
                    # codechallenge14
                    elif ico == "D":
                        clear()
                        title("Historical Challenges(CodeChallenges)")
                        separator()
                        type_writer(f"You Chose: {ico}\nRunning... {ico}")
                        separator()
                        care4()
                        separator()
                        type_writer("Press Enter to Exit...")
                        input()
                        continue
                
                    # codechallenge15
                    elif ico == "E":
                        clear()
                        title("Historical Challenges(CodeChallenges)")
                        separator()
                        type_writer(f"You Chose: {ico}\nRunning... {ico}")
                        separator()
                        care5()
                        separator()
                        type_writer("Press Enter to Exit...")
                        input()
                        continue
                
                    # exit
                    elif ico == "F":
                        clear()
                        title("Historical Challenges(CodeChallenges)")
                        separator()
                        type_writer("Are you sure you want to Exit CodeChallenges (11 - 15) Menu? (Y/N)")
                        separator()
                        in_chal = input("Your Choice --> ").upper()

                        if in_chal == "Y":
                            clear()
                            title("Historical Challenges(CodeChallenges)")
                            separator()
                            type_writer("You have exited, nice meeting you Adventurer...")
                            separator()
                            pause()
                            break

                        elif in_chal == "N":
                            clear()
                            title("Historical Challenges(CodeChallenges)")
                            separator()
                            type_writer("You have chosen to stay, you may browse further...")
                            separator()
                            pause()
                            continue
                
                        else:
                            clear()
                            title("Historical Challenges(CodeChallenges)")
                            separator()
                            type_writer("There is no such option, Adventurer!\n\nPress Enter to choose again...")                                    
                            separator()
                            input()
                            pause()
                            continue
                    
                    # invalid
                    else:
                        clear()
                        title("Historical Challenges(CodeChallenges)")
                        separator()
                        type_writer("There is no such option, Adventurer!\n\nPress Enter to choose again...")                                    
                        separator()
                        input()
                        pause()
                        continue

            # Exit
            elif chal == "D":
                clear()
                title("Historical Challenges(CodeChallenges)")
                separator()
                type_writer("Are you sure you want to Exit CodeChallenges Menu? (Y/N)")
                separator()
                in_chal = input("Your Choice --> ").upper()

                if in_chal == "Y":
                    clear()
                    title("Historical Challenges(CodeChallenges)")
                    separator()
                    type_writer("You have exited, nice meeting you Adventurer...")
                    separator()
                    pause()
                    break

                elif in_chal == "N":
                    clear()
                    title("Historical Challenges(CodeChallenges)")
                    separator()
                    type_writer("You have chosen to stay, you may browse further...")
                    separator()
                    pause()
                    continue
                
                else:
                    clear()
                    title("Historical Challenges(CodeChallenges)")
                    separator()
                    type_writer("There is no such option, Adventurer!\n\nPress Enter to choose again...")                                    
                    separator()
                    input()
                    pause()
                    continue

            
            # invalid
            else:
                clear()
                title("Historical Challenges(CodeChallenges)")
                separator()
                type_writer("There is no such option, Adventurer!\n\nPress Enter to choose again...")                                    
                separator()
                input()
                pause()
                continue

    # Guide Menu
    elif buff == "C":
        while True:
            clear()
            title("Records & Documentation(Python Background)")
            separator()
            type_writer(f"Welcome to the Guide Menu, Adventurer {name}!\nI will be your Guide to the different Realms of Python Programming Language\nChoose a Realm to Explore:\n\n\tA - Built-In Functions Realm\n\tB - Data Types Realm\n\tC - Control Structures Realm\n\tD - Variables & Operators Realm\n\tE - Functions Realm\n\tF - Modules & Import Realm\n\tG - Depart") # Menu for Guide
            separator()
            gui = input("Your Choice --> ").upper()

            # BuiltIn Functions Guide
            if gui == "A":
                while True:
                    clear()
                    title("Records & Documentation(Python Background)")
                    separator()
                    type_writer("You have chosen Built-In Functions Guide Realm\nHere are the things you can learn about Built-In Functions in Python:\n\tA - print()\n\tB - input()\n\tC - len()\n\tD - type()\n\tE - int(), float(), str()\n\tF - range()\n\tG - sum()\n\tH - Exit") # Menu for BuiltIn Functions
                    separator()
                    cream = input("Your Choice --> ").upper()

                    if cream == "A":
                        while True:
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("You have chosen the path of print() function\nWhat would you like to know about print() function?\n\t1 - Description\n\t2 - Syntax\n\t3 - Examples\n\t4 - Exit")
                            separator()
                            in_choice = input("Your Choice --> ")
                        
                            if in_choice == "1":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Here is a brief overview of the print() function:\n\n\tThe print() function is used to output text or other data to the console.\n\nPress Enter to go back...")                                 
                                separator()
                                input()
                                pause()
                                continue

                            elif in_choice == "2":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Here is the syntax of the print() function:\n\nprint(*objects, sep=' ', end='\\n', file=sys.stdout, flush=False)\n\nPress Enter to go back...")
                                separator()
                                input()
                                pause()
                                continue

                            elif in_choice == "3":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Here are some examples of the print() function:\n\nExample 1:\n\tprint('Hello, World!')\n\n\tOutput: Hello World!\n\nDo you want to see more examples? (Y/N)")
                                separator()
                                other_ex = input("Your Choice --> ").upper()

                                if other_ex == "Y":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Here are more examples of the print() function:\nExample 2:\n\tprint('Hello', 'World', sep='-')\n\n\tOutput: Hello-World\n\nExample 3:\n\tprint('Hello', end='!,'World')\n\n\tOutput: Hello! World\n\nPress Enter to go back...")
                                    separator()
                                    input()
                                    pause()
                                    continue

                                elif other_ex == "N":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Alright, thanks for checking in!...\nPress Enter to exit...")
                                    separator()
                                    input()
                                    pause()
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Returning to print() function Menu...")
                                    separator()
                                    pause()
                                    continue

                                else:
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("There is no such option, Adventurer!\n\nPress Enter to choose again...")                                    
                                    separator()
                                    input()
                                    pause()
                                    continue
                            
                            elif in_choice == "4":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Are you sure you want to exit print() function Guide? (Y/N)")
                                separator()
                                exit_inp = input("Your Choice --> ").upper()

                                if exit_inp == "Y":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Exiting print() function Guide...\nPlease wait...")
                                    separator()
                                    pause()
                                    break

                                elif exit_inp == "N":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Returning to print() function Menu...")
                                    separator()
                                    pause()
                                    continue

                                else:
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("There is no such option, Adventurer!\n\nPress Enter to go back...")
                                    separator()
                                    input()
                                    pause()
                                    continue

                            else:
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("There is no such option, Adventurer!\n\nPress Enter to go back...")
                                separator()
                                input()
                                pause()
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Returning to print() function Menu...")
                                separator()
                                pause()
                                continue
                        
                    elif cream == "B":
                        while True:
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("You have chosen the path of input() function\nWhat would you like to know about input() function?\n\t1 - Description\n\t2 - Syntax\n\t3 - Examples\n\t4 - Depart")
                            separator()
                            in_choice = input("Your Choice --> ")

                            if in_choice == "1":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Here is a brief overview of the input() function:\n\n\tThe input() function in Python allows users to provide input during program execution.\n\tIt pauses the program, waits for user input, and returns the input as a string.\n\nPress Enter to go back...")
                                separator()
                                input()
                                continue

                            elif in_choice == "2":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Here is the syntax of the input() function:\n\n\tinput(prompt)\n\nPress Enter to go back...")
                                separator()
                                input()
                                continue

                            elif in_choice == "3":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Here are some examples of the input() function:\n\nExample 1:\n\tname = input('Enter your name: ')\n\n\tOutput: Enter your name: (pauses the program and waits for the user to input something)\n\nDo you want to see more examples? (Y/N)")
                                separator()
                                other_ex = input("Your Choice --> ").upper()

                                if other_ex == "Y":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Here are more examples of the input() function:\n\nExample 2:\n\tage = input('Enter your age: ')\n\n\tOutput: Enter your age: (pauses the program and waits for the user to input something)\n\nExample 3:\n\tnumber = input('Enter a number: ')\n\n\tOutput: Enter a number: (pauses the program and waits for the user to input something)\n\nPress Enter to go back...")
                                    separator()
                                    input()
                                    continue

                                elif other_ex == "N":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Alright, thanks for checking in!...\n\nPress Enter to exit...")
                                    separator()
                                    input()
                                    pause()
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Returning to input() function Menu...")
                                    separator()
                                    pause()
                                    continue

                                else:
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("There is no such option, Adventurer!\n\nPress Enter to choose again...")
                                    separator()
                                    input()
                                    continue

                            elif in_choice == "4":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Are you sure you want to exit input() function Guide? (Y/N)")
                                separator()
                                exit_inp = input("Your Choice --> ").upper()
                                
                                if exit_inp == "Y":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Exiting input() function Guide...\nPlease wait...")
                                    separator()
                                    pause()
                                    break

                                elif exit_inp == "N":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Returning to input() function Menu...")
                                    separator()
                                    pause()
                                    continue

                                else:
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("There is no such option, Adventurer!\n\nPress Enter to go back...")
                                    separator()
                                    input()
                                    continue
                            
                            else:
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("There is no such option, Adventurer!\n\nPress Enter to go back...")
                                separator()
                                input()
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Returning to input() function Menu...")
                                separator()
                                pause()
                                continue

                    elif cream == "C":
                        while True:
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("You have chosen the path of len() function\n\nWhat would you like to know about len() function?\n\t1 - Description\n\t2 - Syntax\n\t3 - Examples\n\t4 - Exit")
                            separator()
                            in_choice = input("Your Choice --> ")
                        
                            if in_choice == "1":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Here is a brief overview of the len() function:\n\n\tThe len() function returns the number of items in an object.\n\nPress Enter to go back...")
                                separator()
                                input()
                                continue

                            elif in_choice == "2":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Here is the syntax of the len() function:\n\n\tlen(object)\n\nPress Enter to go back...")
                                separator()
                                input()
                                continue

                            elif in_choice == "3":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Here are some examples of the len() function:\n\nExample 1:\n\tlen('Hello')\n\n\tOutput: 5\n\nDo you want to see more examples? (Y/N)")
                                separator()
                                other_ex = input("Your Choice --> ").upper()

                                if other_ex == "Y":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Here are more examples of the len() function:\n\nExample 2:\n\tlen([1, 2, 3, 4])\n\n\tOutput: 4\n\n\Example 3:\n\tlen((1, 2, 3))\n\n\tOutput: 3\n\nPress Enter to go back...")
                                    separator()
                                    input()
                                    continue

                                elif other_ex == "N":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Alright, thanks for checking in!...\n\nPress Enter to exit...")
                                    separator()
                                    input()
                                    pause()
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Returning to len() function Menu...")
                                    separator()
                                    continue

                                else:
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("There is no such option, Adventurer!\n\nPress Enter to choose again...")
                                    separator()
                                    input()
                                    continue
                            
                            elif in_choice == "4":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Are you sure you want to exit len() function Guide? (Y/N)")
                                separator()
                                exit_inp = input("Your Choice --> ").upper()

                                if exit_inp == "Y":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Exiting len() function Guide...\n\nPlease wait...")
                                    separator()
                                    pause()
                                    break

                                elif exit_inp == "N":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Returning to len() function Menu...")
                                    separator()
                                    pause()
                                    continue

                                else:
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("There is no such option, Adventurer!\n\nPress Enter to go back...")
                                    separator()
                                    input()
                                    pause()
                                    continue

                            else:
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("There is no such option, Adventurer!\n\n Enter to go back...")
                                separator()
                                input()
                                pause()
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Returning to len() function Menu...")
                                separator()
                                pause()
                                continue

                    elif cream == "D":
                        while True:
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            print("You have chosen the path of type() function\nWhat would you like to know about type() function?\n\t1 - Description\n\t2 - Syntax\n\t3 - Examples\n\t4 - Exit")
                            separator()
                            in_choice = input("Your Choice --> ")
                        
                            if in_choice == "1":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Here is a brief overview of the type() function:\n\tThe type() function returns the type of an object.\n\nPress Enter to go back...")
                                separator()
                                input()
                                continue

                            elif in_choice == "2":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Here is the syntax of the type() function:\n\ttype(object)\n\nPress Enter to go back...")
                                separator()
                                input()
                                continue

                            elif in_choice == "3":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Here are some examples of the type() function:\nExample 1:\n\ttype(5)\n\n\tOutput: <class 'int'>\n\nDo you want to see more examples? (Y/N)")
                                separator()
                                other_ex = input("Your Choice --> ").upper()

                                if other_ex == "Y":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Here are more examples of the type() function:\nExample 2:\n\ttype(3.14)\n\n\tOutput: <class 'float'>\n\nExample 3:\n\ttype('Hello')\n\n\tOutput: <class 'str'>\n\nPress Enter to go back...")
                                    separator()
                                    input()
                                    continue

                                elif other_ex == "N":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Alright, thanks for checking in!...\n\nPress Enter to exit...")
                                    separator()
                                    input()
                                    pause()
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Returning to type() function Menu...")
                                    separator()
                                    pause()
                                    continue

                                else:
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("There is no such option, Adventurer!\n\nPress Enter to choose again...")
                                    separator()
                                    input()
                                    pause()
                                    continue

                            elif in_choice == "4":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Are you sure you want to exit type() function Guide? (Y/N)")
                                separator()
                                exit_inp = input("Your Choice --> ").upper()

                                if exit_inp == "Y":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Exiting type() function Guide...\nPlease wait...")
                                    separator()
                                    pause()
                                    break

                                elif exit_inp == "N":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Returning to type() function Menu...")
                                    separator()
                                    pause()
                                    continue

                                else:
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("There is no such option, Adventurer!\n\nPress Enter to go back...")
                                    separator()
                                    input()                                    
                                    continue

                            else:
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("There is no such option, Adventurer!\n\nPress Enter to go back...")
                                separator()
                                input()
                                pause()
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Returning to type() function Menu...")
                                separator()
                                pause()
                                continue

                    elif cream == "E":
                        while True:
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("You have chosen the path of int(), float(), str() functions\nWhat would you like to know about int(), float(), str() functions?\n\t1 - Description\n\t2 - Syntax\n\t3 - Examples\n\t4 - Exit")
                            separator()
                            in_choice = input("Your Choice --> ")

                            if in_choice == "1":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Here is a brief overview of the int(), float(), str() functions:\n\n\tThe int() function converts a value to an integer.\n\tThe float() function converts a value to a floating-point number.\n\tThe str() function converts a value to a string.\n\nPress Enter to go back...")
                                separator()
                                input()
                                continue

                            elif in_choice == "2":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Here is the syntax of the int(), float(), str() functions:\n\n\tint(x)\n\tfloat(x)\n\tstr(x)\n\nPress Enter to go back...")
                                separator()
                                input()
                                continue

                            elif in_choice == "3":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Here are some examples of the int(), float(), str() functions:\nExample 1:\n\tint('5')\n\n\tOutput: 5\n\nDo you want to see more examples? (Y/N)")
                                separator()
                                other_ex = input("Your Choice --> ").upper()

                                if other_ex == "Y":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Here are more examples of the int(), float(), str() functions:\nExample 2:\n\tfloat('3.14')\n\n\tOutput: 3.14\n\nExample 3:\n\tstr(100)\n\n\tOutput: '100'\n\nPress Enter to go back...")
                                    separator()
                                    input()
                                    continue

                                elif other_ex == "N":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Alright, thanks for checking in!...\n\nPress Enter to exit...")
                                    separator()
                                    input()
                                    pause()
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Returning to int(), float(), str() functions Menu...")
                                    separator()
                                    pause()
                                    continue

                                else:
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("There is no such option, Adventurer!\n\nPress Enter to choose again...")
                                    separator()
                                    input()
                                    continue

                            elif in_choice == "4":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Are you sure you want to exit int(), float(), str() functions Guide? (Y/N)")
                                separator()
                                exit_inp = input("Your Choice --> ").upper()

                                if exit_inp == "Y":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Exiting int(), float(), str() functions Guide...\nPlease wait...")
                                    separator()
                                    pause()
                                    break

                                elif exit_inp == "N":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Returning to int(), float(), str() functions Menu...")
                                    separator()
                                    pause()
                                    continue

                                else:
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("There is no such option, Adventurer!\n\nPress Enter to go back...")
                                    separator()
                                    input()
                                    continue

                            else:
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("There is no such option, Adventurer!\n\nPress Enter to go back...")
                                separator()
                                input()
                                pause()
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Returning to int(), float(), str() functions Menu...")
                                separator()
                                pause()
                                continue
                    
                    elif cream == "F":
                        while True:
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            print("You have chosen the path of range() function\nWhat would you like to know about range() function?\n\t1 - Description\n\t2 - Syntax\n\t3 - Examples\n\t4 - Exit")
                            separator()
                            in_choice = input("Your Choice --> ")
                            
                            if in_choice == "1":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Here is a brief overview of the range() function:\n\n\tThe range() function generates a sequence of numbers within a specified range.\n\nPress Enter to go back...")
                                separator()
                                input()
                                continue

                            elif in_choice == "2":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Here is the syntax of the range() function:\n\n\trange(start, stop[, step])\n\nPress Enter to go back...")
                                separator()
                                input()
                                continue

                            elif in_choice == "3":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Here are some examples of the range() function:\nExample 1: range(5)\n\n\tOutput: 0, 1, 2, 3, 4\n\nDo you want to see more examples? (Y/N)")
                                separator()
                                other_ex = input("Your Choice --> ").upper()

                                if other_ex == "Y":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    print("Here are more examples of the range() function:\nExample 2:\n\trange(1, 10, 2)\n\n\tOutput: 1, 3, 5, 7, 9\n\nExample 3:\n\trange(10, 0, -1)\n\n\tOutput: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1\n\nPress Enter to go back...")
                                    separator()
                                    input()
                                    continue

                                elif other_ex == "N":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Alright, thanks for checking in!...\n\n Press Enter to exit...")
                                    separator()
                                    input()
                                    pause()
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Returning to range() function Menu...")
                                    separator()
                                    continue

                                else:
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("There is no such option, Adventurer!\n\nPress Enter to choose again...")
                                    separator()
                                    input()
                                    continue

                            elif in_choice == "4":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Are you sure you want to exit range() function Guide? (Y/N)")
                                separator()
                                exit_inp = input("Your Choice --> ").upper()

                                if exit_inp == "Y":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Exiting range() function Guide...\nPlease wait...")
                                    separator()
                                    pause()
                                    break

                                elif exit_inp == "N":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Returning to range() function Menu...")
                                    separator()
                                    continue

                                else:
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("There is no such option, Adventurer!\n\nPress Enter to go back...")
                                    separator()
                                    input()
                                    continue

                            else:
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("There is no such option, Adventurer!\n\nPress Enter to go back...")
                                separator()
                                input()
                                pause()
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Returning to range() function Menu...")
                                separator()
                                pause()
                                continue

                    elif cream == "G":
                        while True:
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("You have chosen the path of sum() function\nWhat would you like to know about sum() function?\n\t1 - Description\n\t2 - Syntax\n\t3 - Examples\n\t4 - Exit")
                            separator()
                            in_choice = input("Your Choice --> ")

                            if in_choice == "1":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Here is a brief overview of the sum() function:\n\n\tThe sum() function returns the sum of all items in an iterable.\n\nPress Enter to go back...")
                                separator()
                                input()
                                pause()
                                continue

                            elif in_choice == "2":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Here is the syntax of the sum() function:\nsum(iterable, start)\n\titerable → A sequence or collection of numbers (list, tuple, set, etc.).\n\tstart (optional) → A value to add to the sum (default is 0).\n\nPress Enter to go back...")
                                separator()
                                input()
                                pause()
                                continue

                            elif in_choice == "3":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Here are some examples of the sum() function:\nExample 1:\n\tnumbers = [1, 2, 3, 4]\n\ttotal = sum(numbers)\n\tprint(total)\n\n\tOutput: 10\n\nDo you want to see more examples? (Y/N)")
                                separator()
                                other_ex = input("Your Choice --> ").upper()

                                if other_ex == "Y":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Here are more examples of the sum() function:\nExample 2:\n\tnumbers = [1, 2, 3, 4]\n\ttotal_with_start = sum(numbers, 10)\n\tprint(total_with_start)\n\n\tOutput: 20\n\nExample 3:\n\tprint(sum((5, 15, 25)))\n\n\tOutput: 45\n\nPress Enter to go back...")
                                    separator()
                                    input()
                                    pause()
                                    continue

                                elif other_ex == "N":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Alright, thanks for checking in!...\n\nPress Enter to exit...")
                                    separator()
                                    input()
                                    pause()
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Returning to sum() function Menu...")
                                    separator
                                    pause()
                                    continue

                                else:
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("There is no such option, Adventurer!\n\nPress Enter to choose again...")
                                    separator()
                                    input()
                                    continue

                            elif in_choice == "4":
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Are you sure you want to exit range() function Guide? (Y/N)")
                                separator
                                exit_inp = input("Your Choice --> ").upper()

                                if exit_inp == "Y":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer ("Exiting sum() function Guide...\nPlease wait...")
                                    separator()
                                    pause()
                                    break

                                elif exit_inp == "N":
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("Returning to sum() function Menu...")
                                    separator()
                                    pause()
                                    continue

                                else:
                                    clear()
                                    title("Records & Documentation(Python Background)")
                                    separator()
                                    type_writer("There is no such option, Adventurer!\n\nPress Enter to go back...")
                                    separator()
                                    input()
                                    pause()
                                    continue

                            else:
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("There is no such option, Adventurer!\nPress Enter to go back...")
                                separator()
                                input()
                                pause()
                                clear()
                                title("Records & Documentation(Python Background)")
                                separator()
                                type_writer("Returning to sum() function Menu...")
                                separator()
                                pause()
                                continue
                            
                    elif cream == "H":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("Are you sure you want to Exit Built-In Functions Realm?")
                        separator()
                        in_cream = input("Your Choice? (Y/N) --> ").upper()

                        if in_cream == "Y":
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("Thank you for exploring the Built-In Functions Realm, Adventurer!\nExiting Menu...")
                            separator()
                            pause()
                            break

                        elif in_cream == "N":
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("Returning to Built-In Function Realm\n\nPress Enter to proceed")
                            separator()
                            input()
                            continue

                        else:
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("There is no such option, Adventurer!\n\nPress Enter to go back...")
                            separator()
                            input()
                            pause()
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("Please wait...")
                            separator()
                            pause()
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("Returning to Built-In Functions Realm...")
                            separator()
                            pause()
                            continue

                    else:
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("There is no such option, Adventurer!\nPress Enter to go back...")
                        separator()
                        input()
                        pause()
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("Please wait...")
                        separator()
                        pause()
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("Returning to Built-In Functions Realm")
                        separator()
                        pause()
                        continue

            elif gui == "B":
                while True:
                    clear()
                    title("Records & Documentation(Python Background)")
                    separator()
                    type_writer("You have chosen Data Types Realm\nHere are some of the Data Types in Python:\n\tA - int\n\tB - float\n\tC - str\n\tD - list\n\tE - dict\n\tF - set\n\tG - bool\n\tH - Exit")
                    separator()
                    cream = input("Your Choice --> ").upper()

                    if cream == "A":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("You have chosen the int Data Type\n\nThe int data type stands for integer, which means it stores whole numbers (no decimal or fractional part).\n\n\tAn integer data type represents some range of mathematical integers.\n\tIntegral data types may be of different sizes and may or may not be allowed to contain negative values.\n\tIntegers are commonly represented in a computer as a group of binary digits (bits).\n\tThe size of the grouping varies so the set of integer sizes available varies between different types of computers and different programming languages\n\nPress Enter to go back...")
                        separator()
                        input()
                        continue

                    elif cream == "B":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("You have chosen the float Date Type\n\nA float (short for floating-point number) is a data type used in programming to store real numbers — numbers that can have a fractional (decimal) part.\n\n\tThe float data type is used to represent floating-point numbers, which are numbers with decimal points.\n\tIt is a fundamental numeric type in many programming languages, including Python, C++, Java, and C#.\n\tFloats are particularly useful for representing real numbers in scenarios where precision is not critical.\n\nPress Enter to go back...")
                        separator()
                        input()
                        continue

                    elif cream == "C":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("You have chosen the str Data Type\n\nThe str data type refers to a string, which is a sequence of characters used to represent text.\n\n\tIn Python, the str data type represents an immutable sequence of Unicode characters used for storing and manipulating textual data.\n\tIt is one of Python’s built-in data types and belongs to the sequence type category.\n\n\tA string can be created using single quotes, double quotes, or triple quotes for multi-line text.\n\tPython does not have a separate character type — a single character is simply a string of length one.\n\nPress Enter to go back...")
                        separator()
                        input()
                        continue

                    elif cream == "D":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("You have chosen the list Data Type\n\nA list is a collection of items that are ordered, changeable, and allow duplicate values.\nLists are widely used in programming for storing and managing data.\n\n\tCreation: Use square brackets [] to create a list.\n\n\t\tExample: my_list = ['apple', 'banana', 'cherry'].\n\n\tAccessing Items: Use indexing to access items. Index starts at 0.\n\n\t\tExample: my_list[0] returns 'apple'.\n\n\tModifying Items: Assign a new value to a specific index to modify it.\n\n\t\tExample: my_list[1] = 'orange' changes 'banana' to 'orange'.\n\n\tAdding Items: Use .append() to add an item at the end. Use .insert(index, item) to add an item at a specific position.\n\n\tRemoving Items: Use .remove(item) to delete a specific item. Use .pop(index) to remove an item by index. Use .clear() to remove all items.\n\n\tSlicing: Extract portions of a list using slicing: my_list[start:stop:step].\n\n\t\tExample: my_list[1:3] returns a sublist.\n\n\tIterating: Use a for loop to iterate through the list.\n\n\t\tExample: for item in my_list: print(item).\n\n\tSorting: Use .sort() to sort the list in place. Use sorted(list) to return a new sorted list.\n\n\tCopying: Use slicing [:] or .copy() to create a shallow copy. Use copy.deepcopy() for a deep copy.\n\n\tNested Lists: Lists can contain other lists.\n\n\t\tExample: nested_list = [[1, 2], [3, 4]].\n\n\tCommon Operations: len(list) to get the number of items. list.count(item) to count occurrences of an item. list.index(item) to find the index of an item.\n\n\tAdvanced Features: Lists support concatenation (+) and repetition (*).\n\n\t\tExample: [1, 2] + [3, 4] results in [1, 2, 3, 4].\n\n\tUse Cases: Lists are ideal for ordered collections where duplicates are allowed and frequent modifications are needed.\n\nPress Enter to go back...")
                        separator()
                        input()
                        continue

                    elif cream == "E":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("You have chosen the dict Data Type\n\nThe dict (short for dictionary) is a built-in data type used to store key–value pairs.\n\n\tStructure: { key: value, key2: value2, ... }\n\n\tKeys: Must be unique and immutable (e.g., strings, numbers, tuples).\n\n\tValues: Can be of any data type and can be duplicated.\n\n\tOrder: As of Python 3.7+, dictionaries maintain insertion order.\n\n\tMutable: You can add, update, or remove items after creation.\n\nPress Enter to go back...")
                        separator()
                        input()
                        continue

                    elif cream == "F":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("You have chosen the set Data Type\n\nA set is a built-in data type that represents an unordered collection of unique elements\n\n\tUnordered – The elements have no fixed position or index.\n\n\tUnique Elements – Duplicate values are automatically removed.\n\n\tMutable – You can add or remove elements after creation.\n\n\tHeterogeneous – Can store different data types (e.g., integers, strings, tuples), but elements must be hashable (lists and dictionaries cannot be elements).\n\nPress Enter to go back...")
                        separator()
                        input()
                        continue

                    elif cream == "G":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("You have chosen the bool Data Type\n\nThe bool (Boolean) data type represents one of two possible truth values:\n\n\t\tTrue\n\n\t\tFalse\n\n\tThese are used to express logical conditions and control program flow.\n\nIn Python, the Boolean type (bool) is a built-in data type that can hold one of two values: True or False.\n\n\tIt is fundamental for decision-making in programs, as it represents the truth value of expressions and controls the flow of execution.\n\n\tA Boolean value is often the result of a comparison or logical operation, but it can also be assigned directly\n\nPress Enter to go back...")
                        separator()
                        input()
                        continue

                    elif cream == "H":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("Are you sure you want to Exit Data Types Realm?")
                        separator()
                        in_cream = input("Your Choice? (Y/N) --> ").upper()

                        if in_cream == "Y":
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("Thank you for exploring the Data Types Realm, Adventurer!\nExiting Menu...")
                            separator()
                            pause()
                            break

                        elif in_cream == "N":
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("Returning to Data Types Realm\n\nPress Enter to proceed...")
                            separator()
                            input()
                            continue

                        else:
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("There is no such option, Adventurer!\n\nPress Enter to go back...")
                            separator()
                            input()
                            pause()
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("Please wait...")
                            separator()
                            pause()
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("Returning to Data Types Realm...")
                            separator()
                            pause()
                            continue

            elif gui == "C":
                while True:
                    clear()
                    title("Records & Documentation(Python Background)")
                    separator()
                    type_writer("You have chosen Control Structures Realm\n\nHere are some of the Control Structures in Python:\n\tA - if, elif, else statements\n\tB - for loops\n\tC - while loops\n\tD - break and continue statements\n\tE - try and except blocks\n\tF - Exit")
                    separator()
                    cream = input("Your Choice --> ").upper()

                    if cream == "A":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("You have chosen if, elif, else statements\n\nYou can have multiple elif blocks, but only one else block at the end.\nConditions are evaluated top to bottom, stopping at the first match.\nIndentation is crucial in Python; each block must be consistently indented.\nUse logical operators (and, or, not) for more complex conditions.\nThis structure is essential for clean, readable decision-making logic in Python programs.\n\n\tif — Checks the first condition (score >= 90).\n\n\telif — Checks the next conditions in sequence (score >= 80, score >= 70, etc.).\n\n\telse — Runs if none of the above conditions are true.\n\nPress Enter to Exit...")
                        separator()
                        input()
                        continue

                    elif cream == "B":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("You have chosen for loops\n\nThe for loop in Python is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) and execute a block of code for each element in the sequence.\n\n\tFor Example:\n\n\t\tfruits = ['apple', 'banana', 'cherry']\n\t\tfor x in fruits:\n\t\t\tprint(x)\n\nIn this example, the loop iterates over each element in the fruits list and prints it.\n\nPress Enter to Exit...")
                        separator()
                        input()
                        continue

                    elif cream == "C":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("You have chosen while loops\n\nA while loop in Python repeatedly executes a block of code as long as a specified condition is true.\n\n\tFor Example:\n\n\t\ti = 1\n\t\twhile i < 6:\n\t\t\tprint(i)\n\t\t\ti += 1\n\nIn this example, the loop will print numbers from 1 to 5. The loop continues as long as i is less than 6.\n\nPress Enter to Exit...")
                        separator()
                        input()
                        continue

                    elif cream == "D":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("You have chosen break and continue statements\n\nbreak and continue are loop control statements that alter the normal flow of for and while loops.\nThey are typically used inside conditional statements to either exit a loop early or skip specific iterations.\n\nHow does it work?\n\n\tbreak:\n\t\tImmediately exits the loop when a condition is met.\n\t\tIn the example, the loop stops entirely when i == 5.\n\n\tcontinue:\n\t\tSkips the current iteration and moves to the next one.\n\t\tIn the example, even numbers are skipped, so only odd numbers are printed.\n\nPress Enter to Exit...")
                        separator()
                        input()
                        continue

                    elif cream == "E":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("You have chosen try and except blocks\n\nThe try and except blocks are used for exception handling — they let you run code that might cause an error without crashing the program.\n\n\tFor Example:\n\t\ttry:\n\t\t\tnum = int(input('Enter a number: '))\n\t\t\tprint(f'You entered: {num}')\n\t\texcept ValueError:\n\t\t\tprint('Invalid input! Please enter a valid integer.')\n\nPress Enter to Exit...")
                        separator()
                        input()
                        continue

                    elif cream == "F":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("Are you sure you want to Exit Control Structures Realm?")
                        separator()
                        in_cream = input("Your Choice? (Y/N) --> ").upper()

                        if in_cream == "Y":
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("Thank you for exploring the Control Structures Realm, Adventurer!\nExiting Menu...")
                            separator()
                            pause()
                            break

                        if in_cream == "N":
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("Returning to Control Structures Realm\n\nPress Enter to proceed...")
                            separator()
                            input()
                            continue

                        else:
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("There is no such option, Adventurer!\nPress Enter to go back...")
                            separator()
                            input()
                            pause()
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("Please wait...")
                            separator()
                            pause()
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("Returning...")
                            separator()
                            pause()
                            continue

                    else:
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("There is no such option, Adventurer!\nPress Enter to go back...")
                        separator()
                        input()
                        pause()
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("Please wait...")
                        separator()
                        pause()
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("Returning to Control Structures Realm")
                        separator()
                        pause()
                        continue

            elif gui == "D":
                while True:
                    clear()
                    title("Records & Documentation(Python Background)")
                    separator()
                    type_writer("You have chosen Variables and Operators Realm\n\nBelow are few things you can know about Variables and Operators\n\t1 - What's a Variable?\n\t2 - Assigning Values\n\t3 - Basic Arithmetic Operators\n\t4 - Exit")
                    separator()
                    cream = input("Your Choice --> ")

                    if cream == "1":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("Great Choice Adventurer!\n\nLet's discuss what is a Variable\n\nA Variable is simply a name that refers to a value stored in memory.\nYou don’t need to declare its type explicitly\nPython determines the type automatically when you assign a value.\n\nKeyPoints:\n\n\tDynamic typing: The type of a variable is determined at runtime.\n\n\tNo explicit declaration: You create a variable by assigning a value with =.\n\n\tCase-sensitive: age and Age are different variables.\n\n\tCan change type: A variable can hold different types of values at different times.\n\nPress Enter to Exit...")
                        separator()
                        input()
                        continue

                    elif cream == "2":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("Great Choice Adventurer!\n\nLet's discuss Assigning Values\n\nSo what is Assigning Values?\n\n\tAssigning values means storing data in a variable so you can use it later in your program.\n\tWhen you assign a value, you use the assignment operator = to link a variable name to a value in memory.\n\n\t\tBasic Syntax:\n\t\t\tvariable_name = value\n\n\t\t\tvariable_name → the name you choose to store the data.\n\t\t\t= → assignment operator (not 'equals' in math, but 'store this value in')\n\t\t\tvalue → the data you want to store (number, string, list, etc.).\n\n\t\tMultiple Assignments:\n\t\t\tPython allows assigning values to multiple variables in one line:\n\n\t\t\t\ta, b, c = 1, 2, 3\n\nPress Enter to Exit...")
                        separator()
                        input()
                        continue

                    elif cream == "3":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("Great Choice Adventurer!\n\nLet's discuss Basic Arithmetic Operators\n\nBasic arithmetic operators are symbols used in programming and math to perform simple calculations like adding, subtracting, multiplying, and dividing numbers.\n\n\t(+) Addition – adds numbers\n\t(-) Subtraction – subtracts numbers\n\t(*) Multiplication – multiplies numbers\n\t(/) Division – divides and returns a decimal\n\t(%) Modulus – returns the remainder\n\t(//) Floor Division – divides and returns the whole number only\n\t(**) Exponentiation – raises a number to a power\n\nPress Enter to Exit...")
                        separator()
                        input()
                        continue

                    elif cream == "4":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("Are you sure you want to Exit Variables and Operatos Realm?")
                        separator()
                        in_cream = input("Your Choice? (Y/N) --> ").upper()

                        if in_cream == "Y":
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("Thank you for exploring the Variables and Operators Realm, Adventurer!\nExiting Menu...")
                            separator()
                            pause()
                            break

                        if in_cream == "N":
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("Returning to Variables and Operators Realm\n\nPress Enter to proceed...")
                            separator()
                            input()
                            continue

                        else:
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("There is no such option, Adventurer!\nPress Enter to go back...")
                            separator()
                            input()
                            pause()
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("Please wait...")
                            separator()
                            pause()
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("Returning to Variables and Operators Realm.")
                            separator()
                            pause()
                            continue

                    else:
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("There is no such option, Adventurer!\nPress Enter to go back...")
                        separator()
                        input()
                        pause()
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("Please wait...")
                        separator()
                        pause()
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("Returning to Variables and Operators Realm")
                        separator()
                        pause()
                        continue

            elif gui == "E":
                while True:
                    clear()
                    title("Records & Documentation(Python Background)")
                    separator()
                    type_writer("You have chosen Function Realm\n\nWhat would you like to know about Functions?\n\t1 - Define Function\n\t2 - Calling a Function\n\t3 - Function with Parameters\n\t4 - Function with Return Value\n\t5 - Exit")
                    separator()
                    cream = input("Your Choice --> ")

                    if cream == "1":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("Alright Adventurer...\nLet's Define Function\n\n\tA function is a reusable block of code that does a specific task.\n\tUsing def tells Python that you are creating a function.\n\tThe code inside the function will only run when the function is called.\n\n\t\tFor Example:\n\t\t\tdef say_hello():\n\t\t\t\tprint('Hello! Welcome to Python.')\n\nPress Enter to Exit...")
                        separator()
                        input()
                        continue

                    elif cream == "2":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("Alright Adventurer...\nWhat's calling a Function?\n\n\tCalling a function means telling Python to run the code inside the function.\n\tYou do this by writing the function name followed by parentheses.\n\n\t\tFor Example:\n\t\t\tsay_hello()\n\nPress Enter to Exit...")
                        separator()
                        input()
                        continue

                    elif cream == "3":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("Alright Adventurer...\nLet's Discuss Funstion with Parameters\n\n\tParameters allow you to pass values into a function so it can work with different data.\n\tThis makes your function more flexible and useful.\n\n\t\tFor Example:\n\t\t\tdef greet_person(name):\n\t\t\t\tprint('Hello,', name)\n\n\t\t\tgreet_person('Maria')\n\t\t\tgreet_person('John')\n\nPress Enter to Exit...")
                        separator()
                        input()
                        continue

                    elif cream == "4":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("Alright Adventurer...\nLet's Discuss Function with Return Value\n\n\tA return value is the result that a function sends back to the program.\n\tThe return keyword ends the function and gives back a value that can be stored or used later.\n\n\t\tFor Example:\n\t\t\tdef add_numbers(a, b):\n\t\t\t\treturn a + b\n\n\t\t\ttotal = add_numbers(4, 6)\n\t\t\tprint('The total is:', total)\n\nPress Enter to Exit...")
                        separator()
                        input()
                        continue

                    elif cream == "5":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("Are you sure you want to Exit Functions Realm?")
                        separator()
                        in_cream = input("Your Choice? (Y/N) --> ").upper()

                        if in_cream == "Y":
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("Thank you for exploring the Functions Realm, Adventurer!\nExiting Menu...")
                            separator()
                            pause()
                            break

                        if in_cream == "N":
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("Returning to Functions Realm\n\nPress Enter to proceed...")
                            separator()
                            input()
                            continue

                        else:
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("There is no such option, Adventurer!\nPress Enter to go back...")
                            separator()
                            input()
                            pause()
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("Please wait...")
                            separator()
                            pause()
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("Returning to Functions Realm.")
                            separator()
                            pause()
                            continue

                    else:
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("There is no such option, Adventurer!\nPress Enter to go back...")
                        separator()
                        input()
                        pause()
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("Please wait...")
                        separator()
                        pause()
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("Returning to Functions Realm")
                        separator()
                        pause()
                        continue

            elif gui == "F":
                while True:
                    clear()
                    title("Records & Documentation(Python Background)")
                    separator()
                    type_writer("You have chosen Modules and Import Realm\n\nWhat would you like to know about Module and Import?\n\t1 - What ia a Module\n\t2 - Importing Module\n\t3 - Using Module Function\n\t4 - Exit")
                    separator()
                    cream = input("Your Choice --> ")

                    if cream == "1":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("That's a great choice Adventurer...\n\nSo What is a Module?\n\n\tA module is a file that contains ready-made code, such as functions and variables, that you can use in your program.\n\tPython has built-in modules that help you perform common tasks without writing everything from scratch.\n\nPress Enter to Exit...")
                        separator()
                        input()
                        continue

                    elif cream == "2":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("That's a great choice Adventurer...\n\nWhat is Importing Module\n\n\tTo use a module, you must first import it.\n\tImporting makes all the functions inside the module available for use in your program.\n\n\t\timport math\n\t\timport random\n\nPress Enter to Exit...")
                        separator()
                        input()
                        continue

                    elif cream == "3":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("That's a great choice Adventurer...\n\nHow to Use a Module?\n\n\tAfter importing a module, you can use its functions by writing the module name, a dot (.), and the function name.\n\n\t\tExample using random:\n\t\t\timport random\n\n\t\t\tnumber = random.randint(1, 10)\n\t\t\tprint(number)\n\n\t\tExample using math:\n\t\t\timport mathh\n\n\t\t\tresult = math.sqrt(9)\n\t\t\tprint(result)\n\nPress Enter to Enter...")
                        separator()
                        input()
                        continue

                    elif cream == "4":
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("Are you sure you want to Exit Module and Import Realm?")
                        separator()
                        in_cream = input("Your Choice? (Y/N) --> ").upper()

                        if in_cream == "Y":
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("Thank you for exploring the Module and Import Realm, Adventurer!\nExiting Menu...")
                            separator()
                            pause()
                            break

                        if in_cream == "N":
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("Returning to Module and Import Realm\n\nPress Enter to proceed...")
                            separator()
                            input()
                            continue

                        else:
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("There is no such option, Adventurer!\nPress Enter to go back...")
                            separator()
                            input()
                            pause()
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("Please wait...")
                            separator()
                            pause()
                            clear()
                            title("Records & Documentation(Python Background)")
                            separator()
                            type_writer("Returning to Module and Import Realm.")
                            separator()
                            pause()
                            continue

                    else:
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("There is no such option, Adventurer!\nPress Enter to go back...")
                        separator()
                        input()
                        pause()
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("Please wait...")
                        separator()
                        pause()
                        clear()
                        title("Records & Documentation(Python Background)")
                        separator()
                        type_writer("Returning to Module and Import Realm")
                        separator()
                        pause()
                        continue

            elif gui == "G":
                clear()
                title("Records & Documentation(Python Background)")
                separator()
                type_writer("You chose to Exit the Guide Menu\nAre you sure, you want to exit?...")
                separator()
                gui_choice = input("What will be your choice?(Y/N) --> ").upper()

                if gui_choice == "Y":
                    clear()
                    title("Records & Documentation(Python Background)")
                    separator()
                    type_writer("Thank you for exploring the PyWorldProject, Adventurer!\nExiting Menu...")
                    separator()
                    pause()
                    break

                elif gui_choice == "N":
                    clear()
                    title("Records & Documentation(Python Background)")
                    separator()
                    type_writer("You have chosen to stay, your determination to learn is on another level Adventurer\n\nPress Enter to return")
                    separator()
                    input()
                    pause()
                    continue

                else:
                    clear()
                    title("Records & Documentation(Python Background)")
                    separator()
                    type_writer("There is no such option, Adventurer!\nPress Enter to go back...")
                    separator()
                    input()
                    pause()
                    clear()
                    title("Records & Documentation(Python Background)")
                    separator()
                    type_writer("Please wait...")
                    separator()
                    pause()
                    clear()
                    title("Records & Documentation(Python Background)")
                    separator()
                    type_writer("Returning to PyWorldProject Guide Menu...")
                    separator()
                    pause()
                    continue                

            else:
                clear()
                title("Records & Documentation(Python Background)")
                separator()
                type_writer("There is no such option, Adventurer!\nPress Enter to go back...")
                separator()
                input()
                pause()
                clear()
                title("Records & Documentation(Python Background)")
                separator()
                type_writer("Please wait...")
                separator()
                pause()
                clear()
                title("Records & Documentation(Python Background)")
                separator()
                type_writer("Returning to Guide Menu...")
                separator()
                pause()
                continue

    # Exit Menu
    elif buff == "D":
        clear()
        title("Main Menu")
        separator()
        type_writer(f"Are you sure you want to Exit the PyWorldProject, Adventurer {name}? (Y/N)")
        separator()
        exit_cho = input("Your Choice will determine your fate Adventurer --> ").upper()

        if exit_cho == "Y":
            clear()
            title("Main Menu")
            separator()
            type_writer("You have chosen to Exit Menu\nThank you for visiting PyWorldProject Adventurer!--Until Next Time!")
            separator()
            pause()
            clear()
            title("Main Menu")
            separator()
            type_writer("Departing...")
            separator()
            pause()
            pause()
            clear()
            break

        elif exit_cho == "N":
            clear()
            title("Main Menu")
            separator()
            type_writer("You have chosen to Stay in the PyWorldProject, Adventurer!\nReturning to PyWorldProject...\nMay the Code be with You Adventurer!")
            separator()
            pause()
            continue

        else:
            clear()
            title("Main Menu")
            separator()
            type_writer("There is no such option, Adventurer!\nPress Enter to go back...")
            separator()
            input()
            pause()
            clear()
            title("Main Menu")
            separator()
            type_writer("Please wait...")
            separator()
            pause()
            clear()
            title("Main Menu")
            separator()
            type_writer("Returning to PyWorldProject Menu...")
            separator()
            pause()
            continue

    # None of the Choices
    else:
        clear()
        title("Main Menu")
        separator()
        type_writer("There is no such option, Adventurer!\n\nPress Enter to go back...")
        separator()
        input()
        pause()
        clear()
        title("Main Menu")
        separator()
        type_writer("Please wait...")
        separator()
        pause()
        clear()
        title("Main Menu")
        separator()
        type_writer("Returning to PyWorldProject...")
        separator()
        pause()
        continue