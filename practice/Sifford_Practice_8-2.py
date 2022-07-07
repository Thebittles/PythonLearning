# Name - Brittany Sifford
# Status - Complete
# Description - This program ask the user to input a senetence and flips case of each character in the sentence except special characters or numbers


#Note - I could have used the swap case here  out of curiosity professor would the swapcase method execute faster than the code below? For in JavaScript for loops execute faster majority of the time over the built in methods 

def main():
    sentence = input("Enter a sentence: ")
    
    print("Original: ", sentence)
    new_sentence = ''
    
    for ch in sentence:
        if ch.islower():
            new_sentence += ch.upper()
        elif ch.isupper():
            new_sentence += ch.lower()
        else:
            new_sentence += ch
            
    print("New: ", new_sentence)

main()


