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