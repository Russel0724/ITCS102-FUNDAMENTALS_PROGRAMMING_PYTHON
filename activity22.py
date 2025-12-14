import random

digit = random.randint(1,10)

tries = 0
eve = True

while eve == True:
    i = int(input("What number u guess(1-10) --> "))
    tries += 1

    if i == digit:
        print("Congratulation")
        print(f"The number is {digit}")
        print(f"You online took {tries} tries")
        break

    else:
        print("youre wrong")
        continue
 