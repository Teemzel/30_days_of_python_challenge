# Week 8
person ={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'}
    }
# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
for key in person:
    if key == value:
     if 'skills' == 'Python':
        for skill in person['skills']:
            print(skill)
# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
# If the person is married and if he lives in Finland, print the information in the following format:
# Iterate 0 to 10 using for loop, do the same using while loop.
for number in range(11):
    print(number)

count = (0)
while count < 11:
    print(count)
    count = count + 1

# Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10, -1, -1):
    print(i)
   
count = (10)
while count >= 0:
    print(count)
    count -=  1   

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(1, 8):
    print("#" * i)


for i in range(11):
    print(f"{i} x {i} = {i*i}",
           end=" ")