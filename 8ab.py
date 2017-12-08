#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from collections import defaultdict

with open('8a_data.txt', 'r') as problem_input:
    data_input = problem_input.read().split('\n')[:-1]

# data_input = """b inc 5 if a > 1
# a inc 1 if b < 5
# c dec -10 if a >= 1
# c inc -20 if c == 10""".split('\n')

registers_dict = defaultdict(lambda: 0)
max_values_registers_dict = defaultdict(lambda: 0)

comparisons_dict = dict()
comparisons_dict['>'] = lambda x, y: x > y
comparisons_dict['<'] = lambda x, y: x < y
comparisons_dict['>='] = lambda x, y: x >= y
comparisons_dict['<='] = lambda x, y: x <= y
comparisons_dict['=='] = lambda x, y: x == y
comparisons_dict['!='] = lambda x, y: x != y

operations_dict = dict()
operations_dict['inc'] = lambda x, y: x + y
operations_dict['dec'] = lambda x, y: x - y


for instruction in data_input:
    (reg_name, op, operand, _, cond_reg, cond_op, cond_value) = instruction.split(' ')
    operand = int(operand)
    cond_value = int(cond_value)
    if comparisons_dict[cond_op](registers_dict[cond_reg], cond_value):
        registers_dict[reg_name] = operations_dict[op](registers_dict[reg_name], operand)
        max_values_registers_dict[reg_name] = max(max_values_registers_dict[reg_name], registers_dict[reg_name])

print(max(registers_dict.values()))
print(max(max_values_registers_dict.values()))
