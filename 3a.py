#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

puzzle_input = 325489

distance = abs((puzzle_input - 4 * (math.ceil(-0.5 + puzzle_input**0.5 / 2))**2 + 4 * (math.ceil(-0.5 + puzzle_input**0.5 / 2)) - 2) %
               (2 * (math.ceil(-0.5 + puzzle_input**0.5 / 2))) - (math.ceil(-0.5 + puzzle_input**0.5 / 2)) + 1) + (math.ceil(-0.5 + puzzle_input**0.5 / 2))

print(distance)
