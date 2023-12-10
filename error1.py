# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

################################### print "Welcome to the error program" ##################################################

# SyntaxError - the print() function syntax was not complied with - missing parenthesis
print("Welcome to the error program")


################################################# print"\n" ##############################################################

# IndentationError - encounter an unexpected indentation - this is a type of syntaxError
# SyntaxError - the print() function syntax was not complied with - missing parenthesis 
print("\n")

# Variables declaring the user's age, casting the str to an int, and printing the result
'''
 age_Str == "24 years old" 
    age = int(age_Str) 
    print("I'm" + age + "years old.")
'''
# Indentation error - encounter an unexpected indentation - this is a type of syntaxError
# NameError: name 'age_Str' is not defined: - NameError is a runtime error
    # We need to change the logical operator "==" to an assignment operator "=" (i.e., remove one of the equality signs) 
# ValueError: invalid literal for int() with base 10: '24 years old' - this is a runtime error
    # The variable "age_str" - character string cannot be casted as ineteger datatypes
    # To correct this - the string "year old." need to be renoved from the "age_str"
    # If we remove the string "year old.", the age_str can then be casted to an integer datatype correctly
age_Str = "24" 

# TypeError: can only concatenate str (not "int") to str - this is a run time error
    # This error occured because the datatype of "age" has changed from a string to an integer using the casting in-built function int()
age = int(age_Str)

# The plus sign operator only concatenate strings to string of which "age" is not
    # To fix this, we need:
        # To remove the plus signs that wrongly concatenate the strings with the value of "age"
        # Replace the with curly braces around age - {age}
        # Introduce a print format - f"..."
print(f"I'm {age} years old.")


'''
years_from_now = "3"
    total_years = age + years_from_now

print "The total number of years:" + "answer_years"
'''
    # Variables declaring additional years and printing the total years of age
# Indentation error - encounter an unexpected indentation - this is a runtime error
    # Remove all the indentations 
# Remove the quotation marks around 3 to convert "years_from_now" to integer dataType from string dataType
# Alternatively, type cast the string in "years_from_now" to an interger dataType - int(years_from_now)
years_from_now = "3"
years_from_now = int(years_from_now)

total_years = age + years_from_now 

########################### print "The total number of years:" + "answer_years" ######################################

# SyntaxError - the print() function syntax was not complied with - missing parenthesis
# TypeError(i.e., runtime error): unsupported operand type(s) for +: 'int' and 'str'
    # Here, the concatenation is runtime error and 
    # Also, there is a logical error even when we put in the correct operattor
    # The logic behind this is to output the total number of years (i.e., "total_years")
    # Therefore, we renove the string "answer_years" and replace it with the variable "total_years" seprated by a comma

print(f"The total number of years: {total_years}")

# Variable to calculate the total amount of months from the total amount of years and printing the result
# NameError: name 'total' is not defined - this is a runtime error
    # To correct this we replace the undefined variable with "total_years"
total_months = total_years * 12


############################# print "In 3 years and 6 months, I'll be " + total_months + " months old" #######################

# Syntax Error - the print() function syntax was not complied with - missing parenthesis
# TypeError: can only concatenate str (not "int") to str - this is a run time error
    # Replace the oprator (+) with commas (, totL_months ,)
# There is a logical error here:
    # The 6 months are not accounted for in the computation to make the printed statement True
        # To fix this:
            # Create a variable "six_months"
            # Assign an integer value 6 to it
            # Add the six_mionths to the total_months

six_months = 6
total_months = total_months + six_months
print(f"In 3 years and 6 months, I'll be {total_months} months old.")

#HINT, 330 months is the correct answer