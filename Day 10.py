# Day 10
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    total = num1 + num2 
    return total
print(add_two_numbers(num1 = 2,num2 = 3))
# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_a_circle(r):
    pi = 3.14
    area = pi * r * r
    return area
print(area_of_a_circle(12))

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
        return total
print(add_all_nums(3,4,5))
