# Name - Brittany Sifford
# Status - Complete
# Description - The program grabs user input and based on input displays the course instructor, rooms, and time by using python dictionaries.

def main():
    # List to keep track of all courses - My thought process is not every course may have a room, or instructor or time.
    courses = ["CS101", "CS102", "CS103", "NT110", "CM241"]

    course_rooms = {
        "CS101": 3004,
        "CS102": 4501,
        "CS103": 6755,
        "NT110": 1244,
        "CM241": 1411
    }

    course_instructor = {
        "CS101": "Haynes",
        "CS102": "Alvarado",
        "CS103": "Rich",
        "NT110": "Burke",
        "CM241": "Lee"
    }

    course_time = {
        "CS101": "8:00 a.m.",
        "CS102": "9:00 a.m.",
        "CS103": "10:00 a.m.",
        "NT110": "11:00 a.m.",
        "CM241": "1:00 p.m."
    }

    course = input("Enter a course number or press enter to stop: ")

    while course != "":
      if course not in courses:
        print(course, "is an invalid course number.")
        course = input("Enter a course number or press enter to stop: ")
      else: 
        print("The details for course ", course, "are:")
        print("Room: ", course_rooms[course])
        print("Instructor: ", course_instructor[course])
        print("Time: ", course_time[course])
        course = input("Enter a course number or press enter to stop: ")
    

       

# Call main function
main()


