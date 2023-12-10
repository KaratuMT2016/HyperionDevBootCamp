# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# NameError: name 'Lion' is not defined
    # Lion is a string assigned to a variable "animal", therefore, should be in double quotes
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

# There is a logical error here
# Although, the program will run without any error as the syntax is correct and there are not runtime errors, the output is wrong
# To fix this:
    # we can apply the print format on the full_spec variable
    # swap the number_of_teeth with animal_type variables in print format statement
    # This will read the correct meaning
#full_spec = "This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth"
full_spec = f"This is a  {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"

# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)
# Insert parenthesis before and after "full_spec"
print(full_spec)

# https://github.com/skills-cogrammar/C5-Data-Science-Lecture-Backpack