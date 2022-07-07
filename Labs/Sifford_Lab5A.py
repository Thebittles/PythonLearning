# Brittany Sifford
# Status - Complete
# Description - This program takes the score of 5 critics and calculates the average, then determines star rating between 0-5 based on average



#We could make it more dynamic by passing in how many people will be critic into the function and making the loop run for that amount.
# Number of Food Critics
number_food_critics = 5

def main():
    #Accumulated total of critics rat
    accum_score = 0
    
   # For loop to ask 5 critic to enter a score
    for critic in range(1, number_food_critics + 1):
        score = int(input("Enter critic score between 0-10: "))
        accum_score += score
        # Input validation
        while score < 0 or score > 10:
            print("You did not enter a rating number between 1 and 10.")
            score = int(input("Enter critic score between 0-10: "))
            accum_score += score
    #Average score
    avg_score = accum_score / number_food_critics
    print(avg_score)
    determine_stars(avg_score)

def determine_stars(avg_score):
    if avg_score >= 9:
        print("Your score of", avg_score, "gives you *****")
    elif avg_score <= 8.9 and avg_score >= 8:
        print("Your score of", avg_score, "gives you ****")
    elif avg_score <= 7.9 and  avg_score >= 7:
        print("Your score of", avg_score, "gives you ***")
    elif avg_score <= 6.9 and  avg_score >= 6:
        print("Your score of", avg_score, "gives you **")
    elif avg_score <= 5.9 and avg_score >= 5:
        print("Your score of", avg_score, "gives you *")
    else:
        print("Your score of", avg_score, "gives you no stars")
        
    


#Call Main Functionc
main()



