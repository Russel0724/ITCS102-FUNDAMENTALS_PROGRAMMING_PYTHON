from activity1 import mine1
from activity2 import *
from activity3 import *
from activity4 import *
from activity5 import *
from activity6 import *
from activity7 import *
from activity8 import *
from activity9 import *
# from activity10 import *
# from activity11 import *
# from activity12 import *
# from activity13 import *
# from activity14 import *
# from activity15 import *
# from activity16 import *
# from activity17 import *
# from activity18 import *
# from activity19 import *
# from activity20 import *
# from activity21 import *
# from activity22 import *
# from activity23 import *
# from activity24 import *
# from activity24_1 import *
# from activity25 import *
# from activity25_1 import *
# from codechallenge1 import *
# from codechallenge2 import *
# from codechallenge3 import *
# from codechallenge4 import *
# from codechallenge5 import *
# from codechallenge6 import *
# from codechallenge7 import *
# from codechallenge8 import *
# from codechallenge9 import *
# from codechallenge10 import *
# from codechallenge11 import *
# from codechallenge12 import *
# from codechallenge13 import *
# from codechallenge14 import *
# from codechallenge15 import *


print("Welcome to MyWorld!")

name = input("State your name --> ")
print(f"Hello {name}")
a = True
while a == True:
    print("Choose what kind of your Project you wanted to see Below")
    print("A - Activity\nB - CodeChallenge\nC - Exit")
    b = input("Your Choice --> ").upper()
    if b == "A":
        print("Welcome to the world of my Activities, Adventurer!")
        print("A - Activities(1 - 9)\nB - Activities(10 - 18)\nC - Activities(19 - 27)\nD - Exit")
        act = input("Your Choice --> ").upper()
        while True:
            if act == "A":
                print("Your have chosen Activities 1 - 9")
                print("A = Activity1\nB - Activity2\nC - Activity3\nD - Activity4\nE - Activity5\nF - Activity6\nG - Activity7\nH - Activity8\nI - Activity9\nJ - Exit")
                choi = input("Your Choice --> ").upper()
                if choi == "A":
                    print(f"You Chose: {choi}")
                    print(f"You may now use {choi}")
                    mine1()
                    continue
                elif choi == "B":
                    print(f"You Chose: {choi}")
                    print(f"You may now use {choi}")
                    mine2()
                    continue
                elif choi == "C":
                    print(f"You Chose: {choi}")
                    print(f" You may now use {choi}")
                    mine3()
                    continue
                elif choi == "D":
                    print(f"You Chose: {choi}")
                    print(f"You may now use {choi}")
                    mine4()
                    continue
                elif choi == "E":
                    print(f"You Chose: {choi}")
                    print(f"You may now use {choi}")
                    mine5()
                    continue
                elif choi == "F":
                    print(f"You Chose: {choi}")
                    print(f"You may now use {choi}")
                    mine6()
                    continue
                elif choi == "G":
                    print(f"You Chose: {choi}")
                    print(f"You may now use {choi}")
                    mine7()
                    continue
                elif choi == "H":
                    print(f"You Chose: {choi}")
                    print(f"You may now use {choi}")
                    mine8()
                    continue
                elif choi == "I":
                    print(f"You Chose: {choi}")
                    print(f"You may now use {choi}")
                    mine9()
                    continue
                elif choi == "J":
                    print("Exiting to Main Menu")
                    break
                else:
                    print("Invalid Choice, Try Again")
                    continue