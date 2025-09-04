#Debugging code


import random


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = sum([new_item, item])
    b_list.append(new_item)

mutate([1, 2, 3, 4, 5, 6, 7, 8])