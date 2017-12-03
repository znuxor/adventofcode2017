#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import numpy as np

puzzle_input = 325489

# quick and dirty method through computation of each ring in a matrix that's large enough
mat_size = 13
mat = np.zeros([mat_size, mat_size], dtype=int)

cur_x = (mat_size - 1) // 2
cur_y = (mat_size - 1) // 2
mat[cur_y, cur_x] = 1
quarter_size = 0
cur_x += 1
cur_y += 1
try:
    while True:
        quarter_size += 2
        for i in range(4):
            for j in range(quarter_size):
                cur_x += (i % 2) * ((i > 1) * 2 - 1)
                cur_y += (1 - i % 2) * ((i > 1) * 2 - 1)
                new_value = np.sum(
                    mat[cur_y - 1:cur_y + 2, cur_x - 1:cur_x + 2])
                mat[cur_y, cur_x] = new_value
                if new_value > puzzle_input:
                    print(new_value)
                    raise IndexError  # yeah yeah this is really bad to make an exit
        cur_x += 1
        cur_y += 1
except IndexError:
    print('done')
