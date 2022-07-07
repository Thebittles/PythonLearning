# Corbin Zang       Practice 9-1
# Change and Delete functions

# Change function allows user to change the
# value of an existing key.
def change(birthdays):

    # Getting the entry to edit from the user
    entry = input('Enter an entry to edit: ')

    # Checking that the entry exists and printing an error if the
    # entry is not found
    if entry not in birthdays:
        print('There is no entry:', entry)

    # Changing the value of the key
    else:

        # Printing the current entry the user has selected
        print('Editing', entry, 'whose birthday is', birthdays[entry])
        print()

        # Getting the new value
        new = input('Enter a new birthday: ')

        # Setting the new value to the chosen key
        birthdays[entry]=new

        # Printing the new key and value pair
        print(entry, 'has been changed to have a birthday of', new)

    # Returning the updated dictionary
    return birthdays

# delete deletes existing key and value pairs
def delete(birthdays):

    # Getting the key to delete
    entry = input('Enter an entry to delete: ')

    # Deleting key if found in the dictionary
    if entry in birthdays:
        del birthdays[entry]
        print('The entry', entry, 'has been deleted.')
        
    # Printing an error if the key is not found
    else:
        print('There is no entry:', entry)

    # Returning the updated dictionary
    return birthdays

