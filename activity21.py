marble = True

while marble == True:
    grace = input("(Yes or No): ")

    if grace.lower() == "yes":
        print("COntinue")
        continue
    elif grace.lower() == "no":
        print("Stop")
        break
    else:
        print("Error input")
        continue