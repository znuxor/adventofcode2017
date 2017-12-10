#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from collections import defaultdict

with open('10a_data.txt', 'r') as problem_input:
    data_input = problem_input.read().split(',')
the_list = np.array(list(range(256)))

# data_input = "3, 4, 1, 5".split(' ')
# the_list = np.array(list(range(5)))

current_position = 0
skip_size = 0
total_roll = 0
for length in data_input:
    integer_length = int(length.rstrip(','))
    if integer_length > len(the_list):
        print('invalid')
        break
    the_list[:integer_length] = np.flip(the_list[:integer_length], axis=0)
    roll_amount = -(integer_length+skip_size)
    total_roll += roll_amount
    the_list = np.roll(the_list, roll_amount)
    skip_size += 1

the_list = np.roll(the_list, -total_roll)
print(the_list)
print(the_list[0] * the_list[1])
