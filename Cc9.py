#countdown timer
#ask user for the number to start countdown
#use for loop to count from that number to 1
#print each number on a new line
#print liftout after the loop ends

print("CountDown Timer")
time = eval(input("Count Down Started: \n"))

for i in range(time, 0, -1):
    print(i)
    
print("LiftOff!")