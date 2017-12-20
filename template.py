#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pprint import pprint

with open('##a_data.txt', 'r') as f:
    input_data = f.read().split('\n')[:-1]

pprint(input_data[1:5])
