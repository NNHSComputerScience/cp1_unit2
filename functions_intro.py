"""
# demo of a function for help in understanding the online textbook

# FUNCTION - a named sequence of statements that belong together and accomplish a task.

The syntax for a function definition is:
def name( parameters (optional) ):
    statements
    return statement(optional)
"""

# FUNCTION DEFIITION - creating your own function

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
    # return keyword returns a value from the function, ending the function's execution 
    return letter_grade

# using (CALLING) our new function 
grade1 = calc_grade(85)
grade2 = calc_grade(91)
print("Grade 1", grade1)
print("Grade 2", grade2)
