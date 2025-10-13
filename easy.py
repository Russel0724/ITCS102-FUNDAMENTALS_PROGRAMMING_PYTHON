for a in range(1, 6, 1):
    for b in range(5, a, -1):
        print(" ", end = " ")
    for c in range(a, 0, -1):
        print("*", end = " ")
    for d in range(1, a , 1):
        print("*", end = " ")
    print()

for i in range(1, 6, 1):
    for d in range(1, i + 1, 1):
        print(i, end = " ")
    print()