sentence = "Hello World"
final_string = " "
sentence_count = len(sentence)
"""
for i in range(sentence_count):
    print(i)
print(sentence)

for i in range(sentence_count):

    if i % 2 == 0:
        final_string += sentence[i].upper()
    
    else:
        final_string += sentence[i].lower()
print(final_string)
"""

my_dictionary = {
    "name": "Karatu", 
    "age": 24, 
    "is_funny": False
    }

print(my_dictionary["name"])

#Using for loop to print dictionary keys
for i in my_dictionary.keys():
    print(i)

#Using for loop to print dictionary values
for i in my_dictionary.values():
    print(i)

#Using for loop to print both key and value using item() built-in function

for i,j in my_dictionary.items():
    print(i,j)

#using the dictionary built-in function

cars = dict(make="Benz", colour="Silver", year="2015")

print(cars)

#To append a key-pair

cars["Model"] = "C-class"
print(cars)

#To remove a key-pair
pop_item = cars.pop("Model")
print(cars, pop_item)