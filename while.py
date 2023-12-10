'''
• A program that continually asks the user to enter a number
• When a user enters -1, the program stops requesting the user to enter number
• The program will the compute the average of the numbers entered excluding the -1

• Start by creating a python file
• Name the python file while.py
• Write a comment in the file outlining the steps in writing the code
• Initialize two variable for the counter and summation of numbers entered
• While loop condition remain true, keep summing the numbers
• When the termination condition is entered
• Break out of the loop and print the average
• End
'''
# This line of code allows user to enter a number
number = int(input("Enter a Number: "))

# The variables count and number_sum are initialized to zero
count = 0
number_sum = 0

#The while loop condition is set
while not number == -1:

    try:

            #This line increments the counter for any entry that satisfies the while condition
            count = count + 1
            
            #This line keeps adding every number entered
            number_sum =  number_sum + number
                
            number = int(input("Enter a Number: "))

    except Exception as e:
         print(e)
#Here the average is computed and printed
average = number_sum/count 
print(f"The average of the {count} numbers is {average}.")