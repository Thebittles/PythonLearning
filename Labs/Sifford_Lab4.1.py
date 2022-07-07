# Brittany Sifford
# Status - Complete
# Description - Takes total amount budgeted from user input, keeps asking user to input an expense until they enter 0,  then prints budgeted amount, amount spent, amount over or under budget


# Problem 1

budgeted_amount = float(input("Enter amount budgeted for the month: "))

accum_amountSpent = 0

amount_spent = float(input("Enter amount spent(0 to quit) : "))
accum_amountSpent += amount_spent

#While amount is not equal to 0 keep asking for amount_spent and added to accumulated amount
while amount_spent != 0:
    amount_spent = float(input("Enter amount spent(0 to quit) : "))
    accum_amountSpent += amount_spent

#Final amount 
final_amount = budgeted_amount - accum_amountSpent

print("Budgeted: $", format(budgeted_amount, ',.2f'), sep='')
print("Amount Spent: $", format(accum_amountSpent, ',.2f'), sep='')

#Determines if user is over or under budget
if final_amount < 0:
    print("You are $", format(final_amount, ',.2f'), " over budget. PLAN BETTER NEXT TIME!", sep='')
else:
 print('You have $', format(final_amount, ',.2f'), " left over on your budget. Good job!", sep='')



