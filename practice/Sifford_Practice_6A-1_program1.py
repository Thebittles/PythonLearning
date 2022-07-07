# Brittany Sifford
# Status - Complete
# Description: This program has two functions, the first opens a file and writes  two names and an age. The second functions opens and reads the file. Then prints each line written to file along with age being diveded by two. 


def main():
    # Open the file
    name_file = open(r'/Users/brittany/Desktop/Classes/Spring22/Progamming1/practice/my_name.txt', 'w')
    
    name1 = "Brittany"
    name2 = "Justin"
    age = 28
    # Write name1 to file
    name_file.write(name1 + '\n')
    # Write name2 to file
    name_file.write(name2 + '\n')
    # Write age to to file as string
    name_file.write(str(age))
    # Close file
    name_file.close()
    
main()
   
