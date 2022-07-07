 # Brittany Sifford
 # Status - Complete
 # Description - This program will calculate the fall distance over time display both time and fall distance in meters
 
 #Import everything from this file 
from Sifford_Lab5B_distance import *
 

def main():
    print("This program will print the amount of time and fall distance in meters")
    print("Time", '\t', "Falling Distance")
    print('-------------------------------')
    for seconds in range(1, 11):
        print(seconds, '\t',format(falling_distance(seconds), '.2f'))



#Call the main function
main()