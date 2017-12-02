#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

data_input = np.loadtxt('2a_data.txt')

mysum = 0
minimums = np.min(data_input, axis=1)
maximums = np.max(data_input, axis=1)
diffs = maximums - minimums

print(np.sum(diffs))
