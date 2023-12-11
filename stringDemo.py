string = "Hello World!"

print(string[0])
print(string[1])
print(string[2])
print(string[3].upper())
print(string[4].upper())

# Prints the range of the string from index 0 to index 4 not including index 5
newString = string[0:5]
print(newString)

# Strips white spaces at the beginning and at the end of a string
newString_1 = string.strip("'")
print(newString_1)

# Finds index 11 and return -1 because index 11 doesn't exist
newString_2 = string.find("11")
print(newString_2)

# Finds and replaces "World" with "Uninverse"
newString_3 = string.replace("World", "Universe")
print(newString_3)

# Splits a string by "l" as a delimeter
newString_4 = string.split("l")
print(newString_4)

# Append puts an addiotnal item to a list at the of the list
# Here Nifemi was appended to the list, thus the list now has 6 items as against the original 5
list = ["John", "Victor", "Jessica", "Brian", "Michell"]
newString_5 = list.append("Nifemi")
print(list)

# Join two items in the list by the symbol "@"
newList = "@".join(["john", "karatu.com"])
print(newList)

# Escape Sequence
print("Hello \n\"Bob\"")


# Building a String using .format()
name = "Peter"
print("Hello, {}!".format(name))
print(f"Hello, {name}!")


# This program takes even numbers at most 50 and add to the string number_builder
number_builder = ""
i = 0
while i <= 50:
    if i % 2 == 0:
        number_builder = number_builder + str(i) + " "
    i += 1
print(number_builder)

# Same program as above in a different way using a list instead

number_builder = []
i = 0
while i <= 50:
    if i % 2 == 0:
        number_builder.append(str(i))
    i += 1
print(" ".join(number_builder))