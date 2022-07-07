# Name - Brittany Sifford
# Status - Complete
# Description - This program generates a seven lottery numbers ranging from 0-9 and then displays them


import random

lottery_numbers = [0] * 7

for number in range(7):
    lottery_numbers[number] = random.randint(0,9)
    
print(lottery_numbers)

for number in lottery_numbers:
    print(number)
