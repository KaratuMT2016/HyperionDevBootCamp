'''
• Start by creating a python file
• Name the python file details.py
• Write a comment outlining the steps in writing the code
• Input a user name
• Input a user age
• Input House Number
• Input Street Name
• print a new line
• Output the input variables by concatinating each of the variables with strings to form a sentence
• Exit the program
'''

name = input("Enter your Name :")

age = input("Enter your Age :")

house_number = input("Enter your House Number :")

street_name = input("Enter Street Name :")


print("\n")

#print("This is " + name + ", aged " + age + " years old, and lives at number " + house_number + " " + street_name + ".")

sentence = "This is {}, aged {} years old, and lives at number {} {}.".format(name, age, house_number, street_name)
print(sentence)