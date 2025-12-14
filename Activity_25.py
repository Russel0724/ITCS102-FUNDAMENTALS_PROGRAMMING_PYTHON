from activity25_1 import *

name  = input("Whats is your name: ")

print(f"Welcome {name} to my File compiler")

g = True

while g == True:
    print("Select a Program")
    print("A - Activity1\nB - Activity2\nC - Activity3\nD - Activity 4\nE - Exit")

    basta = input("Input the letter of the activity you like to run --> ").lower()

    if basta == "a":
        ac1()
        continue
    elif basta == "b":
        ac2()
        continue
    elif basta == "c":
        ac3()
        continue
    elif basta == "d":
        ac4()
    elif basta == "e":
        print("Thank you for cooperation")
        break
    else:
        print("invalid input")
