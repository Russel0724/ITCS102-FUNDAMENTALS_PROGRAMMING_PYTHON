#odd number summation
#enter 10 numbers
#codechallenge7

bruh = 0
for i in range(-1, 11, 1):
    yeah = eval(input("Enter your Numbirs --> "))
    if yeah % 2:
        bruh += yeah
print("Sum of odd numbers is", bruh)
