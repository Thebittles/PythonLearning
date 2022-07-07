#Brooks Pavelka - Completed
#The look_up and display functions for 9-1 practice

def look_up(birthdays):
    name = input('Enter a name: ')
    print(birthdays.get(name,'Sorry, this name was not found.'))

def display(birthdays):
    birthdays_list = birthdays.items()
    print('Here are all of the birthdays:')
    print('Name\tBirthday')
    print('----------------')
    for tup in birthdays_list:
        for item in tup:
            print(item,end='\t')
        print()
