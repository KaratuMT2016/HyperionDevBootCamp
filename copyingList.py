'''
This is python program using the copy( ) function to manipulate lists'
It empasizes the similarity between slicing a list and the difference with deepcopy()function
• y = x[:] - makes reference to the actual list x
• y = copy.copy(x) does the same thing as y
• Any manipulations you do to y in both instances modifies x list itself. It is called shallow copy
• y = copy.deepcopy(x) - makes a copy of x and modify it without altering x itself. This is called deepcopy
'''

import copy

x = [[1,2,3,4], [5,6,7,8,9]]
print("List_x:", x)
y = x[:]
u = copy.copy(y)
z = copy.deepcopy(x)

x[0][3] = 100
z[1][4] = 200

print("List_x_modified:", x)
print("List_y:", y)
print("List_z:", z)
print("List_u:", u)