#factorial program
#descending numbers
#must be equal to 120
#the factorial number is 5

no = eval(input("Enter your number --> "))
ber = 1

for i in range (no, 0, -1):
    ber *= i
print("The factorial of", no, "is", ber)