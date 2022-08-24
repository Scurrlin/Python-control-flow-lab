# NOTES AND PERSONAL OBSERVATIONS AT THE BOTTOM OF THIS PAGE!

# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

def vowel_const():
    ch = input('Please enter a letter from the alphabet (a-z or A-Z): ')
    vowel = ['a', 'e', 'i', 'o', 'u']
    if ch.lower() in vowel:
        print(f'The letter {ch} is a vowel')
    else:
        print(f'The letter {ch} is a consonant')

vowel_const()

# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

def len_phrase():
    while True:
        str = input('Please enter a word or phrase: ')
        if str != 'quit':
            print(f'What you entered is {len(str)} characters long.')
            print('Enter "quit" to stop the program.')
        else:
            break

len_phrase()

# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

def age():
    try:
        age = int(input(f"Input a dog's age in human years:"))
    if age < 3:
        age *= 10
    else:
        age = 20 + (age - 2) * 7
    print(f"The dog's age in dog years is {age}")

# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

def which_triangle():
    i = 1
    sides = []
    while i < 4:
        answer = int(input(f'Enter the lengths of the number {i} side of a triangle: '))
        sides.append(answer)
        i += 1
    if (sides[0] + sides[1]) >= sides[2] and (sides[0] + sides[2]) >= sides[1] and (sides[1] + sides[2]) >= sides[0]:
        triangle_type(sides)
    else:
        print(f'{sides[0]}, {sides[1]} & {sides[2]} do not make a triangle.')

def triangle_type(arr):
    if len(set(arr)) == 1:
        print(f'A triangle with sides of {arr[0]}, {arr[1]} & {arr[2]} is a equalateral triangle')
    elif len(set(arr)) == 2:
        print(f'A triangle with sides of {arr[0]}, {arr[1]} & {arr[2]} is a isosceles triangle')
    elif len(set(arr)) == 3:
        print(f'A triangle with sides of {arr[0]}, {arr[1]} & {arr[2]} is a scalene triangle')

which_triangle()

# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

def fibonacci(num):
    i = 0
    total = 0
    fib1 = 0
    fib2 = 1

    while i <= num:
        print(f'term:{i} / number: {total}')
        fib1 = fib2
        fib2 = total
        total = fib1 + fib2
        i += 1 

fibonacci(50)
  
# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

mo = input('Enter the month of the season (Jan - Dec): ')
day = int(input('Enter the day of the month: '))

    if mo in ('Jan', 'Feb', 'Mar'):
        season = 'Winter'
    elif mo in ('Apr', 'May', 'Jun'):
        season = 'Spring'
    elif mo in ('Jul', 'Aug', 'Sep'):
        season = 'Summer'
    else:
        season = 'Fall'

    if mo == 'Mar' and day > 19:
        season = 'Spring'
    elif mo == 'Jun' and day > 20:
        season = 'Summer'
    elif mo == 'Sep' and day > 21:
        season = 'Fall'
    elif mo == 'Dec' and day > 20:
        season = 'Winter'

print(f'{mo} {day} is in {season}')

# Notes and Personal Observations:

# I worked on this lab with Andrew for most of it, but wanted to try the last question on my own.
# I am noticing some similar issues I had with my early exposure to Javascript, but do feel as though
# I'm better prepared to try and generate solutions. This last exercise cemented for me that I still
# feel like I have some gaps in my knowledge of the "order of operations" if you will with regards
# to logically structuring code. Current plan to rectify this is to spend some time going over
# some of the previous material at the micro level to better identify what specific aspects of my knowledge
# foundation are shaky. To be clear, I do feel as though I have improved considerably since the start of
# the program, but I need to put more time in on my own to fill in the aforementioned knowledge gaps.