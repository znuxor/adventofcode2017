#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

data_input = np.loadtxt('2a_data.txt')

my_sum = 0
for i in range(data_input.shape[1]):
    mod_matrix = np.tile(data_input[:, i].reshape([data_input.shape[0], 1]), [1, data_input.shape[1]-1])
    new_data_matrix = np.delete(data_input, i, axis=1)
    modulated_mat = np.mod(new_data_matrix, mod_matrix)
    evenly_div = np.any(modulated_mat == 0, axis=1)
    first_term = data_input[evenly_div, i]
    second_term = new_data_matrix[np.where(modulated_mat == 0)]
    max_nums = np.maximum(first_term, second_term)
    min_nums = np.minimum(first_term, second_term)
    divs = max_nums//min_nums
    my_sum += np.sum(divs)

print(my_sum)
