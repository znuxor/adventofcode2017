#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pprint import pprint
import numpy as np
import math

with open('22a_data.txt', 'r') as f:
    input_data = f.read().split('\n')[:-1]

input_map = np.array(list(list(a) for a in input_data))
input_map = input_map == '#'
safe_pad = 1000
input_map = np.pad(input_map, safe_pad, 'minimum')

start_position = [math.floor(i/2) for i in input_map.shape]

burst_number = 10000
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
    if input_map[current_pos[0], current_pos[1]]:
        rotate_right()
    else:
        rotate_right()
        rotate_right()
        rotate_right()
        infected_number += 1
    input_map[current_pos[0], current_pos[1]] = not input_map[current_pos[0], current_pos[1]]
    move_one()

print(infected_number)
