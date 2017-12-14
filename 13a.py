#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import OrderedDict
from pprint import pprint

with open('13a_data.txt', 'r') as problem_input:
    data_input = problem_input.read().split('\n')
    del(data_input[-1])

# data_input = """0: 3
# 1: 2
# 4: 4
# 6: 4""".split('\n')

# obviously we do not need to simulate the whole thing
# we only need to know at which instants a given scanner is going to detect us
# this is happens each 2N-2 steps, where N is the scanner range

severity = 0

for line in data_input:
    depth, range_ = line.split(': ')
    depth = int(depth)
    range_ = int(range_)
    if not depth % (2*(range_-1)):
        severity += depth*range_

print(severity)
