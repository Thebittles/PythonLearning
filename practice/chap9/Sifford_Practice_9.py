
# Person 1 - Look up and display functions
# Britt
# Brooks
# Corbin
# Elias
"""
Group project – break into groups of 3 or 4

Using the example of the birthday dictionary in Chapter 9, create a dictionary application, subject of your choosing (appropriate content)

In addition to the menu choices provided to the user in the example, add menu items to display the entire dictionary.

Each person will create a separate module for their function(s) with the main program importing all the modules.

Person 1 – main program/menu display, coordinates other programs

Person 2 – Look up and display functions

Person 3 – Add function

Person 4  - Change, and Delete functions

When you are done – demonstrate your menu

Save your programs for next class – make sure everyone has a copy  in case someone is absent

 """

# Import the students program
from Elias_add_function import add
from Brooks_look_up_and_display import display, look_up
from Corbiin_change_delete import change, delete
from Corbin_pickle import save
from Elias_retrieve import retrieve

def main():
    # First create a empty dictionary to store birthdays in
    birthdays = {}
    # Initialize variable for menuselection
    selection = 0
    while selection != 7:
        selection = menu_display()
        # Determines which program to run based on user selection
        if selection == 0:
            display(birthdays)
        elif selection == 1:
            look_up(birthdays)
        elif selection == 2:
            add(birthdays)
        elif selection == 3:
            change(birthdays)
        elif selection == 4:
            delete(birthdays)
        elif selection == 5:
            save(birthdays)
        elif selection == 6: 
            retrieve()
        


# Function for menu choices
def menu_display():
    print()
    print("Student birthdays menu")
    print('0: Display Birthdays')
    print('1: Look up a birthday')
    print('2: Add a birthday')
    print('3: Change/Update an existing birthday')
    print('4: Delete a birthday')
    print('5: Save birthdays to file')
    print('6: Retrieve birthday from file')
    print('7: Quit program')
    print()

    # Grap user input for program menu choice
    selection = int(input("Please enter the menu choice number: "))

    # Need to error handle user input
    while selection < 0 or selection > 7:
        selection = int(input("Please enter a valid choice 0-5: "))

    # Return selection back to main function
    return selection

 

# Call the main function
main()
