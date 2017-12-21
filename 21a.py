#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
import numpy as np

with open('21a_data.txt', 'r') as f:
    input_data = f.read().split('\n')[:-1]

translation_dictionary = dict()
for line in input_data:
    old_pattern, new_pattern = line.rstrip(' ').split(' => ')
    old_pattern = old_pattern.split('/')
    old_pattern = list([*(old_pattern[i])] for i in range(len(old_pattern)))
    old_pattern = np.array(old_pattern)
    new_pattern = new_pattern.split('/')
    new_pattern = list([*(new_pattern[i])] for i in range(len(new_pattern)))
    new_pattern = np.array(new_pattern)
    old_pattern = old_pattern == '#'
    new_pattern = new_pattern == '#'
    for i in range(4):
        old_pattern = np.rot90(old_pattern, k=1)
        old_pattern_key = tuple(map(tuple, old_pattern))
        if old_pattern_key not in translation_dictionary:
            translation_dictionary[old_pattern_key] = new_pattern
        else:
            pass
        old_pattern2 = np.flipud(old_pattern)
        old_pattern_key2 = tuple(map(tuple, old_pattern2))
        if old_pattern_key2 not in translation_dictionary:
            translation_dictionary[old_pattern_key2] = new_pattern
        else:
            pass


start_pattern = np.array([['.','#','.'], ['.','.','#'], ['#','#','#']])
start_pattern = start_pattern == '#'
print(start_pattern)

IT_NUMBER_A = 5
IT_NUMBER_B = 18
#for i in range(IT_NUMBER_A):
for i in range(IT_NUMBER_B):
    size_side = start_pattern.shape[0]
    if not size_side % 2:
        new_size_side = size_side * 3 //2
        new_matrix = np.zeros([new_size_side, new_size_side], dtype='bool')
        for x in range(size_side//2):
            for y in range(size_side//2):
                tuple_square = tuple(map(tuple, start_pattern[2*x:2*x+2, 2*y:2*y+2]))
                new_matrix[3*x:3*x+3, 3*y:3*y+3] = translation_dictionary[tuple_square]
                # print(new_matrix)
                # print()
    else:
        new_size_side = size_side * 4 //3
        new_matrix = np.zeros([new_size_side, new_size_side], dtype='bool')
        for x in range(size_side//3):
            for y in range(size_side//3):
                tuple_square = tuple(map(tuple, start_pattern[3*x:3*x+3, 3*y:3*y+3]))
                new_matrix[4*x:4*x+4, 4*y:4*y+4] = translation_dictionary[tuple_square]
                # print(new_matrix)
                # print()
        pass
    start_pattern = new_matrix
    total = np.sum(start_pattern)

total = np.sum(start_pattern)
print(start_pattern.shape)
print(total)
