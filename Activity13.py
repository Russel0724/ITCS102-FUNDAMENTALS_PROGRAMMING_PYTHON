x = 0

for i in range(1, 11, 1):
    val = eval(input("Enter your number: --> "))
    x += val
    print(x, "New Value of", val)
print("total:", x)
