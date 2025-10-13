col = eval(input("Enter the No. of Column --> "))
for a in range(1,11,1):
    for b in range(1, col + 1, 1):
        print(f"{a}x{b}={a*b}", end = "\t\t")
    print()