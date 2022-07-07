# Brittany Sifford
# Status - Complete
# Description - The programs displays step-by-step instructions for making a peanut butter & jellyy sandwhich

def main():
  #Display Startup Message
  startupMessage()
  input("Press Enter to see step 1: ")
  #Display Step 1
  step1()
  input("Press Enter to see step 2: ")
  #Display Step 2
  step2()
  input("Press Enter to see step 3: ")
  #Display Step 3
  step3()
  input("Press Enter to see step 4: ")
  #Display Step 4
  step4()
  input("Press Enter to see step 5: ")
  #Display Step 5
  step5()
  # Display Exit Message
  exitMessage()

 
#Starting Message
def startupMessage():
  print("Hello this is how you make a sandwich.")
  print()

#Step 1 
def step1():
  print("Step 1: Make sure you have the following items: ")
  print("Bread")
  print("Peanut Butter")
  print("Jelly")
  print("Knife")
  print("Plate")
  print()

#Step 2
def step2():
  print("Step 2: Take 2 slices of bread and lay them on your plate")
  print()

#Step 3
def step3():
  print("Step 3: Use your knife to spread peanut butter across one of your slices of bread on one side.")
  print()
  
#Step 4
def step4():
  print("Step 4: Clean your knife and repeat step 3 but with Jelly on the other slice of bread.")
  print()

#Step 5
def step5():
  print("Step 5: Take both slices of bread and put them together spread sides touching.")
  print()
  
#Outro Message
def exitMessage():
  print("Goodbye and enjoy! Yum!")



#Calls the main function
main()
    


