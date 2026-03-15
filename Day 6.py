# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
# Find the length of the set it_companies
print(len(it_companies))
# Add 'Twitter' to it_companies
it_companies.add('Twitter')
it_companies
# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Bamboo', 'Tesla'])
# Remove one of the companies from the set it_companies
it_companies.remove('Bamboo')
# What is the difference between remove and discard
it_companies.discard('Tesla')  # Remove an element from a set if it is a member.Unlike set.remove(), the discard() method does not raise an exception when an element is missing from the set.
# Join A and B
ab = A.union(B)
ab
A.update(B)
A
# Find A intersection B
A.intersection(B)
B.intersection(A)
# Is A subset of B
A.issubset(B)
# Are A and B disjoint sets
A.isdisjoint(B)
B.isdisjoint(A)
# Join A with B and B with A
B.update(A)
B
# What is the symmetric difference between A and B
B.symmetric_difference(A)
A.symmetric_difference(B)
# Delete the sets completely
del A
del B 
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
ages = set(age)     # {19, 22, 24, 25, 26}
ages
print(len(age))     # 8
print(len(ages))    # 5
# Explain the difference between the following data types: string, list, tuple and set
string = 'string' # A  collection of string constants.
list = list       # It is a collection of item in a particular order, list are mutable sequence.
tuple = tuple     # It is a collection of different data types which is ordered & immutable.
set = set         # It is collection of unordered & un-indexed distinct elements.
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

# Create an empty dictionary called dog
dog = {}
# Add name, color, breed, legs, age to the dog dictionary
dog = {'name': 'Jack', 'color':'Brown', 'breed':'braboel', 'legs':'4', 'age':'5'}
print(type(dog))
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name':'Ada', 'last_name':'Angel', 'gender':'Female', 'age':'15',
           'marital_status':'married', 'skills':'Programmer', 'country':'Nigeria', 'city':'Ibadan',
           'address':{'street':'Space Street', 'Postal':'2210'}}
# Get the length of the student dictionary
print(len(student))
# Get the value of skills and check the data type, it should be a list
student.values() = ''
# Modify the skills values by adding one or two skills
student['skills'].append('HTML')
student['post_tittle'] = 'Developer'
student
# Get the dictionary keys as a list
key = student.keys()
key
# Get the dictionary values as a list
value = student.values()
value
# Change the dictionary to a list of tuples using items() method
print(student.items())
# Delete one of the items in the dictionary
print(student.clear())
# Delete one of the dictionaries
del student