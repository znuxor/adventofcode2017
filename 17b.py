#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque

puzzle_input = 377
# puzzle_input = 3
my_circular_buffer = deque()

my_circular_buffer.append(0)

for i in range(1, 50000000+1):
    new_pos = puzzle_input % len(my_circular_buffer)
    my_circular_buffer.rotate(-new_pos-1)
    my_circular_buffer.appendleft(i)
my_circular_buffer.rotate(-my_circular_buffer.index(0))
print(my_circular_buffer[1])
