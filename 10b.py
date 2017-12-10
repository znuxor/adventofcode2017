#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from collections import defaultdict

with open('10a_data.txt', 'r') as problem_input:
    data_input_text = list(problem_input.read())[:-1]
    # data_input_text = ""
    # data_input_text = "AoC 2017"
    # data_input_text = "1,2,3"
    # data_input_text = "1,2,4"
    data_input = []
    for item in data_input_text:
        data_input.append(ord(item))
    data_input.extend([17, 31, 73, 47, 23])
    print(data_input)

round_number = 64

the_list = np.array(list(range(256)))

# data_input = "3, 4, 1, 5".split(' ')
# the_list = np.array(list(range(5)))

skip_size = 0
total_roll = 0
for _ in range(round_number):
    for length in data_input:
        integer_length = length
        if integer_length > len(the_list):
            print('invalid')
            break
        the_list[:integer_length] = np.flip(the_list[:integer_length], axis=0)
        roll_amount = -(integer_length+skip_size)
        total_roll += roll_amount
        the_list = np.roll(the_list, roll_amount)
        skip_size += 1

# This is the sparse hash
sparse_hash = np.roll(the_list, -total_roll)
print(sparse_hash)

dense_hash = []
#sparse_hash = np.array([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22])
for zone_id in range(sparse_hash.shape[0]//16):
    current_xor_value = 0
    for i in range(16):
        current_xor_value = np.bitwise_xor(current_xor_value, sparse_hash[zone_id*16+i])
    dense_hash.append(current_xor_value)

#dense_hash = [64, 7, 255]
print(dense_hash)

hex_string = ""
for number in dense_hash:
    hex_string = hex_string + "{:0>2x}".format(number)
print(hex_string)
print(len(hex_string))
