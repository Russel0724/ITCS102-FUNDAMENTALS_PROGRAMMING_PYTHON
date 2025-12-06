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
