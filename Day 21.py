# Import Module
import math
from statistics import *
from random import random, randint

# Writ a function which generates a six digit/character random_user_id

import random
import string
def random_user_id():
    character = string.ascii_letters + string.digits
    return ''.join(random.choices(character, k = 6))
print(random_user_id())

# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
import random
import string
def user_id_gen_by_user():
    char_count = int(input('Enter a number of character: '))
    id_count = int(input('Enter a number of IDs to generate: '))
    character = string.ascii_letters + string.digits
    for _ in range(id_count):
        new_id = ''.join(random.choice(character) for _ in range(char_count))
        print(new_id)
user_id_gen_by_user()  
   
   
# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each)
import random
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255) 
    b = random.randint(0, 255)
    return (r,g,b)
rgb_color_gen()

