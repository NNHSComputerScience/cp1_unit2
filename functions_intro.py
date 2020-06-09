# function definition - creating your own function
#   not required to know yet, this is just a demo

def calc_grade(percentage): 
    """takes in a percentage and prints the appropriate letter grade"""
    if(percentage >= 90):
        letter_grade = "A"
    # this overchecks the value of percentage
    #   We know that percentage must be < 90 if the
    #       elif is executed.
    #elif(percentage >= 80 and percentage < 90):
    elif(percentage >= 80):
        letter_grade = "B"
    elif(percentage >= 70):
        letter_grade = "C"
    elif(percentage >= 60):
        letter_grade = "D"
    else:
        letter_grade = "F"
    
    print("The grade is " + letter_grade)

# using (calling) our new function 
calc_grade(85)
calc_grade(91)
