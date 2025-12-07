import random

print("number guesser")

ranber = random.randint(1,100)
tries = 0
go = True

while go == True:
    no = eval(input("Enter your number: "))

    tries += 1

    if no == ranber:
        print("Number has been guessed!")
        print(f"You took {trie} tries")
        break
    else:
        print("Wrong Guess")
        print("Again")
        continue
