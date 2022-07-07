# Brittany Sifford
# Program Status: Complete
#This program converts original recipe amounts to desired amount of servings.

num_of_servings = float(input("Enter the number of servings of spaghetti sauce you want to make: "))

#Original amount of servings is 4
original_recipe_serving = 4.0

print("To make", num_of_servings, "servings of spaghetti sauce, you will need: ")

# Original recipe: 2cups of tom sauce / 4
tomato_sauce = ((2.0 / original_recipe_serving) * num_of_servings)

# Original recipe: 1/3cup of tom paste
tomato_paste =  format((((1/3) / original_recipe_serving) * num_of_servings) , '.3f')

# Orignal recipe: 2 cloves of garlic
cloves_garlic = ((2.0 / original_recipe_serving) * num_of_servings)

# Original recipe: 1tbl of oregano
oregano = ((1.0 / original_recipe_serving) * num_of_servings)

print(tomato_sauce, "cups of tomato sauce")
print(tomato_paste, "cups of tomato pasate")
print(cloves_garlic, "cloves of garlic")
print(oregano, "tablespoons of oregano")