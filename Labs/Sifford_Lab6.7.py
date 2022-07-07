# Brittany Sifford
# Status - Complete
# Description - This program will write random numbers 1-500 How every many times you specified in the input ot the file random_numbers.txt

#Importing random module
import random

def main():
  #Description of program
  print("This program will write random numbers 1-500, however many times you would like.")
  try:
    # Grabs desired amount of times to write to file
    amount = int(input("Please enter the amount of times you want a random number to be printed: "))
    # Open File
    number_file = open(r'/Users/brittany/Desktop/Classes/Spring22/Progamming1/Labs/random_numbers.txt', 'w')
    for number in range(1, amount + 1):
      # Get random number every iteration of loop 
      ran_num = random.randint(1, 500)
      number_file.write(str(ran_num) + '\n')
    # Close the file
    number_file.close()
  # Error Handling - Something goes wrong opening/writing to file
  except IOError:
    print("Something went wrong trying to open/write the file")
  # Error Handling - Numeric value wants to read num instead of str
  except ValueError:
    print("Must be a numeric value entered into input")
  # Error Handling - Any unspecified error
  except:
    print("An program error occurred ")




#Call main function
main()