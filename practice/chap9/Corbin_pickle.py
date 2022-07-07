# Corbin Zang    Practice 9.2

# This program pickles the birthday dictionary

# Importing the pickle module
import pickle

def save(bdays):

    # Creating a .dat file to write to
    outfile = open(r'/Users/brittany/Desktop/Classes/Spring22/Progamming1/practice/chap9/birthdays.dat', 'wb')

    # Dumping the contents of the 
    pickle.dump(bdays, outfile)

    # Closing the .dat file
    outfile.close()

    
