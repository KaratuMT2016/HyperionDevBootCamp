'''
A program that reads in a string and makes each alternate
character into an upper case chracter and each other alternate
character a lower case character. Then take thesame string but 
making each alternative word lower and upper case

• START
• Declare a string variable containing the string
• Declare another empty string that will hold the alternated string
• Introduce a for loop using range to get the length of the string
    • Using if...else statement
        • Apply modulo to get all the even index
        • Using in-built function upper() change the character at that index to upper case
        • Else Save the character at that index as it is on the empty string
• At the end of the for loop:
    • Print the what use to be the empty string
• Take the string and turn it into a list
• Declare another empty list that will hold the altered words in the list
• Initialize a for loop:
    • The for loop should take two variables "index" and "word" to enumerate the list
        • Using and if...else statement
            • compare to check of the modulo of the index equals zero
                • if True alter the word at that index to upper case
                • else alter it to lower case
• Concatenate the words in the list using join separated by white space
• Print the concatenated result 
• END
'''

# The next two lines below decalred two string variables 
# One containing a string and the other is an empty string
string = "i am learning to code"
newString = ""

# A for loop that iterates through the string using the index 
for index in range(len(string)):

    # The modulo of index is computed and compared to zero
    if index % 2 == 0:

        # the even index is changed to upper case 
        newString += string[index].upper() 
    else:

        # the charcater at that index is left the same
        newString += string[index].lower()

# The alternate string is printed at the end of the for loop
print(newString)

# convert the string literal into a list
split_string_to_list = string.split()

# declare an empty list
split_string_to_list1  = [] 

# Enumerate through the split_string_to_list list
for index, word in enumerate(split_string_to_list):

    # if modulo is compared to 1
    if index % 2 == 1: 

        # print the word at that index in upper case
        split_string_to_list1.append(word.upper()) 

    else:
        
        # print the word at that index in lower case
        split_string_to_list1.append(word.lower()) 

# String the words to gether into a single string seprated by white space
result_string = " ".join(split_string_to_list1) 

# print the concatenated string result
print(result_string) 