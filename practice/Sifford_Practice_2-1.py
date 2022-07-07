
#Practice Ch. 2-1


#This is a comment
#This is another comment

#Input for cost of Hamburger as float
hamburger = float(input("Enter cost of Hamburger "))

#Input for cost of fries as float
fries = float(input("Enter cost of Fries "))

#Input for cost of Shake as float
shake = float(input("Enter cost of Shake "))

#Calculate the total cost and display with appropriate message (Example: The cost is: $45)
total_cost = hamburger + fries + shake

#Printing the total cost
print("The cost is: $", sep='', end='')
print(total_cost)

# Calculate the avg cost and stores it in a variable 
avg_cost = (total_cost / 3)
print("The average cost is: $", sep='', end='')
print(format(avg_cost, '.2f'))



#Practice assignment 