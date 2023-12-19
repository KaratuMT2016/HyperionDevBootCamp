field = [
[".","m",".","."],
["m",".",".","."],
[".","m",".","."],
[".","m",".","."],
[".","m",".","m"]

]

for row in range(len(field)):

    for col in range(len(field)-1):
        if field[row][col] == 'm':
            print('The current position we are on is a mine')
        elif field[row][col] == '.':
            print("It is safe to proceed!")