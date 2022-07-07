# Brittany Sifford
# Status - Complete
# Description  - This program reads a file inputed by user sums all the numbers written into that file and displays the sum and average. This program also handles any IOErrors, ValueErrors, and any other unspecified errors using try/except


# Path to number_list.txt - /Users/brittany/Desktop/Classes/Spring22/Progamming1/practice/number_list.txt

def main():
  try:
    fileName = input("Enter a filename: ")
    # Accumlator - total of all nums sum
    total = 0
    # Counter - count of num 
    count = 0
    # Open the number file
    number_file = open(fileName, 'r')
    # Loop through and read lines from file
    for line in number_file:
      num = int(line)
      total += num
      count += 1
    average = total/count
    print("The sum of all your numbers is", total)
    print("The average of all your numbers is", average)
    #Close the file
    number_file.close()
  #Error handling - IOError - user enters wrong file path/name
  except IOError:
    print("An error trying to read the file: ", fileName)
  #Error handling - ValueError - reads "fifty" instead of 50
  except ValueError:
    print("An error occured: Non numeric data found in file")
  #Error handling - any unspecified errors
  except:
    print("An error occured please try again")

 # Call main function
main()


