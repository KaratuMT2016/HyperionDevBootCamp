'''
• Start by creating a python file
• Name the python file replace.py
• Write a comment in the file outlining the steps in writing the code
• Create string variable to save the sentence
• Using thesame name as the string variable created, call the replace function on the string variaple and pass the replace parameters
• Declare another string variable and call the upper function to change the letters od the string to uppercase
• Print the upper the uppercase strings
• Use slicing to revers the letters of the single string and save it in a new variable
• Print the reverse single-string 
• End the program
'''

# This is the single string assigned to a variable called single_string
single_string = "The!quick!brown!fox!jumps!over!the!lazy!dog."

#This line of code uses the replace() function to remove the symbol "!" and replace it with a space
single_string = single_string.replace("!", " ")

#This line of code converts the string to uppercase letters using the built-in function upper()
single_string1 = single_string.upper()

print(single_string1)

#This line of code reverses the single string
reverse_letter = single_string[::-1]


#This line prints the single string in a reverse order
print(reverse_letter)
