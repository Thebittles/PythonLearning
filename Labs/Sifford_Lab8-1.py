# Name - Brittany Sifford
# Status - Complete
# This program opens a file and counts the number of uppercase, lowercase, digits, and spaces in the the text of the file and prints the counts.

def main():

    text_file = open(
        r'/Users/brittany/Desktop/Classes/Spring22/Progamming1/Labs/text.txt', 'r')

    upperCase = 0
    lowerCase = 0
    digits = 0
    spaces = 0

    for line in text_file:
        for ch in line:
            if ch.isupper():
                upperCase += 1
            if ch.islower():
                lowerCase += 1
            if ch.isdigit():
                digits += 1
            if ch.isspace():
                spaces += 1

    text_file.close()

    # Print Counts
    print("Uppercase Letters: ", upperCase)
    print("Lowercase Letters: ", lowerCase)
    print("Digits: ", digits)
    print("Spaces: ", spaces)

main()
