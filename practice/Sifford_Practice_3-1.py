#Brittany Sifford
#Practice assignment Ch. 3-1

#User enter month
month = int(input("Please enter the month as a number: "))

#User  enters day
day = int(input("Please enter the day as a number: "))

#User enters year
year = int(input("Please enter the last two digits of the year: "))


if (month * day) == year:
    print("The date is magic")
else:
    print("The date is NOT magic")