# Level 3 Intro to Python Code School
# If there's less than 3 knights -> Retreat!
# If there's more than 10 knights => Trojan Rabbit!
# Otherwise -> Sign Truce

# Battle Rules #1
num_knights = 2

if num_knights < 3:
    print('Retreat!') # Part of conditional block
    print('Raise the white flag!') # Part of conditional block
print('Knights of the Round Table!') # Not part of conditional

# Battle Rules #2
num_knights = 4

if num_knights < 3:
    print('Retreat!')
else:
    print('Truce?')

# Challenge 3.3 Comparison Operators
# Now that we've learned the comparison operators: <, <=, ==, >=, >, !=, let's give them a try by comparing two numbers in the console, saving the result to a variable, and printing out the result
answer = 10 == 10
print(answer)

# Challenge 3.4 If else
# When planning your trip to the UK, you packed your raincoat and umbrella, but it will help to know some British slang if it does rain.
# Let's write a program to suggest the appropriate rain slang depending on how hard it's raining… you know, to impress the locals.
# If the rain speed is less than 5, print: "Just a Scotch mist". Otherwise, print: "It's a real Cow-quaker out there"
rain_speed = 7

if rain_speed < 5:
    print('Just a Scotch mist')
else:
    print("It's a real Cow-quaker out there")

# Battle Rules #3 (using elif)
num_knights = 10
day = 'Wednesday'

if num_knights < 3:
    print('Retreat!')
elif num_knights >= 10:
    print('Trojan Rabbit')
elif day == 'Tuesday':
    print('Taco Night')
else:
    print('Truce?')

# Using and/or operators
# King Arthur has decided:
# On all Mondays, we retreat
# We can only use the Trojan Rabbit on Wednesday
# New Monday Rule
if num_knights < 3 or day == "Monday":
    print('Retreat!')
# Trojan Rabbit Rule
if num_knights <= 10 and day == "Wednesday":
    print('Trojan Rabbit!')

# Battle Rules #4 (adding rules from above)
num_knights = 10
day = 'Wednesday'

if  num_knights < 3 or day == 'Monday':
    print('Retreat!')
elif num_knights <= 10 and day == 'Wednesday':
    print('Trojan Rabbit!')
else:
    print('Truce?')

# User Input - With the input() Function
# Ask the user to input the day of the week
day = input('Enter the day of the week\n')
print('You entered:', day)

# Ask the user to input the number of knights
# NOTE anything entered into an input will be a string, if an int is needed, be sure to use the int() function to convert the response.
num_knights = int(input('Enter the number of knights'))

print('You entered:', num_knights)
if num_knights < or day == 'Monday':
    print('Retreat!')

# Battle Rules #5
num_knights = int(input('How many knights?'))
day = input('What day is it?')

if num_knights < 3 or day == 'Monday':
    print('Retreat!')
elif num_knights >= 10 and day == 'Wednesday':
    print('Trojan Rabbit!')
else:
    print('Truce?')

# Extended Battle Rules (Nested conditionals)
# If we see a killer bunny, throw Holy Hand Grenade
# Otherwise go to the original rules of engagement
# Battle Rules #6
num_knights = int(input('Enter number of knights'))
day = input('Enter day of the week')
enemy = input('Enter type of enemy')

if enemy == 'killer bunny':
    print('Holy Hand Grenade!')
else:
    # original battle rules
    if num_knights < 3 or day == 'Monday':
        print('Retreat!')
    elif num_knights >= 10 and day == 'Wednesday':
        print('Trojan Rabbit!')
    else:
        print('Truce?')

# Challenge 3.8 - Rock-Paper-Python
# We're going to make our own rock-paper-python game, where paper beats rock, rock beats python, and python beats paper.
computer_choice = 'rock'
user_choice = input("Enter rock, paper, or python:\n")

if computer_choice == user_choice:
    print('TIE')
else:
    print('You lose :( Computer wins :D')

# Challenge 3.9 - Improving Rock-Paper-Python
# Let's improve on the code we just wrote to add some cases where a user can win.
computer_choice = 'rock'
user_choice = input("Enter rock, paper, or python:\n")

if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_choice == 'python':
    print('WIN')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('WIN')
elif user_choice == 'python' and computer_choice == 'paper':
    print('WIN')
else:
    print('You lose :( Computer wins :D')
