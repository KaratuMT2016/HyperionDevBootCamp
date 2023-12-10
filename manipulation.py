'''
• Start by creating a python file
• Name the python file manipulation.py
• Write a comment in the file outlining the steps in writing the code
• Input a sentence for manipulation
• Declare and empty string to populate later
• Compute the length of the sentence
• Print the length of the sentence
• Get the last letter of the sentence
• Replace every occurence of the last letter of the sentence with @
• Print the sentence with the replaced chratcter (@)
• To print the last 3 letters of the sentence in the reverse order:
    • Reverse the sentence
    • Use a for loop to traverse the sentence 
        • Use an if statement to get the first 3 chracters 
        • concatenate the 3 charcaters in the empty string declared earlier
        • Once the if condition is satisfied, break out of the if condition aand print the result
• To print first 3 charcaters and the last 2 charcaters of the sentence and make up a word with 5 charcaters
    • Slice the sentence to get the first 3 characters and save it in a seprate variable
    • Slice the sentence again to get the last two chracters and save it in a seperate variable
    • Use the print format to print the resultant word
• End the program
'''

str_manip = input("Please, enter a sentence : ")

reverse_three_xters = " "

sentence_length = len(str_manip)
print("Length of the sentence is :", sentence_length)

# These lines of code finds the last character in the saved response and replace it with @
last_letter = str_manip[-1]

last_letter_replaced = str_manip.replace(last_letter,"@")
print("All occurences of the last xter replaced with @: " + last_letter_replaced)

#This lines reverses the response saved in str_manip and print the last three elements of a string.
last_three_letters = str_manip[sentence_length::-1]

for i in range(sentence_length):
    if i < 3:
        reverse_three_xters += last_three_letters[i]
    else:
        break
print("The last 3 xters backwards are:" + reverse_three_xters + "\n") 

#These lines take the first 3 xters and the last 2 xters of the sentence and make up a word with 5 xters
three_xters = str_manip[:3]
two_xters = str_manip[-2:]
print(f"This word - {three_xters}{two_xters} - is made up from the first 3 xters and the last two characters of the sentence. \n")