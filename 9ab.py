#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from collections import defaultdict

with open('9a_data.txt', 'r') as problem_input:
    data_input = problem_input.read()

#data_input = "{{<!!>},{<!!>},{<!!>},{<!!>}}"


total_score = 0
local_score = 0
exclamation_ignore = False
in_garbage_zone = False
garbage_characters = 0

# basically a state machine
for character in data_input:
    if exclamation_ignore:
        exclamation_ignore = False
    elif in_garbage_zone:
        if character == '!':
            exclamation_ignore = True
        elif character == '>':
            in_garbage_zone = False
        else:
            garbage_characters += 1

    else:
        if character == '!':
            exclamation_ignore = True
        elif character == '<':
            in_garbage_zone = True
        else:
            if character == '{':
                local_score += 1
            elif character == '}':
                total_score += local_score
                local_score -= 1

print(garbage_characters)
print(total_score)
