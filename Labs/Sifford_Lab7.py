# Name - Brittany Sifford
# Status - Complete
# Description - This program has two functions the first ask you to input 10 numbers createas a list from those 10 numbers, then ask you to choose a greater than number to compare against the list
# The second function takes the list and number and returns a list containing only the values that are greater than the number inputted by the user.


def main():
    list = [0] * 10
    print("Enter a list of 10 integers")

    for i in range(len(list)):
        list[i] = int(input("Enter a number: "))

    number = int(input(
        "Enter the number you wish to test if the list elements are greater than: "))
    
    print("Number:", number)
    
    print("List of numbers:")
    
    print(list)

    greater_than, number = displayLarger(list, number)
    
    print("List of numbers that are larger than ", number, ":", sep="")
    print(greater_than)


def displayLarger(list, number):

    greater_than = []

    for i in range(len(list)):
        if list[i] > number:
            greater_than.append(list[i])

    return greater_than, number

main()
