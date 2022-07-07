""" Lab 10 – Classes

Personal Information Class:  
Design a class called Employee that holds the following data about an employee:
name
ID number
Department
Job Title

Class.   Store your class in a separate file called employee.py.

Your class will have an initializer method that will be passed the information entered by the user as arguments. 
 
Write appropriate accessor and mutator methods for each data attribute.   

Write a __str__ method to print the contents of the class (see example of __str__ on p. 523).


 Main program:
Your main program should create three instances of the class. 

Your program should get the information from the user and pass it as parameters to the initializer method.  

Using the __str__ method invoked by the print function, the program should display the personal information for the three individuals. 


Output and Sample Dialog:
Enter employee name: Mary Smith
Enter employee ID:  123456
Enter department: Accounting
Enter position: Accountant

Enter employee name: Joe Morales
Enter employee ID:  678910
Enter department: Engineering
Enter position: Engineer

Enter employee name: Marie Zinc
Enter employee ID:  45678
Enter department: Customer Service
Enter position: Customer Service Rep

Employee  1 :
Name: Mary Smith
ID number: 123456
Department: Accounting
Title: Accountant

Employee  2 :
Name: Joe Morales
ID number: 678910
Department: Engineering
Title: Engineer

Employee  3 :
Name: Marie Zinc
ID number: 45678
Department: Customer Service
Title: Customer Service Rep

Note:   You may not actually be using the setter and getter methods but to be complete, your class needs to include them.    
See Cellphone class example.  Instead of using this method of printing, invoke __str__  in main by using  print(object_name).
Turn in two files, employee.py and your main program (yourlastname_Lab10.py).
 """
 
#Importing class module
from Sifford_Lab10_employee import Employee
 
 
# Creating employee list and data
def create_list():
    employee_list = []
    
    num_of_employee = int(input("How many employees info would you like to enter?: "))
    
    for count in range(1, num_of_employee + 1):
        print("Employee ", count)
        name = input("Enter employee name: ")
        id = int(input("Enter employee id: "))
        dept = input("Enter employee dept: ")
        title = input("Enter the employee title: ")
        print()
        
        employee = Employee(name, id, dept, title)
        
        employee_list.append(employee)
        
    return employee_list


# Function for displaying data
def display_data(list):
    for emp in range(len(list)):
        print("Employee ", emp + 1)
        print("Name:", list[emp].get_name())
        print("ID Number:", list[emp].get_id())
        print("Department:", list[emp].get_dept())
        print("Title:", list[emp].get_title())
        print()


def main():
    
    employee_list = create_list()
    
    print("Employee info listed below")
    print()
    display_data(employee_list)
     
 
 

main()