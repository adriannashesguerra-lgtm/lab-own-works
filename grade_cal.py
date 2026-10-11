def grade_calculator ():
    #greet
    print ("Welcomome to the Grade calculator!")
    name = input ("Enter your name: ").strip().title()
    score = int(input("enter your score: [1-100] "))
    
    #calculate the grade
    if score == 100:
        grade = "A"
    elif score >= 90:
        grade = "B"
    elif score >= 80:
        grade = "C"
    elif score >= 70:
        grade = "D"
    elif score >= 60:
        grade = "E"
    elif score < 59:
        grade = "F"
    else:
        print ("You entered an invalid input")
        return

    print ("\nGrade Calculator")
    print (f"Name: {name}")
    print (f"Score: {score}")
    print (f"Grade: {grade}")
grade_calculator ()