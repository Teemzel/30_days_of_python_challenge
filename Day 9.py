# Day 9
# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lis = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in lis:
    print(i)

# Use for loop to iterate from 0 to 100 and print only even numbers
even = list(range(0, 101, 2))
for i in even:
    print(i)

# Use for loop to iterate from 0 to 100 and print only odd numbers
odd = list(range(1, 101, 2))
for i in odd:
    print(i)

# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
summ = list(range(0, 101))
for i in summ:
    print(sum(summ))

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_even = list(range(0, 101, 2))
for i in sum_even:
    print(sum(sum_even))

sum_odd = list(range(0, 101, 2))
for i in sum_odd:
    print(sum(sum_odd))

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruita = ['banana', 'orange', 'mango', 'lemon']
fruita[::-1]
