# Name: Brittany Sifford
# Status: Complete
# Description: This program ask the user to input a date formatted mm/dd/yyyy and prints the date as Month day, year



def date_printer():
    str_date = input("Enter a date in the format mm/dd/yyy: ")
    
    months = ['January', "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    list = str_date.split('/')
    
    month = int(list[0]) - 1
    
    print(months[month] + " " + list[1] + ", " + list[2])
    
    print()
    
date_printer()