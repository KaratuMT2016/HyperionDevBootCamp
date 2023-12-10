def count_letters(string):
    # Create an empty dictionary to store the frequency of each letter
    frequency = {}

    # Iterate over each character in the string
    for char in string:
        # If the character is already in the dictionary, increment its count
        if char in frequency:
            frequency[char] += 1
        # Otherwise, add the character to the dictionary with a count of 1
        else:
            frequency[char] = 1

    # Print the frequency of each letter
    for char, count in frequency.items():
        print(f"{char}: {count}")

# Example usage
count_letters(" i am a coding genius")