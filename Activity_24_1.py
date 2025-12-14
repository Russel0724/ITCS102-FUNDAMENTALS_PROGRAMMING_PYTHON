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
