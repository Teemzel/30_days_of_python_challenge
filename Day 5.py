# Declare an empty list
empty = []
empty
# Declare a list with more than 5 items
items = ['Table','Chair', 'Book', 'Pen', 'Eraser']
items 
# Find the length of your list
print(len(items))                   # 5

# Get the first item, the middle item and the last item of the list
print(items[0])
print(items[2])
print(items[-1])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Teemzel', 20, 5.6, 'Married', 'Lagos']
mixed_data_types

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(it_companies)                     # ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# Print the number of companies in the list
print(len(it_companies))                # 7
# Print the first, middle and last company
print(it_companies[0])                  # Facebook
print(it_companies[3])                  # Apple
print(it_companies[6])                  # Amazon

# Print the list after modifying one of the companies
modify_itcomp = len(it_companies) -2
it_companies[modify_itcomp] = 'Tesla'
print(it_companies)

# Add an IT company to it_companies
it_companies.append('MongoDB')                # ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Tesla', 'Amazon', 'MongoDB']
it_companies


# Insert an IT company in the middle of the companies list
it_companies.insert(3, 'Twittter')         # ['Facebook', 'Google', 'Microsoft', 'Twittter', 'Apple', 'IBM', 'Tesla', 'Amazon', 'MongoDB']
it_companies

# Change one of the it_companies names to uppercase (IBM excluded!)


# Join the it_companies with a string '#;  '
join = '#; '.join(it_companies)             # Facebook#; Google#; Microsoft#; Twittter#; Apple#; IBM#; Tesla#; Amazon#; dobog
print(join)

# Check if a certain company exists in the it_companies list.
print('Apple' in it_companies)              # True

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
it_companies

# Slice out the first 3 companies from the list
company = it_companies[3:]              # ['IBM', 'Google', 'Facebook', 'Dobog', 'Apple', 'Amazon']
company

# Slice out the last 3 companies from the list
company = it_companies[0:6]             # ['Twittter', 'Tesla', 'Microsoft', 'IBM', 'Google', 'Facebook']
company
# Slice out the middle IT company or companies from the list
company_2 = it_companies[0:4]
company_2

# Remove the first IT company from the list
it_companies.pop(0)
it_companies

# Remove the middle IT company or companies from the list
it_companies.remove('Apple')

# Remove the last IT company from the list
it_companies.pop()

# Remove all IT companies from the list
del it_companies

# Destroy the IT companies list

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)                  # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
front_end

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_end.copy()
full_stack
new_stack = ['Python', 'SQL']
index_position = 5
# Insert the new_stack at the specified index using slice assignment
full_stack[index_position:index_position] = new_stack
full_stack

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort()
ages
# Add the min age and the max age again to the list
min(ages)
max(ages)

# Find the median age (one middle item or two middle items divided by two)

    

# Find the average age (sum of all items divided by their number )
sum_age = sum(ages) 
sum_age
n = len(ages)
n
middle_age = sum_age / n
print(f'The average age is: ',{middle_age})

# Find the range of the ages (max minus min)
# Compare the value of (min - average) and (max - average), use abs() method

# Create an empty tuple
tp = tuple()
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
boys = ('dave', 'sam', 'mike')
girls = ('jane', 'kate', 'best')
# Join brothers and sisters tuples and assign it to siblings
siblings = boys + girls
siblings
# How many siblings do you have?
print(len(siblings))
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('fred', 'susan')
family_members = parents + siblings
family_members
# Unpack siblings and parents from family_members
siblings_new = family_members[2:]
siblings_new
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'apple', 'carrot')
vegetables = ('tomato', 'spinach', 'jute')
animal = ('milk', 'cheese', 'pork')
food_stuff_tp = fruits + vegetables + animal
food_stuff_tp
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
food_stuff_lt
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_lt.pop(4)
food_stuff_lt
# Slice out the first three items and the last three items from food_staff_lt list
slice = food_stuff_lt[3:6]
slice
# Delete the food_staff_tp tuple completely
del food_stuff_tp
# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)
