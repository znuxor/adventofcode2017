#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from collections import defaultdict

with open('7a_data.txt', 'r') as problem_input:
    data_input = problem_input.read().split('\n')[:-1]

# data_input = """pbga (66)
# xhth (57)
# ebii (61)
# havc (66)
# ktlj (57)
# fwft (72) -> ktlj, cntj, xhth
# qoyq (66)
# padx (45) -> pbga, havc, qoyq
# tknk (41) -> ugml, padx, fwft
# jptl (61)
# ugml (68) -> gyxo, ebii, jptl
# gyxo (61)
# cntj (57)""".split('\n')

# Build the tree

class Node():
    def  __init__(self, weight):
        self.weight = weight
        self.child_nodes = []
        self.parent_node = None

    def add_child_node(self, child_node):
        self.child_nodes.append(child_node)
        child_node.set_parent(self)

    def set_parent(self, parent_node):
        if self.has_parent():
            raise Error("Already a parent")
        else:
            self.parent_node = parent_node

    def has_parent(self):
        if self.parent_node is not None:
            return True
        else:
            return False

nodes_dict = dict()

# create the nodes
for line in data_input:
    split_line = line.split(" ")
    name = split_line[0]
    weight = int(split_line[1][1:-1])
    new_node = Node(weight)
    nodes_dict[name] = new_node

# add the structural information
for line in data_input:
    split_line = line.split(" ")
    if len(split_line) == 2:
        continue
    name = split_line[0]
    for child_node_string in split_line[3:]:
        child_node = nodes_dict[child_node_string.rstrip(',')]
        nodes_dict[name].add_child_node(child_node)

for node_name in nodes_dict:
    if not nodes_dict[node_name].has_parent():
        print(node_name + ' has no parent!')

