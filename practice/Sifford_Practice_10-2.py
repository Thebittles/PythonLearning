



class Pet:
  
  def __init__(self):
   #Data attributes
    self.__name = 0
    self.__type = 0
    self.__age = 0
  
  # Method - Set the name
  def set_name(self, name):
    self.__name = name
  
  #Method - Set the animal type
  def set_type(self, type):
    self.__type = type
    
  # Method - Set the animal age
  def set_age(self, age):
    self.__age = age
  
  # Method - Gets the name
  def get_name(self):
    return self.__name
  
  # Method - Gets the animal type
  def get_animal_type(self):
    return self.__type
  
  # Method - Gets the age
  def get_age(self):
    return self.__age
    



def main():
  
  #Create Instance
  animal = Pet()
  
  #Get name from user
  name = input("Pleae enter the pet name: ")
  # Set the name
  animal.set_name(name)  
  
  
  # Get type from user
  type = input("Please enter the pet type: ")
  # Set the type
  animal.set_type(type)
  
  # Get age from user
  age = int(input("Please enter the age of the pet: "))
  # Set the age
  animal.set_age(age)
  
  print()
  print("Your pets name, type, and age is..")
  print(animal.get_name())
  print(animal.get_age())
  print(animal.get_animal_type())
  


  

main()