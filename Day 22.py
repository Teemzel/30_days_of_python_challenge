# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import random
import string
def list_of_hexa_colors(num_colors):
    hexa_color = []
    character = '0123456789abcdef'
    for _ in range(num_colors):
        color = '#' + ''.join(random.choice(character) for _ in range(6))
        hexa_color.append(color)
    return hexa_color
print(list_of_hexa_colors(5))