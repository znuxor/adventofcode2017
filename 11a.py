#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from collections import Counter

def compute_hex_distance(hex_cnt):
    # start by removing duplicate distances
    min_n_s = min(hex_cnt['n'], hex_cnt['s'])
    min_ne_sw = min(hex_cnt['ne'], hex_cnt['sw'])
    min_nw_se = min(hex_cnt['nw'], hex_cnt['se'])
    hex_cnt['n'] -= min_n_s
    hex_cnt['s'] -= min_n_s
    hex_cnt['ne'] -= min_ne_sw
    hex_cnt['sw'] -= min_ne_sw
    hex_cnt['nw'] -= min_nw_se
    hex_cnt['se'] -= min_nw_se
    print(hex_cnt)
    # now remove kinked pairs
    # those are values that are located between two values and can be merged together as one move
    kink_1 = min(hex_cnt['n'], hex_cnt['se'])
    kink_2 = min(hex_cnt['ne'], hex_cnt['s'])
    kink_3 = min(hex_cnt['se'], hex_cnt['sw'])
    kink_4 = min(hex_cnt['s'], hex_cnt['nw'])
    kink_5 = min(hex_cnt['sw'], hex_cnt['n'])
    kink_6 = min(hex_cnt['nw'], hex_cnt['ne'])

    hex_cnt['n'] -= kink_1
    hex_cnt['se'] -= kink_1
    hex_cnt['ne'] += kink_1

    hex_cnt['ne'] -= kink_2
    hex_cnt['s'] -= kink_2
    hex_cnt['se'] += kink_2

    hex_cnt['se'] -= kink_3
    hex_cnt['sw'] -= kink_3
    hex_cnt['s'] += kink_3

    hex_cnt['s'] -= kink_4
    hex_cnt['nw'] -= kink_4
    hex_cnt['sw'] += kink_4

    hex_cnt['sw'] -= kink_5
    hex_cnt['n'] -= kink_5
    hex_cnt['nw'] += kink_5

    hex_cnt['nw'] -= kink_6
    hex_cnt['ne'] -= kink_6
    hex_cnt['n'] += kink_6
    print(hex_cnt)
    distance = sum(hex_cnt[a_key] for a_key in hex_cnt.keys())
    return distance

with open('11a_data.txt', 'r') as problem_input:
    data_input = problem_input.read().split(',')
    data_input[-1] = data_input[-1].rstrip('\n')

# data_input = ['ne', 'ne', 'ne']
# data_input = ['ne', 'ne', 'sw', 'sw']
# data_input = ['ne', 'ne', 's', 's']
# data_input = ['se', 'sw', 'se', 'sw', 'sw']

each_direction_counter = Counter()

each_direction_counter.update(data_input)
print(each_direction_counter)


distance = compute_hex_distance(each_direction_counter)
print(distance)
