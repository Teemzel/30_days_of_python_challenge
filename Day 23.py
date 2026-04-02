# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
import random
def rgb_color_gen(n):
    color_gen = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255) 
        b = random.randint(0, 255)
        color_gen.append((r,g,b))
    return color_gen
print(rgb_color_gen(5))


import random
def rgb_color_gen(n):
    return [( random.randint(0, 255),
                 random.randint(0, 255), 
                 random.randint(0, 255) )
                 for _ in range(n)]
print(rgb_color_gen(3))
# Write a function generate_colors which can generate any number of hexa or rgb colors.
import random
import string
def generate_colors(n, mode = 'hex'):
    hexa_color = []
    for _ in range(n):
        r,g,b = [random.randint(0, 255) for _ in range(3)]
        if mode == 'rgb':
            hexa_color.append((r,g,b))
        else:
            hexa_color.append(f'#{r:02x}{g:02x}{b:02x}')
    return hexa_color
print(generate_colors(3, 'rgb'))
print(generate_colors(5, 'hex'))

# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
import random
def shuffle_list(n):
    number = n[:]
    random.shuffle(number)
    return number
item = [3, 6, 1, 2]
list_item = ['book', 'bags', 'shoes', 'clothes', 'jeans']
shuffle_item = shuffle_list(item)
shuffle_item2 = shuffle_list(list_item)
print(shuffle_item)
print(shuffle_item2)
# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
import random
def array_numbers():
    return random.sample(range(10),7)
print(array_numbers())
        
