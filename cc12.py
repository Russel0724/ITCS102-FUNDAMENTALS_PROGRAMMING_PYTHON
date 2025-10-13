for g in range(1,10,1):
    for r in range(9,g,-1):
        print(" ", end =' ')
    for m in range(g,0,-1):
        print(m, end =' ')
    for t in range(2,g + 1,1):
        print(t, end =' ')
    print()