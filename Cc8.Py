#multiplication table for 6
#create a program that prints the of a number entered by the user, using a simple loop
#ask the user to input a number
#use a for loop to print the multiplication table for that number.
#format each line clearly

print("The Multiplication Table")
no = eval(input("Enter your Number: \n"))

for i in range(1, 11):
  num = no * i
  print(no, 'x' ,i, '=' , num)