# Name - Brittany Sifford
# Status - Complete
# Description - This program generates two list containing five random numbers in the range of 1-10. The program then joins the two list displays the joined list, then gets the total of the joined lists and prints. Finally displays the lowest and highest value from the joined list

import random


def main():
  print("Main")
  
  list1 = [0] * 5
  list2 = [0] * 5

  index = 0
  while index < (len(list1) and len(list2)):
    list1[index] = random.randint(1, 10)
    list2[index] = random.randint(1, 10)
    index += 1
  
  list3 = list1 + list2
  list3.sort()
  
  total = total_list(list3)
  
  print("The list..", list3)
  print("The total of the list is...", total)
  print("The lowest and highest value in the list", min(list3), "and", max(list3))

	


def total_list(num_list):
  
  total = 0
  
  for value in num_list:
    total += value
    
  return total


main()