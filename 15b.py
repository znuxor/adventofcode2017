#!/usr/bin/env python3
# -*- coding: utf-8 -*-

input_a = 289
input_b = 629

# input_a = 65
# input_b = 8921

multiplicator_a = 16807
multiplicator_b = 48271

divisor_ab = 2**31-1
divisor_bit_mask = 2**31-1
divisor_bit_mask_2 = 2**31

stepNumber = 5000000

current_value_a = input_a
current_value_b = input_b
same_bits_counter = 0

for _ in range(stepNumber):
    current_value_a *= multiplicator_a
    current_value_a %= divisor_ab
    while (current_value_a & 0b11):
        current_value_a *= multiplicator_a
        current_value_a %= divisor_ab
    current_value_b *= multiplicator_b
    current_value_b %= divisor_ab
    while (current_value_b & 0b111):
        current_value_b *= multiplicator_b
        current_value_b %= divisor_ab
    # print("{:0>32b}\n{:0>32b}\n".format(current_value_a & 2**32-1, current_value_b & 2**32-1))
    same_bits_counter += (current_value_a & 2**16-1) == (current_value_b & 2**16-1)

print(same_bits_counter)
