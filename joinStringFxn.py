def join_strings(str1, str2):
    return str1 + " " + str2

joined_string = join_strings("Hello", "Karatu!")

print(joined_string)

def using_join(list_names):
    return ' '.join(list_names)

stringlist = ["Hello", "my", "name", "is", "Karatu", "John"]

result = using_join(stringlist)

print(result)

def calculate_average(values):

    if not values:
        return "The list is empty."
    total = sum(values)
    average = total/len(values)
    return average

list_of_values = [1,2,3,4,5]

result = f"The average is = {calculate_average(list_of_values)}"

print(result)