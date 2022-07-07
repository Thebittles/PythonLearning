# Brittany Sifford
# Status - Complete
# Description: This program opens and reads file. Then prints each line written to file along with age being diveded by two. 


def main():
    #Open my_name.txt
    name_file = open(r'/Users/brittany/Desktop/Classes/Spring22/Progamming1/practice/my_name.txt', 'r')
    
    #Reading each line and stripping '\n'
    #I know this as chaining methods in JavaScript is it the same in python?
    line1 = name_file.readline().rstrip()
    line2 = name_file.readline().rstrip()
    line3 = name_file.readline().rstrip()
    
    #Print first name
    print(line1)
    #Print second name
    print(line2)
    #Print age as a number
    print(int(line3))
    #Print age / 2
    print(int(line3)/2)
    
    
    

    
main()
   
