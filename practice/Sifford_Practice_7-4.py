# Name - Brittany Sifford
# Status - Complete
# Description - This program generates a 2-D list with the values in the sub-list being numbers entered from the user. The program  displays the 2-D list then displays each element in the 2-D list and displays the total value of all the elements


def main():
  rows = 4
  cols = 2
  #Creates main list
  arr = []
  
  #Looping through first list
  for i in range(rows):
    #create sub list
    col = []
    #Looping through sub list
    for j in range(cols):
      #Letting user enter values for sublist
      col.append(int(input("Please enter a number: ")))
    #After values entered into sub list append to main list
    arr.append(col)
    
  #Display final list form
  print(arr)
  
  #Getting sum and displaying each number
  
  total = 0
  
  for i in arr:
    #print(i)
    for j in i:
      #Display each element 
      print(j)
      total += j
      
  print("Total of all elements is: ", total)
  
main()





