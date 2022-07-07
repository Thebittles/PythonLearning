# Elias Cerda
# The add function will add birthdays
# to birthdays dicitonary.
def add(birthdays):
    name = input('Enter a name: ')
    bday = input('Enter a birthday:')

# Add name if it doesn't exist.

    if name not in birthdays:
        birthdays[name] = bday
    else:
        print('That birthday already exists.')
