#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque

with open('16a_data.txt', 'r') as f:
    input_data = list(map(lambda x: (x[0], [int(y) if y.isdigit(
    )else y for y in x[1:].split('/')]), f.read().rstrip('\n').split(',')))

dancers = deque([chr(ord('a') + i) for i in range(16)])


def pos_swapper(x):
    index_a, index_b = x
    (dancers[index_a], dancers[index_b]) = (dancers[index_b], dancers[index_a])


def value_swapper(x):
    value_a, value_b = x
    index_a, index_b = dancers.index(value_a), dancers.index(value_b)
    dancers[index_a], dancers[index_b] = dancers[index_b], dancers[index_a]


operations = {
    's': lambda x: dancers.rotate(x[0]),
    'x': pos_swapper,
    'p': value_swapper
}

n_repetitions = 1000000000
order_start = ''.join(dancers)
i = 0
while i < n_repetitions:
    i+= 1
    for opcode, rest_of_op in input_data:
        operations[opcode](rest_of_op)
    if not i % 100:
        print('{}%'.format(i * 100 / n_repetitions))
    if order_start == ''.join(dancers):
        print('Cycle detected at {}!'.format(i))
        n_repetitions %= i
        i = 0
print()
print(''.join(dancers))
