off = 0

for i in range(1,11):
    gm = eval(input("Enter a Number --> "))
    if gm % 2 == 1:
        off += gm
print(f"The summation of all odd number is {off}")
