 # Day 2
 # Built in Function
print("Hello World!")
str(4)
float(7)
int(6)
input("Enter Your Name")

dir(str)

min(5,8,2,6)
max(5,7,9,1,4)
sum([4,7,1,6,4])

#variable
First_name = "Dejavu"
Last_name = "Sailor"
Cars = "BMW","TESLA"
Age = 20
Country = "Nigeria"
City = "Lagos"
Skill = "Content Creator"
Year = 2026
Is_married = True
Person_info = {
    'first_name' : 'Dejavu',
    'last_name' : 'Sailor',
    'country' : 'Nigeria',
    'city' : 'Lagos'
}

print('First_name:', First_name)
print('Last_name:', Last_name)
print('Cars:', Cars)
print('Age:', Age)
print('Country:', Country)
print('City:', City)
print('Skill:', Skill)
print('Year:', Year)
print('Is_Married:', Is_married)
print('Person_info:', Person_info)
print(First_name, Last_name, Age,Country, City, Is_married)

len(First_name)
len(Last_name)

print(type(First_name))     # str
print(type(Last_name))      #str
print(type(Cars))           #tuple
print(type(Age))            #int
print(type(Country))        #str
print(type(City))           #str
print(type(Skill))          #str
print(type(Year))           #int
print(type(Is_married))     #bool
print(type(Person_info))    #dict

num_one = 5
num_two = 4
total = sum((num_one, num_two))
print(total)

diff = num_one - num_two
print(diff)

division = num_one / num_two
print(division)

product = num_one * num_two
print(product)

remainder = num_one % num_two
print(remainder)

exp = num_one ** 2
print(exp)

floor_diivision = num_one // num_two
print(floor_diivision)

print('total : ', total)
print('diff: ', diff)
print('division: ', division)
print('product: ', product)
print('remainder:', remainder)
print('exponential: ', exp)
print('floor_division: ', floor_diivision)

import math
radius = int(input("Enter the radius of a circle:"))
area_of_circle = math.pi * (radius ** 2)
print(f"The circumference of a circle is : {area_of_circle}")

circum_of_circle = 2 * math.pi * radius
print(f"The circumference of a circle is : {circum_of_circle}")

Firstname = input("what is your first name? ")
print(Firstname)
Lastname = input("what is your last name? ")
print(Lastname)
Country2 = input("which country are you from? ")
print(Country2)
Age2 = input("How old are you? ")
print(Age2)

help(dir)

#Casting

# float to int
num_int = int(4.5)
print(num_int)

# int to float
num_float = float(82)
print(num_float)

# int to str
num_str = str(32)
print(num_str)

# str to list
print(list(First_name))