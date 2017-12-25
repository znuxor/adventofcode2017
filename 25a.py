#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
from functools import total_ordering
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

pieces = []
with open('25a_data.txt', 'r') as f:
    input_data = f.read()

memory_serial_list = [0]
current_pos = 0
states = {
    'a': [[1, +1, 'b'], [0, -1, 'c']],
    'b': [[1, -1, 'a'], [1, -1, 'd']],
    'c': [[1, +1, 'd'], [0, +1, 'c']],
    'd': [[0, -1, 'b'], [0, +1, 'e']],
    'e': [[1, +1, 'c'], [1, -1, 'f']],
    'f': [[1, -1, 'e'], [1, +1, 'a']]
}

step_limit = 12656374
i = 0
current_state = 'a'
for __ in range(step_limit):
    value_to_print, shift, new_state = states[current_state][memory_serial_list[current_pos]]
    memory_serial_list[current_pos] = value_to_print
    current_pos += shift
    if current_pos < 0:
        current_pos = 0
        memory_serial_list.insert(0, 0)  # we need a value before
    elif current_pos == len(memory_serial_list):
        memory_serial_list.append(0)  # we are at the end
    current_state = new_state

checksum = sum(memory_serial_list)
print(checksum)
