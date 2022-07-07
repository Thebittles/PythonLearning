# Brittany Sifford
# Status - 
# Description - This program generates the side of a square, then calculates the square area and square perimeter based on side. Returns all three values.


 
#Import random module
import random


def main():
    # Get random int between 1-100
    # Side will be our value of one side of a square
    side = random.randint(1, 100)
    sq_area = square_area(side)
    sq_perimeter = square_perimeter(side)
    return side, sq_area, sq_perimeter
#Display the side, the returned area, and the returned perimeter.

# Function for square_area
def square_area(side):
    area = side**2
    return area

# Function for square_perimeter
def square_perimeter(side):
    perimeter = 4*side
    return perimeter
    

#Call main function   
#Destructuring values from main?
side, sq_area, sq_perimeter = main()

print("The side of the square is: ", side)
print("The square area of the square is: ", sq_area)
print("The square perimeter of the square is: ", sq_perimeter)