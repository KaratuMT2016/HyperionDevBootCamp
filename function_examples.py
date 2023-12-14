greeting = lambda : print('''
Aspiring Data Analyst with a strong background 
in Data Science, skilled in SQL, SQLite, Data Analysis,
Data Modelling, Machine Learning, and Data Analytics. 
Graduated top of the class in a HyperionDev Data Science 
boot camp.
'''.lower())

add_numbers = lambda x,y,z : (x+y+z)


custom_greeting = lambda name : print(f"Welcome {name}!")
user_name = input("Please, enter your name : ")
custom_greeting(user_name)

greeting()
print(add_numbers(1,2,3))
#print(add_numbers)


##########Recursion###########

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def add_list(list, index):
    if index == 0:
        return list[index]
    return list[index] + add_list(list,index - 1)

print(factorial(5))
list = [1,2,3,4,5,6,7,8,9]
index = int(input("Please, enter an index : "))
print(add_list(list, index))