"""
A str in Python is an immutable sequence of Unicode code points. These could include letters, diacritical marks, positioning characters, 
numbers, currency symbols, emoji, punctuation, space and line break characters, and more. Being immutable, a str object's value in memory 
doesn't change; methods that appear to modify a string return a new copy or instance of that str object.

A str literal can be declared via single ' or double " quotes. The escape \ character is available as needed.
"""


single_quoted = 'These allow "double quoting" without "escape" characters.'

double_quoted = "These allow embedded 'single quoting', so you don't have to use an 'escape' character"

escapes = 'If needed, a \'slash\' can be used as an escape character within a string when switching quote styles won\'t work.'

print(single_quoted)
print(double_quoted)
print(escapes)


"""
Strings can be concatenated using the + operator. This method should be used sparingly, as it is not very performant or easily maintained.
"""

language = "Ukrainian"
number = "nine"
word = "дев'ять"

sentence = word + " " + "means" + " " + number + " in " + language + "."

print(sentence)


"""
If a list, tuple, set or other collection of individual strings needs to be combined into a single str, <str>.join(<iterable>), is a better option:
"""

# str.join() makes a new string from the iterables elements.
chickens = ["hen", "egg", "rooster"]
print(' '.join(chickens))


# Any string can be used as the joining element.

print(' :: '.join(chickens))

print(' 🌿 '.join(chickens))


"""
Code points within a str can be referenced by 0-based index number from the left:
"""

creative = '창의적인'

print(creative[0])

print(creative[2])

print(creative[3])

print()

for index in range(len(creative)):
    print(creative[index])

print()
print(creative[-4])

print(creative[-2])

print(creative[-1])

print()

# Print each character of the string using a for loop with -1-based index
for index in range(-1, -len(creative)-1, -1):
    print(creative[index])

"""
There is no separate “character” or "rune" type in Python, so indexing a string produces a new str of length 1:
"""

website = "exercism"
website_type = type(website[0])

website_length = len(website[0])

print(website[0] == website[0:1] == 'e')
print(website_type)
print(website_length)


"""
Substrings can be selected via slice notation, using <str>[<start>:stop:<step>] to produce a new string. 
Results exclude the stop index. If no start is given, the starting index will be 0. If no stop is given, 
he stop index will be the end of the string.
"""

moon_and_stars = '🌟🌟🌙🌟🌟⭐'
sun_and_moon = '🌞🌙🌞🌙🌞🌙🌞🌙🌞'

print("Print index 1, 2, and 3: ", moon_and_stars[1:4])


print("Print from index 0 to 3 - 1: ", moon_and_stars[:3])


print("Print from and including index 3 to the end of the list: ", moon_and_stars[3:])


print("Print the list in reverse order, not including the item at index -1: ", moon_and_stars[:-1])


print("Print the items from index -4 to -6 excluding -3: ", moon_and_stars[:-3])


print("Print the items in the list starting from index 0  and stop at index (n -1) by default, skipping 2 step at a time: ", sun_and_moon[::2])


print("Print the items in the list starting from index 0  and stop at index -2, skipping 2 step at a time: ",sun_and_moon[:-2:2])


print("Print the items in the list starting from index 1  and stop at index (n-1), skipping 2 step at a time: ", sun_and_moon[1:-1:2])

"""
Strings can also be broken into smaller strings via <str>.split(<separator>), 
which will return a list of substrings. The list can then be further indexed 
or split, if needed. Using <str>.split() without any arguments will split the 
string on whitespace.
"""

cat_ipsum = "Destroy house in 5 seconds mock the hooman."

#Split the string into a list seprated by whitespace
print(cat_ipsum.split())

print(cat_ipsum.split()[-1])

#Split the string into a list seprated by comma
cat_words = "feline, four-footed, ferocious, furry"
print(cat_words.split(', '))


"""
Separators for <str>.split() can be more than one character. The whole string is used for split matching.
"""

colors = """red,
orange,
green,
purple,
yellow"""

# The escape sequence \n will remove the back slash from the colors strings
# The output will appear this way without the escape sequence - ['red', '\norange', '\ngreen', '\npurple', '\nyellow']
print(colors.split(',\n'))


"""
Strings support all common sequence operations. Individual code points can be iterated through in a loop via for item in <str>. 
Indexes with items can be iterated through in a loop via for index, item in enumerate(<str>).
"""

exercise = 'လေ့ကျင့်'

# Note that there are more code points than perceived glyphs or characters
for code_point in exercise:
    print(code_point)
print()
# Using enumerate will give both the value and index position of each element.
for index, code_point in enumerate(exercise):
    print(index, ": ", code_point)



"""
Instructions
You are helping your younger sister with her English vocabulary homework, which she is finding very tedious. Her class is learning to 
create new words by adding prefixes and suffixes. Given a set of words, the teacher is looking for correctly transformed words with 
correct spelling by adding the prefix to the beginning or the suffix to the ending.

There's four activities in the assignment, each with a set of text or words to work with.
"""

"""
1. Add a prefix to a word
One of the most common prefixes in English is un, meaning "not". In this activity, your sister needs to make negative, or "not" words by adding un to them.

Implement the add_prefix_un(<word>) function that takes word as a parameter and returns a new un prefixed word:
"""

def add_prefix_un(word):
    return "un" + word

# Implementing the function with "happy"
print(add_prefix_un("happy"))

# Implementing the function with "manageable"
print(add_prefix_un("manageable"))


"""
2. Add prefixes to word groups
There are four more common prefixes that your sister's class is studying: en (meaning to 'put into' or 'cover with'), pre (meaning 'before' or 'forward'), 
auto (meaning 'self' or 'same'), and inter (meaning 'between' or 'among').

In this exercise, the class is creating groups of vocabulary words using these prefixes, so they can be studied together. 
Each prefix comes in a list with common words it's used with. The students need to apply the prefix and produce a string that shows the prefix applied to all of the words.

Implement the make_word_groups(<vocab_words>) function that takes a vocab_words as a parameter in the following form: [<prefix>, <word_1>, <word_2> .... <word_n>], 
and returns a string with the prefix applied to each word that looks like: '<prefix> :: <prefix><word_1> :: <prefix><word_2> :: <prefix><word_n>'.
"""

def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = vocab_words[1:]
    prefixed_words = [prefix + word for word in words]
    return " :: ".join([prefix] + prefixed_words)

# Implementing the function
vocab_words_1 = ['en', 'close', 'joy', 'ligten', 'large']
print(make_word_groups(vocab_words_1)) 

vocab_words_2 = ['pre', 'order', 'heat', 'view', 'serve', 'dispose', 'position']
print(make_word_groups(vocab_words_2))  

vocab_words_3 = ['auto', 'didactic', 'mate', 'matic', 'graph', 'dial']
print(make_word_groups(vocab_words_3))  

vocab_words_4 = ['inter', 'twine', 'connected', 'dependent', 'act', 'national', 'fere']
print(make_word_groups(vocab_words_4))  

"""
3. Remove a suffix from a word
ness is a common suffix that means 'state of being'. In this activity, your sister needs to find the original root word by removing the ness suffix. 
But of course there are pesky spelling rules: If the root word originally ended in a consonant followed by a 'y', then the 'y' was changed to 'i'. 
Removing 'ness' needs to restore the 'y' in those root words. e.g. happiness --> happi --> happy.

Implement the remove_suffix_ness(<word>) function that takes in a word, and returns the root word without the ness suffix.
"""

def remove_suffix_ness(word):
    if word.endswith("ness"):
        root_word = word[:-4]  # Remove the "ness" suffix
        if root_word.endswith("i"):
            root_word += "y"  # Restore the 'y' if the original word ended in 'y'
        return root_word
    else:
        return word  # Return the word unchanged if it doesn't end with "ness"

# Implementing the function
print(remove_suffix_ness("happiness"))  
print(remove_suffix_ness("kindness"))   
print(remove_suffix_ness("sadness"))    
print(remove_suffix_ness("loneliness")) 


"""
4. Extract and transform a word
Suffixes are often used to change the part of speech a word is assigned to. A common practice in English is "verbing" or "verbifying" -- where an adjective becomes a verb by adding an en suffix.

In this task, your sister is going to practice "verbing" words by extracting an adjective from a sentence and turning it into a verb. Fortunately, all the words that need to be transformed here 
are "regular" - they don't need spelling changes to add the suffix.

Implement the adjective_to_verb(<sentence>, <index>) function that takes two parameters. A sentence using the vocabulary word, and the index of the word, once that sentence is split apart. 
The function should return the extracted adjective as a verb.
"""

def adjective_to_verb(sentence, suffix_position):
    words = sentence.split()
    if suffix_position < 0:
        # Find the adjective
        for i in range(len(words)):
            if words[i].endswith('.'):
                adj = words[i - 1]
                break
    else:
        adj = words[suffix_position - 1]
        
    # Remove any punctuation from the adjective
    adj = adj.strip('.').strip(',')
    
    # Create the verb by adding 'en' to the adjective
    verb = adj + 'en'
    
    return verb

# Implementing the function
print(adjective_to_verb('I need to make that bright.', -1))  
print(adjective_to_verb('It got dark as the sun set.', 2))   


