# Day 3
Age = 20
print('Age:', Age)
Height = 5.8
print('Height:', Height)
Complex = (1 + 1j)
print('Complex: ', Complex)
print(type(Complex))

base = float(input("Enter base: "))
height = float(input("Enter height: "))
area_of_triangle = 0.5 * base * height 
print(f'The area of a triangle is: {area_of_triangle}')


# Area of a triangle
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
Perimeter_of_a_triangle = (a + b + c)
print(f'The perimeter of a triangle is: {Perimeter_of_a_triangle}')

#Area of a rectangle
length = 6
width = 8
area_of_a_rectangle = (length * width)
print(area_of_a_rectangle)

perimeter_of_a_rectangle = 2 * area_of_a_rectangle
print(perimeter_of_a_rectangle)

r = int(input("Enter the radius: "))
pi = 3.14
area_of_a_circle = pi * r * r
print(area_of_a_circle)

circ_of_a_circle = 2 * pi * r
print(circ_of_a_circle)

x = int(input("Value: "))
y = (x**2 + 6 * x) + 9
print(y)

print(len('python') != (len('dragon')))
print('on' in 'python' and 'on' in 'dragon')
print('I hope this course is not full of jargon')
print('jargon' in 'I hope this course is not full of jargon')

len('python')
float(len('python'))
str(float(len('python')))

number = int(input('Enter a value'))
if number % 2 == 0:
    print(f'{number} is an even number')
else:
    print(f'{number} is an odd number')

7 // 3 == int(2.7)

type('10') == type(10)

hours = int(input('Enter an hour value '))
rate_per_hour = int(input('Enter rate per hour '))
daily_pay = hours * rate_per_hour
print(f'daily earning is ${daily_pay}')
weekly_pay = daily_pay * 5
print(f'weekly earning is ${weekly_pay}')

Years = int(input('Enter numbers of years you have lived'))
Seconds = 60
Minutes = 60
Hours = 24
Seconds_a_day = Seconds * Minutes * Hours * 365
print(Seconds_a_day)
seconds_lived = Years * Seconds_a_day
print(seconds_lived)