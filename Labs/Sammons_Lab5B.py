# Andrew Sammons
# Lab 5B
# Complete, Tested

# Write a program that uses a given formula to calculate and display the distance an object falls over a given time
# no inputs
# output a chart with a given format

 #Import everything from this file 
from Sifford_Lab5B_distance import *

FALL_DURATION = 10

def main():  # no inputs, pass the duration given into the falling_distance function, print as a chart
    border = "-" * 41
    print("Time (seconds)  |", "Total Distance Fallen", sep="\t")
    print(border)
    for seconds in range(FALL_DURATION + 1):
        print(seconds, '\t',format(falling_distance(seconds), '.2f'))


main()
