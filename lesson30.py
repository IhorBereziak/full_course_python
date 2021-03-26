# https://docs.python.org/3/library/
# import os
# import random as r
# import random
# from random import randint, shuffle
# from random import *

# print(os.getcwd())
# print(randint(0, 100))
# l = [1, 2, 3, 4, 5]
# shuffle(l)
# print(l)

import libs

print(__name__)
# print(libs.get_count('hello', 'l'))
# print(libs.get_len('hello'))

f = libs.get_count
print(f('hello', 'o'))
