# Brittany Sifford
# Practice - 4-2
# Status - Complete
# Description - Grabs the user input numbers one low, and one high. Then iterates through low to high,  prints each number * 10 and also accumulates iterator total sum. 

#Grabs 
num1 = int(input("Enter a low number: "))
num2 = int(input("Enter a high number: "))

#amount to increment 
increment_amount = 1
#Number to multiply by
multiplier_amount = 10

#Initialize a variable for accumulator
total = 0;
 #Checks to make sure num1 is lower than num2
while num1 > num2 or num1 == num2:
  print('You did not enter the numbers correctly, please try again')
  num1 = int(input("Enter a low number: "))
  num2 = int(input("Enter a high number: "))
#When inputs are good run for loops
print('Number\tNumber * 10')
print('--------------')
for number in range(num1, num2 + 1, increment_amount):
 print(number, '\t', number * multiplier_amount)
for number in range(num1, num2 + 1, increment_amount):
 total += number
#prints accumalted total after for loop finishes
print("Accumulated total is: ", total)

