#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('19a_data.txt', 'r') as f:
    input_data = f.read().split('\n')[:-1]

x = (input_data[0].index('|'))
y = 0

direction = 'D'
letters = []
current_case = '|'

while current_case != ' ':
    if direction == 'D':
        y += 1
    elif direction == 'U':
        y -= 1
    elif direction == 'L':
        x -= 1
    elif direction == 'R':
        x += 1
    current_case = input_data[y][x]
    if current_case == '+':
        if direction in ('D', 'U'):
            if input_data[y][x-1] != ' ':
                direction = 'L'
            else:
                direction = 'R'
        else:
            if input_data[y-1][x] != ' ':
                direction = 'U'
            else:
                direction = 'D'

    elif current_case not in ('|', '-'):
        letters.append(current_case)

print(''.join(letters))
