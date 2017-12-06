#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

puzzle_input = np.array("0   5   10  0   11  14  13  4   11  8   8   7   1   4   12  11".split('  '), dtype=int)
# puzzle_input = np.array([0, 2, 7, 0], dtype=int)
state_history = []
state_history.append(str(puzzle_input))

step_number = 0
while True:
    step_number += 1
    # Find the max value + index, finds the amount to put per block
    max_value = np.amax(puzzle_input)
    max_index = np.argmax(puzzle_input)
    redistrib_value_all = max_value // puzzle_input.shape[0]
    remain = max_value % puzzle_input.shape[0]
    puzzle_input[max_index] = 0
    puzzle_input += redistrib_value_all
    for i in range(remain):
        max_index = (max_index + 1) % puzzle_input.shape[0]
        puzzle_input[max_index] += 1

    new_state = str(puzzle_input)
    if new_state not in state_history:
        state_history.append(new_state)
    else:
        print(step_number)
        print(step_number-state_history.index(new_state))
        break

