# Brittany Sifford
# Status - Complete
# Display Year, and accumlated ocean rise in millimeters

# Problem 2


 #1.8 millimeters
rise_amount = 1.80

accumulated_rise = 0

#Duration of years
years = 25

print('Year\tRise (in millimeters)')

for year in range(1, years + 1, 1):
    accumulated_rise += rise_amount
    print(year, '\t', format(accumulated_rise, '.2f'))