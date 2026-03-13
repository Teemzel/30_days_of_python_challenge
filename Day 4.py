# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
a = 'thirty'
b = 'days'
c = 'of'
d = 'python'
challenge = (a.title() + ' ' + b.title() + ' ' + c.title() + ' ' + d.title())
print(challenge)            # Thirty Days Of Python
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
first = 'Coding'
second = 'For'
third = 'All'
space = ' '
print(first + space + second + space + third)  # Coding For All

# Declare a variable named company and assign it to an initial value "Coding For All"
company = "Coding For All"
# Print the variable company using print().
print(company)                                 # Coding For All
# Print the length of the company string using len() method and print().
print(len(company))         # 14
# Change all the characters to uppercase letters using upper() method.
print(company.upper())                          # CODING FOR ALL
# Change all the characters to lowercase letters using lower() method.
print(company.lower())                          # coding for all
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())                     # Coding for all
print(company.title())                          # Coding For All
print(company.swapcase())                       # cODING fOR aLL
# Cut(slice) out the first word of Coding For All string.
company
result = company[6:]
print(result)
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
substring = 'Coding'
print(company.index(substring))
print('Coding' in 'Python For Coding')
# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))  # Python For All

# Change Python for Everyone to Python for All using the replace method or other methods.
company_2 = 'Python For Everyone'
print(company_2.replace('Everyone' , 'All'))  # Python For All

# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())                      # ['Coding', 'For', 'All']

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
Apps = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(Apps.split(','))   # ['Facebook', ' Google', ' Microsoft', ' Apple', ' IBM', ' Oracle', ' Amazon']
# What is the character at index 0 in the string Coding For All.
print(company.index('Coding'))
# What is the last index of the string Coding For All.
print(company.index('All'))             # 11
# What character is at index 10 in "Coding For All" string.
print(company.index(' A'))

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
p = company_2[0]
print(p)
f = company_2[7]
print(f)
e = company_2[11]
print(e)
acronym = p + f + e
print(acronym)
# Create an acronym or an abbreviation for the name 'Coding For All'.
first[0]
second[0]
third[0]
# Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))           # 0
# Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))           # 7
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
last_occurence = 'Coding For All People'
last_occurence.rfind('l')           # 19

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
word = 'You cannot end a sentence with because because because is a conjunction'
word.index('because')               # 31
word.find('because')                # 31

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
word.rfind('because')               # 47

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
phrase_remove = 'because because because '
word.replace(phrase_remove, '')

# Does ''Coding For All' start with a substring Coding?
company
print(company.startswith('Coding'))         # True
# Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))           # False
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
sentence = '   Coding For All      '
print(sentence.strip())
# Which one of the following variables return True when we use the method isidentifier():
        # 30DaysOfPython
        # thirty_days_of_python
python_30 = '30DaysOfPython'
python_30.isidentifier()                    # False
python_thirty = 'thirty_days_of_python'
python_thirty.isidentifier()                # True

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = ' # '.join(libraries)
print(result)

# Use the new line escape sequence to separate the following sentences.
        # I am enjoying this challenge.
        # I just wonder what is next.
word_1 = 'I am enjoying this challenge.'
word_2 = 'I just wonder what is next.'
print(f'{word_1}\n{word_2}')

# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print('Name\tAge\tCountry\t City')
print('Asabeneh\t250\tFinland\tHelsinki')

# Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
string_format = 'The area of a circle with radius %d is %.2f meters square. '%(radius,area)
print(string_format)
string_format_new = 'The area of a circle with radius {} is {:.2f} meters square.' .format(radius,area)
print(string_format_new)
# Make the following using string formatting methods:
a = 8
b = 6
print('{} + {} = {}'.format(a,b, a + b))
print('{} - {} = {}'.format(a,b, a - b))
print('{} * {} = {}'.format(a,b, a * b))
print('{} / {} = {:.2f}'.format(a,b, a / b))            # 1.33, 2 replace 2 decimal number
print('{} % {} = {}'.format(a,b, a % b))
print('{} // {} = {}'.format(a,b, a // b))
print('{} ** {} = {}'.format(a,b, a ** b))
