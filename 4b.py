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
    anagrams_list = list()
    for word in line.split(' '):
        word_anagram_list = list(word)
        word_anagram_list.sort()
        if word_anagram_list not in anagrams_list:
            anagrams_list.append(word_anagram_list)

    
    if len(anagrams_list) == len(line.split(' ')):
        total_valid += 1

print(total_valid)
