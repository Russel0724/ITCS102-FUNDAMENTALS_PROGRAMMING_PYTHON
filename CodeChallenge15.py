print("AniList")

anime = []
an = True

while an == True:
    li = input("Enter Your Anime for the List: ")
    print("The Anime Added to your List.")
    anime.append(li)
    if li == "exit":
        print("Your listing is finish, exiting!")
        anime.pop()
        break

print(f"Here is the Summation List of your Anime: ")
for me in anime:
    print(f"- {me}")
