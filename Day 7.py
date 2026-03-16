# Day 7
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
user = int(input('Enter your age: '))
age = 18
new_age = age - user
if user >= age:
   print('You are old enough to drive.')
elif   user < age:
  print(f'Not old enough to drive, wait for: {new_age} years more to drive')
else:
    print('Not meant to drive') 

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age = int(input('Enter my age: '))
your_age = int(input('Enter your age: '))
age_difference = abs(my_age - your_age)
# def year_diff(my_age, your_age):
if my_age > your_age and age_difference == 1:
    print(f'I am {age_difference} year older than you')
elif my_age > your_age and age_difference > 1:
    print(f'I am {age_difference} years older than you')
elif your_age > my_age and age_difference == 1:
    print(f'You are {age_difference} year older than me')
elif your_age > my_age and age_difference > 1:
    print(f'You are {age_difference} years older than me')
else:
    print('We are age mate')
    
# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b,
#  if a is less b return a is smaller than b, else a is equal to b. Output:
a = int(input('Enter number one: '))
b = int(input('Enter number two: '))
if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} is equal to {b}')

# Write a code which gives grade to students according to theirs scores:
# 80-100 A, 70-79 B, 60-69 C, 50-59 D, 0-49 F
student_score = int(input("Please enter the student's score (0-100): "))
if 0 <= student_score <= 100:
    if student_score >= 80:
        grade = 'A'
    elif student_score >= 70:
        grade = 'B'
    elif student_score >= 60:
        grade = 'C'
    elif student_score >= 50:
        grade = 'D'
    else:
        grade = 'F'
    print(f"The student's grade is: {grade}")
else:
    print('Invalid marks')

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. 
# December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
Autumn = ['September', 'October', 'November']
Winter = ['December', 'January', 'February']
Spring = ['March', 'April', 'May']
Summer = ['June', 'July', 'August']
month = str(input('Enter a month: '))
if month in Autumn:
    print('The month is Autumn Season')
elif month in Winter:
    print('The month is Winter Season')
elif month in Spring:
    print('The month is Spring Season')
else: 
    print('The month is Summer Season')


# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = str(input('Name of a fruit: '))
if new_fruit in fruits:
    print(f'{new_fruit} already exists in the list')
else: 
    fruits.append(new_fruit)
    print(fruits)

