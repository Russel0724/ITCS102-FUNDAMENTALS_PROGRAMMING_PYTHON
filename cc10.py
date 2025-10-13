for m in range(1,11,1):
    for g in range(10,m,-1):
        print(" ", end=' ')
    for t in range(1,m,1):
        print("*", end=' ')
    for r in range(1,m,1):
        print("*", end=' ')
    print()