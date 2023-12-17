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