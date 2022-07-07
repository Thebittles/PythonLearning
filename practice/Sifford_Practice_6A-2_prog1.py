# Brittany Sifford
# Status - Complete
# Description - This program opens/creates a file and prints the numbers 50-100 and then closes the file

"""
Program 1 - Write numbers to a file:
Open an output file with the filename number_list.txt
Use a loop to write the numbers 50 through 100 to the file, and then close the file.   Be sure to save your file to use in the next assignment
 """


def main():
    # Open Number file
    number_file = open(r'/Users/brittany/Desktop/Classes/Spring22/Progamming1/practice/number_list.txt', 'w')
    # Loop through 50-100
    for num in range(50, 100 + 1):
      # Convert to strign and write the numbers in loop iteration
        number_file.write(str(num) + '\n')

    number_file.close()


main()
