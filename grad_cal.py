while True:
    try:
        print ("Welcome to the Grade Calculator")
        name = input("Enter your name: ").strip().title()
        num_subjects = int(input("Enter the number of subjects: "))

        total_score = 0
        for i in range (num_subjects):
            score = float(input(f"Enter your Grade {i+1}:  "))
            total_score += score
        average_score = total_score / num_subjects
        print (f"\nName: {name}\nAverage Grade: {average_score:.2f}")
        
    except ValueError:
        print("Invalid input. Please enter numeric values for grades.")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        if average_score >= 75:
            print("Remarks: Passed")
            break
        else:
            print("Remarks: Failed")
            break
    finally:
        print("\nGrade Calculation Completed.")
        