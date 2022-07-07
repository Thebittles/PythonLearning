#User monthly gross pay
monthly_gross = float(input("Enter gross monthly pay "))
#2. Accept input of monthly paycheck deductions (one number) from the user.
#Monthly Paycheck Deductions
monthly_deduction = float(input("Enter total monthly paycheck deduction "))
# Calculate net monthly income and format
net_monthly_pay = (monthly_gross - monthly_deduction)
#Display Monthly net income
print("Monthly Net: $", format(net_monthly_pay, '.2f'), sep='')
#12 months in a year
number_of_months = 12
#Calculate yearly gross by taking monthly gross and multiple by 12 months 
yearly_gross = format((monthly_gross * number_of_months), ',.2f')
#Print Yearly Gross 
print("Yearly gross pay: $", yearly_gross, sep='')
#Calculate yearly net pay by taking monthly net pay and multiply by 12 months 
yearly_net = format((net_monthly_pay * number_of_months), ',.2f')
#Print Yearly Net
print("Yearly net pay: $", yearly_net, sep='')


