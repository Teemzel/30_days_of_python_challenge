# Use map to create a new list by changing each country to uppercase in the countries list
countries = ['Brazil', 'Germany', 'usa', 'Canada', 'Nigeria']
upper_countries = list(map(str.upper, countries))
print(upper_countries)
# Use map to create a new list by changing each number to its square in the numbers list
numbers = [1,2,3,4,5,6]
square_numbers = list(map(lambda x: x**2, numbers))
print(square_numbers)
# Use map to change each name to uppercase in the names list
names = ['Kent', 'Trump', 'Sailor', 'Bernard']
upper_names = list(map(str.upper, names))
print(upper_names)
# Use filter to filter out countries containing 'land'.
countries = ['Brazil', 'Island', 'Finland', 'Germany', 'Swizzerland', 'Canada', 'Thailand']
filter_countries = list(filter(lambda c: 'land' in c.lower(), countries))
print(filter_countries)
# Use filter to filter out countries having exactly six characters.
countries = ['Brazil', 'Island', 'Finland', 'Germany', 'Swizzerland', 'Canada', 'Thailand']
filter_countries = list(filter(lambda c: len(c) == 6, countries))
print(filter_countries)
# Use filter to filter out countries containing six letters and more in the country list.
countries = ['Brazil', 'Island', 'Togo', 'Finland', 'Germany', 'Swizzerland', 'Ghana', 'Canada', 'Thailand']
filter_countries = list(filter(lambda x: len(x) >= 6, countries))
print(filter_countries)
# Use filter to filter out countries starting with an 'E'
countries = ['England', 'Island', 'Finland', 'Swizzerland', 'Germany', 'Ethiopia', 'Egypt', 'Canada', 'Thailand']
filter_countries = list(filter(lambda C:  C.startswith('E'), countries))
print(filter_countries)
