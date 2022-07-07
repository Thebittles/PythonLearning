# Name - Brittany Sifford
# Status - Complete
# Description - This program asks the user to input First, Middle, Last name. Prints the full name and then counts the number of A, E, S not case sensitive and displays the counts.


def get_name():
    
    first = input("Enter your first name: ")
    middle = input("Enter your middle name: ")
    last = input("Enter your lastname: ")
    
    full_name = first + " " + middle + " " + last
    
    print("Full name: ", full_name)
    
    A_count = 0
    E_count = 0
    S_count = 0
    
    for ch in full_name:
        if ch == 'a' or ch == 'A':
            A_count += 1
        elif ch == 'e' or ch == 'E':
            E_count += 1
        elif ch == "s" or ch == "S":
            S_count += 1
    
    print("Counts of a & A", A_count)
    print("Counts of e & E", E_count)
    print("Counts of s & S", S_count)


get_name()