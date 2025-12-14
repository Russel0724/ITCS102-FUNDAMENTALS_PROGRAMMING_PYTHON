def code1():
    name = input("State Your Name: ")
    print("\t\t\t\t\t\t\t*\n\t\t\t\t\t\t*\t\t*\n\t\t\t\t\t*\t\t\t\t*\n\t\t\t\t*\t\t\t HI \t\t\t*\n\t\t\t*\t\t\t\t", name, "\t\t\t*\n\t\t\t\t*\t\t\t\t\t\t*\n\t\t\t\t\t*\t\t\t\t*\n\t\t\t\t\t\t*\t\t*\n\t\t\t\t\t\t\t*")

def code2():
    deno = [1000, 500, 200, 100, 50, 20, 10, 5, 1]

    amount = eval(input("Enter Amount to Deposit: "))

    print("Here is a Breakdown using PH denomination")

    print(amount // 1000, "-", 1000)
    amount = amount % 1000
    print(amount // 500, "-", 500)
    amount = amount % 500
    print(amount // 200, "-", 200)
    amount = amount % 200
    print(amount // 100, "-", 100)
    amount = amount % 100
    print(amount // 50, "-", 50)
    amount = amount % 50
    print(amount // 20, "-", 20)
    amount = amount % 20
    print(amount // 10, "-", 10)
    amount = amount % 10
    print(amount // 5, "-", 5)
    amount = amount % 5
    print(amount // 1, "-", 1)
    amount = amount % 1

def code3():
    email = "akolangto"
    pwd = "mamamo"

    x = input("Email --> ")
    y = input("Password --> ")
    if x.lower() == email and y.lower() == pwd:
        print("Access Granted!")
    else:
        print("Access Denied!")

def code4():
    pp = int(input("Enter Your Number --> "))
    if pp % 2 == 0:
        print("The number", pp, "is an even number!")
    else:
        print("The number", pp, "is an odd number!")

def code5():
    #mangaI recommendation
    # --- Layer 1: get user prefered manga
    print("Welcome to the Mangaka World Recommendation Center!")
    print("Select your Manga Genre:")
    print("1. RomCom")
    print("2. Adventure")
    print("3. Isekai")
    book_type = input("Enter Choice (1/2/3): --> ")

    # --- RomCom ---
    if book_type == "1":
        print("You Selected: RomCom Genre")

        chapters = input("Enter your chapter range (short/long): ")
        year = input("Enter the year of publication (2000/2010/2020): ")

        if chapters == "short" and year == "2000":
            print("We Recommend the following below:" , "\nQuoran High School Host Club \nToradora! \nLovely Complex \nChobits")
        elif chapters == "long" and year == "2000":
            print("We Recommend the following below:" , "\nHoney and Clover \nLovely Complex \nKimi ni Todoke")
        elif chapters == "short" and year == "2010":
            print("We Recommend the following below:" , "\nGe: Good Ending")
        elif chapters == "long" and year == "2010":
            print("We Recommend the following below:" , "\nMaid Sama! \nNisekoi \nKimi ni Todoke \nToradora")
        elif chapters == "short" and year == "2020":
            print("We Recommend the following below:" , "\nThe Summer You Were There \nLove Me, Love Me Not \nOoh La La \nBlue Box")
        elif chapters == "long" and year == "2020":
            print("We Recommend the following below:" , "\nHorimiya \nThe Dangers in My Heart \nKaguya-sama: Love is War \nMy Dress Up Darling \nThe Quintessential Quintuplets")

    # --- Adventure ---
    if book_type == "2":
        print("You Selected: Adventure Genre")

        chapters = input("Enter your chapter range (short/long): ")
        year = input("Enter the year of publication (2000/2010/2020): ")

        if chapters == "short" and year == "2000":
            print("We Recommned the following below:" , "\nSand Land")
        elif chapters == "long" and year == "2000":
            print("We Recommend the following below:" , "\nInuYasha \nBattle Royale \nGuin Saga \nKamunagara")
        elif chapters == "short" and year == "2010":
            print("We Recommend the following below:" , "\nAkame ga Kill \nMade in Abyss \nBlack Torch \nAstra Lost in Space(Kanata no Astra)")
        elif chapters == "long" and year == "2010":
            print("We Recommend the following below:" , "\nMagi: The Labyrinth of Magic \nBlue Exorcist(Ao no Exorcist) \nAkame ga Kill \nThe Seven Deadly Sins(Nanatsu no Taizai) \n Attack on Titan(Shingeki no Kyojin) \nGolden Kamuy \nDr. Stone")
        elif chapters == "short" and year == "2020":
            print("We Recommend the following below:" , "\nShaman King: Marcos \nMoriking")
        elif chapters == "long" and year == "2020":
            print("We recommend the following below:" , "\nFrieren: Beyond Journey's End \nThe Blue Wolves of Mibu")

    # --- Isekai ---
    if book_type == "3":
        print("You Selected: Isekai Genre")

        chapters = input("Enter your chapter range (short/long): ")
        year = input("Enter the year of publication (2000/2010/2020): ")

        if chapters == "short" and year == "2000":
            print("We Recommend the following below:" , "\nThe Twelve Kingdoms (Juuni Kokuki) \nSpiral Alive: Ima, Futatabi no Monogatari \nSuperior")
        elif chapters == "long" and year == "2000":
            print("We Recommend the following below:" , "\nFushigi Yuugi: Genbu Kaiden \nTsubasa: Reservoir Chronical")
        elif chapters == "short" and year == "2010":
            print("We Recommend the following below:" , "\nAstra Lost in Space \nBlack Torch \nStein;Gate")
        elif chapters == "long" and year == "2010":
            print("We Recommend the following below:" , "\nThe Devil is a Part-Timer! \nRe:Zero -Starting Life in Another World- \nKonosuba: God's Blessing on This Wonderful World! \nThat Time I Got Reincarnated as a Slime \nJobless Reincanation(Mushoku Tensei \nIn Another World With My Smartphone \nThe Rising of the Shield Hero \n Arifureta: From Commonplace to World's Strongest")
        elif chapters == "short" and year == "2020":
            print("We Recommend the following below:" , "\nThe White Mage Doesn't Want to Raise the Hero's Level \nThank You, Isekai \nSurvival in Another World with My Mistress!")
        elif chapters == "long" and year == "2020":
            print("We Recommend the following below:" , "\nIsekai Kanja no Tensei Musou (The Sage Becomes OP in Another World)")

        else:
            print("No Recommendation at a moment")

def core1():
    no = eval(input("Enter your number --> "))
    ber = 1

    for i in range (no, 0, -1):
        ber *= i
    print("The factorial of", no, "is", ber)

def core2():
    bruh = 0
    for i in range(-1, 11, 1):
        yeah = eval(input("Enter your Numbirs --> "))
        if yeah % 2:
            bruh += yeah
    print("Sum of odd numbers is", bruh)

def core3():
    print("The Multiplication Table")
    no = eval(input("Enter your Number: \n"))

    for i in range(1, 11):
        num = no * i
        print(no, 'x' ,i, '=' , num)

def core4():
    print("CountDown Timer")
    time = eval(input("Count Down Started: \n"))

    for i in range(time, 0, -1):
        print(i)
    
    print("LiftOff!")

def core5():
    print("\t\t *" ,end=" ")
    for g in range(1,11,1):
        for r in range(10,g,-1):
            print(" ", end=' ')
        for m in range(1,g,1):
            print("*", end=' ')
        for t in range(1,g,1):
            print("*", end=' ')
        print()

def care1():
    print("\t\t *", end=" ")
    for g in range(1,11,1):
        for r in range(10,g,-1):
            print(" ", end=" ")
        for m in range(1,g,1):
            print("*", end=" ")
        for t in range(1,g,1):
            print("*", end=" ")
        print()
    for g in range(1,11,1):
        for r in range(1,g,1):
            print(" ", end=" ")
        for m in range(10,g,-1):
            print("*", end=" ")
        for t in range(10,g,-1):
            print("*", end=" ")
        print()

def care2():
    for g in range(1,10,1):
        for r in range(9,g,-1):
            print(" ", end =' ')
        for m in range(g,0,-1):
            print(m, end =' ')
        for t in range(2,g + 1,1):
            print(t, end =' ')
        print()

def care3():
    #Christmas Tree
    for a in range(2,6,1):
        for b in range(0,7):
            print(" ",end=" ")
        for c in range(6,a,-1):
            print(" ",end=" ")
        for d in range(3,a):
            print("*",end=" ")
        for e in range(2,a,1):
            print("*",end=" ")
        print()    
    for f in range(1,3,1):
        for g in range(0,7):
            print(" ",end=" ")
        for h in range(0 - 1,f,1):
            print(" ",end=" ")
        for i in range(2,f,-1):
            print("*",end=" ")
        for j in range(3,f,-1):
            print("*",end=" ")
        print()    
    for k in range(2,9,1):
        for l in range(12,k,-1):
            print(" ",end=" ")
        for m in range(2,k,1):
            print("*",end=" ")
        for n in range(1,k):
            print("*",end=" ")
        print()
    for o in range(2,10,1):
        for p in range(12,o,-1):
            print(" ",end=" ")
        for q in range(1,o):
            print("*",end=" ")
        for r in range(2,o):
            print("*",end=" ")
        print()
    for s in range(2,13,1):
        for t in range(12,s,-1):
            print(" ",end=" ")
        for u in range(1,s):
            print("*",end=" ")
        for v in range(2,s):
            print("*",end=" ")
        print()
    for w in range(1,7):
        for x in range(1,9):
            print(" ",end=" ")
        for y in range(1,9):
            print("",end="*")
        print()

def care4():
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
            print(f"You took {tries} tries")
            break
        else:
            print("Wrong Guess")
            print("Again")
            continue

def care5():
    print("AniList")

    anime = []
    an = True

    while an == True:
        li = input("Enter Your Anime for the List(type 'exit' to exit): ")
        print("The Anime Added to your List.")
        anime.append(li)
        if li == "exit":
            print("Your listing is finish, exiting!")
            anime.pop()
            break

    print(f"Here is the Summation List of your Anime: ")
    for me in anime:
        print(f"- {me}")