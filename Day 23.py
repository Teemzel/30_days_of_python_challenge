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
                 random.randint(0, 255) )]
color = rgb_color_gen(3)
print(color)
# Write a function generate_colors which can generate any number of hexa or rgb colors.