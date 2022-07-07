#Elias Cerda

import pickle


def retrieve():

    end_of_file = False

    inputFile = open(
        r'/Users/brittany/Desktop/Classes/Spring22/Progamming1/practice/chap9/birthdays.dat', 'rb')

    while not end_of_file:
        try:
            birthday = pickle.load(inputFile)
            display_data(birthday)
        except EOFError:
            # End of file has been reached
            end_of_file = True

    inputFile.close()


def display_data(birthday):
    print()
    print("Birthdays")
    for key in birthday:
      print(key, birthday[key])
