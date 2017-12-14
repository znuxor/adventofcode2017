#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from array import array
import numpy as np

puzzle_input = 'vbqugkhl'

# puzzle_input = 'flqrgnkx'

round_number = 64
def compute_knot_hash_sum(hash_str):
    the_list = np.array(list(range(256)))
    skip_size = 0
    total_roll = 0
    hash_list = list(ord(x) for x in hash_str)
    hash_list.extend([17, 31, 73, 47, 23])
    for _ in range(round_number):
        for length in hash_list:
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
    # print(sparse_hash)
    dense_hash = array('B')
    for zone_id in range(sparse_hash.shape[0]//16):
        current_xor_value = 0
        for i in range(16):
            current_xor_value = np.bitwise_xor(current_xor_value, sparse_hash[zone_id*16+i])
        # print(current_xor_value)
        dense_hash.append(current_xor_value)
    sum_of_hash = 0
    for item in dense_hash:
        sum_of_hash += bin(item).count('1')
    # print(dense_hash)
    # hex_string = ""
    # for number in dense_hash:
        # hex_string = hex_string + "{:0>2x}".format(number)
    # print(hash_str)
    # print(hex_string)
    # print()
    return sum_of_hash

total_sum = 0
for row in range(128):
    new_string = puzzle_input+'-'+str(row)
    total_sum += compute_knot_hash_sum(new_string)
print(total_sum)
