# Sifford, Brittany
# Complete
# Takes quantity of software purchased and determines discount amount based on quantity then returns discount amount and total after discount.

# Price per package
software_price = float(149.00)

# Grabs the total amount of packages purchased
quantity = float(input("Enter the number of packages purchased: "))

# Calculate total without discount
total = software_price * quantity

# Discounts
discount_1 = 0.10
discount_2 = 0.20
discount_3 = 0.30
discount_4 = 0.40

# Determine Discount_Amount and Final_Total
if quantity == 0:
    print("No Software purchased.")
elif quantity < 10:
    discount_amount = 0.0
    print("Discount Amount: $", format(discount_amount, ',.2f'), sep='')
    print("Total Amount: $", format(total, ',.2f'), sep='')
elif (quantity >= 10 and quantity <= 49):
    discount_amount = total * discount_1
    final_total = total - discount_amount
    print("Discount Amount: $", format(discount_amount, ',.2f'), sep='')
    print("Total Amount: $", format(final_total, ',.2f'), sep='')
elif (quantity >= 50 and quantity <= 99):
    discount_amount = total * discount_2
    final_total = total - discount_amount
    print("Discount Amount: $", format(discount_amount, ',.2f'), sep='')
    print("Total Amount: $", format(final_total, ',.2f'), sep='')
elif (quantity >= 100 and quantity <= 149):
    discount_amount = total * discount_3
    final_total = total - discount_amount
    print("Discount Amount: $", format(discount_amount, ',.2f'), sep='')
    print("Total Amount: $", format(final_total, ',.2f'), sep='')
else:
    discount_amount = total * discount_4
    final_total = total - discount_amount
    print("Discount Amount: $", format(discount_amount, ',.2f'), sep='')
    print("Total Amount: $", format(final_total, ',.2f'), sep='')
