names = ["Hello", 1, 8.6, True]


two_dee = [[1,2,3], [4,5,6], [7,8,9]]

#print(two_dee[0])

for row in two_dee:
    print(f"Term : {row}")
    for col in row:
        print(f"Grade : {col}")



for count, row in enumerate(two_dee, start=1):
    print(f"Term : {count}")
    for col in row:
        print(f"Grade : {col}")