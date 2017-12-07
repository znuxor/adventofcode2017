#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from collections import Counter

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
    def  __init__(self, weight, name):
        self.name = name
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

    def get_cumulative_weight(self):
        cum_weight = self.weight
        for child in self.child_nodes:
            cum_weight += child.get_cumulative_weight()
        return cum_weight

    def is_balanced(self):
        child_cum_weights = []
        for child in self.child_nodes:
            child_cum_weights.append(child.get_cumulative_weight())
        if len(set(child_cum_weights)) <= 1:
            return True
        else:
            return False

    def get_odd_child(self):
        child_cum_weights = []
        for child in self.child_nodes:
            child_cum_weights.append(child.get_cumulative_weight())
        counter = Counter(child_cum_weights)
        wrong_child = self.child_nodes[child_cum_weights.index(counter.most_common(2)[1][0])]
        if wrong_child.is_balanced():
            return wrong_child.name
        else:
            return wrong_child.get_odd_child()



nodes_dict = dict()

# create the nodes
for line in data_input:
    split_line = line.split(" ")
    name = split_line[0]
    weight = int(split_line[1][1:-1])
    new_node = Node(weight, name)
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
    if not nodes_dict[node_name].is_balanced():
        #print(node_name + ' is not balanced')
        #print("Its cumulative weight is: ", end = "")
        #print(nodes_dict[node_name].get_cumulative_weight())
        odd_child_name = nodes_dict[node_name].get_odd_child()
        print(odd_child_name + ' is the node with the wrong weight.')
        needed_cum_weight = 0
        for child in nodes_dict[odd_child_name].parent_node.child_nodes:
            if child.name != odd_child_name:
                needed_cum_weight = child.get_cumulative_weight()
                break
        weight_delta = needed_cum_weight - nodes_dict[odd_child_name].get_cumulative_weight()
        correct_weight = nodes_dict[odd_child_name].weight + weight_delta
        print('The correct weight should be: ', end = '')
        print(correct_weight)
        break

