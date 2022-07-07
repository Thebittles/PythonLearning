# Brittany Sifford
# Status - Complete 
# Description - This program generates a random radius value and then caluclates the area of a circle based on that radius value. 

#Import random module
import random

#Global constant PI
PI = 3.14159

def main():
  #Get random num and store in variable radius
  radius = get_random()
  print("Radius is..", radius)
  #Calculate area using radius
  area = PI * (radius**2)
  return print("Area is..", area)

# Get random floating point b/w 1-100
def get_random():
  return random.uniform(1.0, 100.00)

#Call the main function
main()