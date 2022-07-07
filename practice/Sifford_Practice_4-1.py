# Brittany Sifford
# Practice - 4-1
# Status - Complete
# Ask for user to input a number between 1 & 7 prints correlating day of week, then ask if user would like to be asked again


#Setting variable to yes
keep_asking = 'yes'

#setting condition for while loop
while keep_asking == 'yes':
    #Grabs number entered from user
    num = int(input("Please enter a number 1-7:"))
    #Checks to see if number entered is between 1 & 7 
    while num < 1 or num > 7:
         print("Error: You did not enter a number between 1-7")
         num = int(input("Please enter a number 1-7:"))
    #Displays correct week string to num entered
    if num == 1:
        print("Monday")
    elif num == 2:
        print("Tuesday")
    elif num == 3:
        print("Wednesday")
    elif num == 4:
        print("Thursday")
    elif num == 5:
        print("Friday")
    elif num == 6:
        print("Saturday")
    else:
        print("Sunday")
    #Ask the user to input yes or no and assigns to variable keep_asking 
    keep_asking = input("Enter yes to keep going or no to quit: ")
    



# Program 2 - Complete
#Ask user to input two numbers, returns total of numbers inputted, ask if you would like to repeat 

#condition to run again
ask_again = 'yes'

while ask_again == 'yes':
    #Enter number 1
    num1 = int(input("Please enter a number: "))
    #Enter number 2
    num2 = int(input("Please enter another number: "))
    total = num1 + num2
    print("The sum of your numbers is:", total)
    #Set condition after running
    ask_again = input("Would you like me to ask again? yes or no: ")