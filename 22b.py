#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pprint import pprint
import numpy as np
import math
from collections import defaultdict

with open('22a_data.txt', 'r') as f:
    input_data = f.read().split('\n')[:-1]

fun_true = lambda x: 1 if x == '#' else 0
data_to_input = list(list(a) for a in input_data)
data_to_input = list(list(map(fun_true, a_list)) for a_list in data_to_input)
M = math.floor(len(input_data)/2)
data_size = range(len(data_to_input))
false_fun = lambda: 0
input_map = defaultdict(false_fun)
for i in data_size:
    for j in data_size:
        input_map[(i, j)] = data_to_input[i][j] * 2
start_position = [M, M]


burst_number = 10000000
current_dir = 'U'
current_pos = start_position


def rotate_right():
    global current_dir
    if current_dir == 'U':
        current_dir = 'R'
    elif current_dir == 'R':
        current_dir = 'D'
    elif current_dir == 'D':
        current_dir = 'L'
    elif current_dir == 'L':
        current_dir = 'U'
    else:
        print('ouch')


def move_one():
    if current_dir == 'U':
        current_pos[0] -= 1
    elif current_dir == 'R':
        current_pos[1] += 1
    elif current_dir == 'D':
        current_pos[0] += 1
    elif current_dir == 'L':
        current_pos[1] -= 1
    else:
        print('ouch')

infected_number = 0
for i in range(burst_number):
    if not input_map[tuple(current_pos)]:  # free
        rotate_right()
        rotate_right()
        rotate_right()
    elif input_map[tuple(current_pos)] == 1:  # weakened
        # do nothing here
        infected_number += 1
    elif input_map[tuple(current_pos)] == 2:  # infected
        rotate_right()
    else:  # flagged
        rotate_right()
        rotate_right()
    input_map[tuple(current_pos)] = (input_map[tuple(current_pos)] + 1) % 4
    move_one()
    if (i % 100000 == 0):
        print(i)

print(infected_number)
