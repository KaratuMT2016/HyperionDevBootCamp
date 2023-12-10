'''
• A python program that output the star pattern:
*
**
***
****
*****
****
***
**
*
• Start by creating a python file
• Name the python file pattern.py
• Write a comment in the file outlining the steps in writing the code
• Define a function
• Initialise the 1st for loop:  
    • set the index variable of the for loop
    • set the range() value to the integer parameter passed to the defined function
    • print the symbol multiplied by the index incremented by 1 - symbol x (index + 1)
• Initialise the nested for loop:
    • within the range() function of the for loop enter 3 variables (start: stop: step):
        • the index of the nested for loop - this takes the last index value of the for loop
        • Start variable - parameter value passed to the defined function and substract 1 from it
        • Stop variable - indicate when the iteration will stop
        • step variable - keeps decrementing the value of the index of the nested for loop by 1
        • multiply the input string by the index value of the nested for loop and 
        • print the string to get the reverse pattern
• End
'''
def star_pattern(n):
    # Traverse the first half of the rows
    for i in range(n):
        # Print stars string
        print("*" * (i + 1))

    # Traverse the second half of the rows
    for i in range(n - 1, 0, -1):
        # Print stars string in reverse
        print("*" * i)

# Print a star pattern with 5 asterisks
star_pattern(5)