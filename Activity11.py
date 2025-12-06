temp = eval(input("What is the Temperature today? --> "))

if temp <= 0:
    print("The temperature is freezing cold")
elif temp >= 1 and temp <= 20:
    print("The temperature is cold")
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
