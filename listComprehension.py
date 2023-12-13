num_list = ['1', '2', '3', '4', '8', '16', '32', '64']
new_num_list = [int(item) for item in num_list]

print(num_list)
print(new_num_list)

list_multi = [(item * 2) for item in new_num_list]
print(list_multi)
#string_list = ["John", "Victor", "Jessica", "Karatu"]
#new_string = [string_list.append()]
# split_string_to_list1.append(word.upper()) 

#andiswab@hyperiondev.com

my_tuple = [(1, 'John'), (2, 'Victor'), (3, 'Jessica')]

#print(key)
my_dict = dict(my_tuple)

print(my_dict)

my_tuple1 = ("001", "John")
key, value = my_tuple1

print(key)
print(value)
print(my_tuple1)

string_list = ["John", "Victor", "Jessica", "Karatu"]

new_string = [(item *2) for item in string_list]

print(new_string)