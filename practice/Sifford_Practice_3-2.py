# Brittany Sifford
# Practice Chapter 3-2
# Program 1: if-else-if

day = int(input("Please enter a number between 1-7: "))

#Check inputs
while day < 1 or day > 7:
    print("Error: You did not enter a number between 1-7")
    day = int(input("Please enter a number between 1-7: "))
#Check num and print correlating day
if day == 1:
    print("Monday")
else:
    if day == 2:
        print("Tuesday")
    else:
        if day == 3:
            print("Wednesday")
        else:
            if day == 4:
                print("Thursday")
            else:
                if day == 5:
                    print("Friday")
                else:
                    if day == 6:
                        print("Saturday")
                    else:
                        print("Sunday")
        

# Program 2: if-elif-else
day = int(input("Please enter a number between 1-7: "))

#Check inputs to make sure its between 1-7
while day < 1 or day > 7:
    print("Error: You did not enter a number between 1-7")
    day = int(input("Please enter a number between 1-7: "))
#Check num and print correlating day
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
else:
    print("Sunday")
