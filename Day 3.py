# Day 3
# Declare your age as integer variable
Age = 20
print('Age:', Age)
# Declare your height as a float variable
Height = 5.8
print('Height:', Height)
# Declare a variable that store a complex number
Complex = (1 + 1j)
print('Complex: ', Complex)
print(type(Complex))

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area_of_triangle = 0.5 * base * height 
print(f'The area of a triangle is: {area_of_triangle}')

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# Area of a triangle
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
Perimeter_of_a_triangle = (a + b + c)
print(f'The perimeter of a triangle is: {Perimeter_of_a_triangle}')

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
#Area of a rectangle
length = 6
width = 8
area_of_a_rectangle = (length * width)
print(area_of_a_rectangle)
perimeter_of_a_rectangle = 2 * area_of_a_rectangle
print(perimeter_of_a_rectangle)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r = int(input("Enter the radius: "))
pi = 3.14
area_of_a_circle = pi * r * r
print(area_of_a_circle)
circ_of_a_circle = 2 * pi * r
print(circ_of_a_circle)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = int(input("Value: "))
y = (x**2 + 6 * x) + 9
print(y)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') != (len('dragon')))
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('I hope this course is not full of jargon')
# There is no 'on' in both dragon and python
print('jargon' in 'I hope this course is not full of jargon')
# Find the length of the text python and convert the value to float and convert it to string
len('python')
float(len('python'))
str(float(len('python')))
# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input('Enter a value'))
if number % 2 == 0:
    print(f'{number} is an even number')
else:
    print(f'{number} is an odd number')
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
7 // 3 == int(2.7)
# Check if type of '10' is equal to type of 10
type('10') == type(10)

# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input('Enter an hour value '))
rate_per_hour = int(input('Enter rate per hour '))
daily_pay = hours * rate_per_hour
print(f'daily earning is ${daily_pay}')
weekly_pay = daily_pay * 5
print(f'weekly earning is ${weekly_pay}')

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
Years = int(input('Enter numbers of years you have lived'))
Seconds = 60
Minutes = 60
Hours = 24
Seconds_a_day = Seconds * Minutes * Hours * 365
print(Seconds_a_day)
seconds_lived = Years * Seconds_a_day
print(seconds_lived)
