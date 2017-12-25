#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from pprint import pprint
import math

with open('23b_data.txt', 'r') as f:
    input_data = f.read().split('\n')[:-1]


def isPrime(num):
    root = math.ceil(math.sqrt(num))
    for it_val in range(2, root):
        if not num % it_val:
            return False
    return True


# prime checker, we check if 10790 + 17N is prime
h = 0
for i in range(107900, 124900+1, 17):
    if not isPrime(i):
        h += 1
print(h)
