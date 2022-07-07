# Brittany Sifford
# Status - Complete
# Description - This program reads a file called random_numbers.txt adds all the numbers from the file, prints the total of the numbers, and the amount of numbers read



def main():
  try:
    # Accumlator - total of all nums sum
    total = 0
    # Counter - count of num 
    count = 0
    # Open the number file
    number_file = open(r'/Users/brittany/Desktop/Classes/Spring22/Progamming1/Labs/random_numbers.txt', 'r')
    # Loop through and read lines from file
    for line in number_file:
      num = int(line)
      total += num
      count += 1
    average = total/count
    print("The sum of all your numbers is", total)
    print("The number of random numbers read from the file", count)
    print("The average of all your numbers is", average)
    #Close the file
    number_file.close()
  #Error handling - IOError - user enters wrong file path/name
  except IOError:
    print("An error trying to read the file: ", number_file)
  #Error handling - ValueError - reads "fifty" instead of 50
  except ValueError:
    print("An error occured: Non numeric data found in file")
  #Error handling - any unspecified errors
  except:
    print("An error occured please try again")

 # Call main function
main()


