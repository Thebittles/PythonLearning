# Brittany Sifford
# Status - Complete
# Description -  This program reads all the lines from a file called number_list.text and displays them.



def main():
    # Open the the file for reading
    number_file = open(
        r'/Users/brittany/Desktop/Classes/Spring22/Progamming1/practice/number_list.txt', 'r')

    # Loop through  file and read each line
    for line in number_file:
        # Convert string line into number
        number = int(line)
        # Print the number
        print(number)

    # Close file after loop is done
    number_file.close()

main()
