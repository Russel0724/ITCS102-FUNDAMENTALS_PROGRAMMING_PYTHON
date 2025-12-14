

print("Adding anime to Dictionary")

ani = {} #empty dictionary

add = True 

def search(aa):
    print("Searching....")
    print(f"Result shows {ani[aa]}")

def printer():
    for a,b in ani.items():
        print(f"Keys {a} Title {b}")

while add == True:
    sho = input("Short term to call the anime: ")
    title = input("Title of the anime: ")

    ani[sho] = title

    pick = input("Would you like to continue\nA - Yes\nB - No\nC - Print\nD - Search\n\nYour Answer ").upper()

    if pick == "A": 
        print("Continuing...")
        continue

    elif pick == "B": #Stopper
        print("Stopping...")
        print("Program Stop")
        break
    
    elif pick == "C": #print
        print("=" * 20)
        print("Printing....")
        printer()
        print("=" * 20)
        continue
    
    elif pick == "D": #Search
        srch = input(f"Put the key: ")
        print("exiting....")
        search(srch)
        continue

    else:
        print("Invalid Choice")
        
