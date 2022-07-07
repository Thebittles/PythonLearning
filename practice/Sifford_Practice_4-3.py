# Brittany Sifford
# Practice - 4-3
# Status - Complete
#Takes number input x from user and takes char input then prints desired char x amount of times for x amount of rows


num = int(input("Enter a number from 1-15: "))
#Input Validation
while num <= 0 or num > 15:
    print("You did not enter a number between 1 and 15")
    num = int(input("Enter a postive number from 1-15: "))
char = input("Please input a character to create the square: ")
for number in range(1, num + 1, 1):
    for number in range(1, num + 1, 1):
        #Prints the char entered with no spaces in second loop
        print(char, end="")
    #Creates the new line in first loop
    print()

