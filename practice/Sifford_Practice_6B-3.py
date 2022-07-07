



def main():
    # Open the the file for reading
    students_file = open(r'/Users/brittany/Desktop/Classes/Spring22/Progamming1/practice/students.txt', 'r')

    print("Name", '\t', "Score")
    print("--------------------------------")
    # Loop through  file and read each line
    for line in students_file:
        # Convert string line into number
        number = line.rstrip()
        # Print the number
        print(number)

    # Close file after loop is done
    students_file.close()

main()