#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from collections import defaultdict

with open('4a_data.txt', 'r') as problem_input:
    data_input = problem_input.read().split('\n')[:-1]

# data_input = [
#         'aa bb cc dd ee',
#         'aa bb cc dd aa',
#         'aa bb cc dd aaa'
#         ]

print('total:', end='')
print(len(data_input))
print()

total_valid = 0

for line in data_input:
    word_dict = defaultdict(lambda: 0)
    for word in line.split(' '):
        word_dict[word]+=1
    if max(word_dict.values())==1:
        total_valid += 1
    print(repr(line))

print(total_valid)
