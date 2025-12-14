def mine1():
    print("Hello World")

def mine2():
    name = input("Please State Your Name --> ")

    print("Confirmed User,", name, ",Welcome to the Matrix, Master.")
    #test change

def mine3():
    purple = input("Please State Your Name --> ")
    print("The overall letters in your name:", len(purple))

def mine4():
    purple = input("Put something --> ")
    print("The Data type of something is", type(purple))

def mine5():
    pur = input("Put something(1-100) --> ")
    print("The Data type of something is", type(pur))

    pur_num = int(pur)  # convert string to int
    answer = 6 + pur_num

    print("The answer is", answer)

def mine6():
    x = eval(input("Type Your Number(1-100): "))
    y = eval(input("Type Your Number(1-100): "))
    l = x + y
    u = x - y
    m = x * y
    i = x / y

    print("The sum of", x, "and", y,"is", l)
    print("The difference of", x, "and" ,y, "is", u)
    print("The product of", x, "and" ,y, "is", m)
    print("The quotient of", x, "and" ,y, "is", i)
    print(x, "exponent by", y, "is" ,x**y)
    print("The remainder of", x, "and" ,y, "is", x%y)
    print("The floor division of", x, "and" ,y, "is", x//y)

def mine7():
    lm = 5
    print("The Value of it is", lm)

    lm *= 5
    print("The Value of it is", lm)

    lm /= 5
    print("The Value of it is", lm)

def mine8():
    mydept = 1000
    mymoney = 500

    print((mydept) <= (mymoney))

    cash = 50
    payment = 80

    print((cash) <= (payment))

def mine9():
    put = "email"
    pit = 4321

    print((put == "email") and (pit == 4321))
    print((put == "email") or (pit == 5321))
    print(not((put == "email") or (pit == 5321)))

def yours1():
    name = input("Input your name --> ")
    isStudent = input("Are you a student (Yes/No) --> ")
    fare = eval(input("bayad --> "))

    if isStudent.lower() == "yes":
        discount = fare * .2
        new_fare = fare - discount
        print("Hi", name, "student discount is", discount, "Discounted fare is", new_fare)
    else:
        print("Sorry", name, "you are not eligible for student discount")

def yours2():
    temp = eval(input("What is the Temperature today? --> "))

    if temp <= 0:
        print("The temperature is freezing cold")
    elif temp >= 1 and temp <= 20:
        print("Temperature is cold")
    elif temp >= 21 and temp <= 30:
        print("The temperature is lookwarm")
    elif temp >= 31 and temp <= 40:
        print("The temperature is warm")
    elif temp >= 41 and temp <= 50:
        print("The temperature is hot")
    elif temp >= 51:
        print("The temperature is boiling hot")
    else:
        print("invalid temperature")

def yours3():
    for i in range(1,11):
        print(i, "Hello World")

def yours4():
    x = 0

    for i in range(1,11,1):
        val = eval(input("Enter your number --> "))
        x += val
        print(x, "New Value of", val)
    print("total:", x)

def yours5():
    for i in range(20,0,-1):
        print(i, "konnichiwa")

def yours6():
    off = 0

    for i in range(1,11):
        gm = eval(input("Enter a Number --> "))
        if gm % 2 == 1:
            off += gm
    print(f"The summation of all odd number is {off}")
   
def yours7():
    for i in range(1,11):
        print(i, end=" ")

def yours8():
    for i in range(1,11):
        for me in range(1,11):
            print(me, end=" ")
        print()

def yours9():
    for x in range(1,11,1):
        for y in range(1,11,1):
            print(y, end=" ")
        print()

    for i in range(1,11,1):
        for o in range(1,i,1):
            print(o, end=" ")
        print()

def them1():
    for i in range(1,11,1):
        for o in range(1,i,1):
            print("*", end=" ")
        print()

def them2():
    for i in range(1,11):
        for me in range(1,i,1):
            print("#",end=" ")
        for g in range(10,i,-1):
            print("*",end=" ")
        print()    

def them3():
    marble = True

    while marble == True:
        grace = input("(Yes or No): ")

        if grace.lower() == "yes":
            print("Continue")
            continue
        elif grace.lower() == "no":
            print("Stop")
            break
        else:
            print("Error input")
            continue

def them4():
    import random

    digit = random.randint(1,10)

    tries = 0
    eve = True

    while eve == True:
        i = int(input("What number u guess(1-10) --> "))
        tries += 1

        if i == digit:
            print("Congratulation")
            print(f"The number is {digit}")
            print(f"You online took {tries} tries")
            break

        else:
            print("youre wrong")
            continue
 
def them5():
    list = ['banana','oranges','raspberry','grapes','strawberry']

    list.append('blackberry')  #adds item
    print(list)
    list.pop() #deletes item from the list
    print(list)
    list.insert(0,'pineapple')  #adds item to the specific position
    print(list)
    for i in list:
        print(f"{i} in the list")

    peace = 'Glenn Russel Tiangco'
    for g in peace:
        print(g)
    print("\nReversed\n")
    for r in peace[::-1]:
        print(r)

def them6():
    def greeter(name):
        print(f"Hello {name}, how are you?")

    def summ(x):
        total = 0
        for i in range(x,0,-1):
            total += i
        print(f"The sum of {x} is {total}")
    greeter("Eren")
    greeter("Naruto")
    greeter("Yuji")
    greeter("Luffy")

    summ(20)
    summ(15)
    summ(10)
    summ(5)

def them7():
    def ac1():
        name = input("What is your name: ")
    def ac2():
        age = eval(input("What is your age: "))
    def ac3():
        address = input("Where do you live: ")
    def ac4():
        sex = input("Male/Female -> ")

    name  = input("Whats is your name: ")

    print(f"Welcome {name} to my File compiler")

    g = True

    while g == True:
        print("Select a Program")
        print("A - Activity1\nB - Activity2\nC - Activity3\nD - Activity 4\nE - Exit")

        basta = input("Input the letter of the activity you like to run --> ").lower()

        if basta == "a":
            ac1()
            continue
        elif basta == "b":
            ac2()
            continue
        elif basta == "c":
            ac3()
            continue
        elif basta == "d":
            ac4()
        elif basta == "e":
            print("Thank you for cooperation")
            break
        else:
            print("invalid input")
