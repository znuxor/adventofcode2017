#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('##a_data.txt', 'r') as f:
    input_data = f.read().split('\n')[:-1]

print(input_data[1:5])
