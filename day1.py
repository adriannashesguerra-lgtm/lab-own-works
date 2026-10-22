"""
I need to refresh my python knowledge, so I will be writing some code snippets to practice.
"""

# variables, datatypes, and collections

#variables containing different datatypes
name = "Adrian Nash" #this is a variable containing a string value
age = 18 #this is a variable containing an integer value
height = 160.0 #this is a variable containing a float value
is_student = True # this is a variable containing a boolean value

# lists
list_of_subjects = ["Math", "Science", "History", "English"] #this is a list containing string values

# adding an item to the list
list_of_subjects.append("Art") #this adds "Art" to the end of the list

# tuples
coordinates = (10.0, 20.0) #this is a tuple containing float values

# adding an item to the tuple
coordinates = coordinates + (30.0,) #this adds 30.0 to the end of the tuple

#dictionaries

student_info = {
    "name": "Adrian Nash", #this is a key-value pair where the key is "name" and the value is "Adrian Nash"
    "age": 18, #this is a key-value pair where the key is "age" and the value is 18
    "height": 160.0, #this is a key-value pair where the key is "height" and the value is 160.0
    "is_student": True #this is a key-value pair where the key is "is_student" and the value is True
}

# changing a value in the dictionary
student_info["age"] = 19 #this changes the value of the key "age" to 19
student_info["height"] = 165.0 #this changes the value of the key "height" to 165.0


"""
mini exercise for refreshing python knowledge using all the concepts above 
"""

name = input("Input your name: ").strip().title()
age = int(input("Input your age: "))
height = float(input("Input your height in cm: "))

sub = []
for i in range (3):
    sub_name = input(f"Enter sub number {i+1}: ").strip().upper()
    sub.append(sub_name)
    
student_status = input("Are you a student? (yes/no): ").strip().lower()
try:   
    if student_status == "yes":
        student_status = True
    else:
        student_status = False
except ValueError:
    print("Invalid input. Please enter 'yes' or 'no'.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    student_info = {
        "name": name,
        "age": age,
        "height": height,
        "subjects": sub,
        "is_student": student_status
    }
    print("===Student Info===")
    print(f"Name: {student_info['name']}")
    print(f"Age: {student_info['age']}")
    print(f"Height: {student_info['height']} cm")
    print(f"Subjects: {', '.join(student_info['subjects'])}")
    print(f"Is Student: {student_info['is_student']}")
    print("==================")