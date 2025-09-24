print("\t\t *" ,end=" ")
for g in range(1,11,1):
    for r in range(10,g,-1):
        print(" ", end=' ')
    for m in range(1,g,1):
        print("*", end=' ')
    for t in range(1,g,1):
        print("*", end=' ')
    print()
