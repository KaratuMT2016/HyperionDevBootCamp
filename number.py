'''
• Start by creating a python file
• Name the python file number.py
• Write a comment in the file outlining the steps in writing the code
• Defined a function called compute_integers that will compute:
   • compute the sum the 3 integers
   • compute the difference of the 1st and 2nd integer
   • compute the product of the 1st and 3rd integer
   • Introduce an if conditional statement to:
      • compute the sum of 1st, 2nd, and 3rd integers and divide by 3rd integer
      • print the result
      • else:
      • catch division by zero
      • print the exception statement
   • return the sum, difference, and product
• Enter the 3 integers
• Create an instance of the defined function
• Pass the 3 integers inputed as parameters:
    • compute the sum, difference, and product
    • print the results
• End of program
'''
# Defined a function called compute_integers 
def compute_integers(x,y,z):
    
    sum = x + y + z
    subtr = x - y
    multi = z * x

    # The if condition catches division by zero, which is undefined
    if z != 0:
        avg = (x + y + z)/(z)
        print(f"\n The sum of {x}, {y}, and {z} divide by {z} is = {avg}")
        
    else:
        print(f"\n The sum of {x}, {y}, and {z} divide by {z} is undefined")
        
    return sum, subtr, multi

# Enables a user to enter the 3 integers
first_integer = int(input("Please, enter the first Integer : "))
second_integer = int(input("Please, enter the second Integer : "))
third_integer = int(input("Please, enter the third Integer : "))

#Create an instance of compute_integers function and pass the 3 integers entered as parameters
sum, subtr, multi = compute_integers(first_integer,second_integer,third_integer)

#Compute the sum, difference, and product of the integers accordingly and print the results
print(f"\n The sum of 3 integers = {sum},\n The difference btwn 1st and 2nd integer = {subtr}, \n The product of the 1st and 3rd integer = {multi} \n")