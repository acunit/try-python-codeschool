# Level 2 of Intro To Python (CodeSchool.com)
# First script made to test on terminal

first_name = 'Monty'
last_name = 'Python'
full_name = first_name + ' ' + last_name
print(full_name)

# Describe the sketch comedy group
name = 'Monty Python'
description = 'sketch comedy group'
year = 1969

# Introduce them
sentence = name + ' is a ' + description + ' formed in ' + str(year)
print(sentence)

# OR could just put in a print screen (for python3)
print(name, 'is a', description, 'formed in', year)

# Describe Monty Python's work (dealing with quotes in strings) put double quotes around it
famous_sketch = "Hell's Grannies"
print(famous_sketch)

# Showing how Newline ('\n') works and Tab ('\t')
famous_sketch1 = "\n\tHell's Grannies"
famous_sketch2 = '\n\tThe Dead Parrot'
print('Famous Work:', famous_sketch1, famous_sketch2)

# Challenge 2.3 String Concatenation
# Let's print the greeting G'day mate by concatenating strings and printing them to the screen.
greeting = "G'day" + ' mate'
print(greeting)

# Challenge 2.5 Getting Started With Python strings
# Tell us about one of your favorite comedians or sketch comedy groups! Some ideas? Amy Schumer, Seinfeld, Ellen, Key & Peele, Jake and Amir, The Lonely Island — whatever you want.
name = 'Dave Chappelle'
description = 'Award winning, American stand-up comedian, actor, writer, and producer.'
year = 1989
sentence = name + ' is a(n) ' + description + ' who started in ' + str(year)
print(sentence)

# Challenge 2.6 - String Formatting
# Create variables named movie1 and movie2 for at least two of your favorite movies. Sorry, only ascii characters! (Remember: If there are apostrophes in the movie titles, you can use double quotes on the outside.)
movie1 = 'Gladiator'
movie2 = 'Star Wars'
# Print your favorite movies to the screen in a nicely formatted list. Use commas to separate them in the print() statement. And use newline ( \n) and tab ( \t) to format your output like so:
# My Favorite Movies:
#      A Great Movie
#      Another Good Movie
print('My Favorite Movies:\n\t', movie1, '\n\t', movie2)

# print the length of greeting
greeting = 'HELLO WORLD!'
print( len(greeting) )

# The Man Who Only Says Ends of Words
word1 = 'Good'
end1 = word1[2] + word1[3]
print(end1)

# Using Slices to Access Parts of a String (marker at first index and then marker before last number)
word = 'Python'
word[2:5] # ==> 'tho'
word1 = 'Good'
word1[0:2] # ==> 'Go'
word1[:2] # ==> 'Go'  word1[0:2] will return same thing
word1[2:] # ==> 'od'  word1[2:4] will return same thing

# slice formula: variable[start:end+1]

# Incorporating String Slices into our solution
word1 = 'Good'
# end1 = word1[2] + word1[3] -> Not needed can just do a Slice
end1 = word1[2:4]
print(end1)

# Using String Slice Shortcut
word1 = 'Good'
end1 = word1[2:]

word2 = 'Evening'
end2 = word2[3:]

print(end1, end2)

# The Index at the Halfway Point (Using integer division [feature of Python3] '//' Devides into whole integers and drops the remainder)
word1 = 'Good'
# half1 = len(word1)/2 # half is 4/2 = 2.0
half1 = len(word1)//2 # half is 4//2 = 2.0
end1 = word1[half1:]

word2 = 'Evening'
# half2 = len(word2)/2 # half is 7/2 = 3.5
half2 = len(word2)//2 # half is 7//2 = 3.0
end2 = word2[half2:]

print(end1, end2)

# Challenge 2.9 Pythonese
# Let's create our own version of Pig Latin called Pythonese. We will take off the first letter of the word and add it to the end plus the letter 'y'. For example: Python would become ython-Py
word = 'Python'
first = word[0]
rest = word[1:]
result = rest + '-' + first + 'y'
print(result)
