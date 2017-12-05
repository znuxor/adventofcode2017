#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

data_input = np.loadtxt('5a_data.txt', dtype=int)
#data_input = np.array([0, 3, 0, 1, -3])
curr_loc = 0
step_number = -1
try:
    while True:
        step_number += 1
        next_jump = data_input[curr_loc]
        data_input[curr_loc] += 1
        curr_loc += next_jump
except Exception:
    pass
finally:
    print(step_number)
