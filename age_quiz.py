'''
• Start by creating a python file
• Name the python file age_quiz.py
• Write a comment in the file outlining the steps in writing the code
• Take a user's age and cast it to integer datatype
• Use a while loo and set the boolean condition to True:
    • Use a try for exception handling:
        • Use the if...elif...else statement to set the different conditions:
            • if user's age is greater than 100:
                • output "Sorry you're dead."
            • else if user's age is gretaer than or equal 65:
                • output "Enjoy your retirement."
            • else if user's age is greater than or equal 40:
                • output "You're down the hill."
            • else if user's age is equal 21:
                • output "Congrats on your 21st"
            • else if a user's age is below 13:
                • output "You qualify for the kiddie discount."
            • otherwise:
            • output "Age is but a number."
        • End of the if...elif...else statement to set the different conditions
    • Catch the exceptions:
        • Excetion handling error message
• End
'''
# START
while True:
    try:
        your_age = int(input("Please, enter your age : "))

        print()

        if your_age > 100:
            print("Sorry you're dead.")
            print()
            break
                
        elif your_age >= 65:
            print("Enjoy your retirement.")
            print()
            break

        elif your_age >= 40:
            print("You're over the hill.")
            print()
            break

        elif your_age == 21:
            print("Congrats on your 21st.")
            print()
            break

        elif your_age < 13:
            print("You qualify for the kiddie discount.")
            print()
            break
            
        else:
            print("Age is but a number.")
            print()
            break

    except ValueError:
        print()
        print("Invalid input. Please enter a valid age.")
# END