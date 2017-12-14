#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pprint import pprint


with open('12a_data.txt', 'r') as problem_input:
    data_input = problem_input.read().split('\n')
    del(data_input[-1])

# data_input = """0 <-> 2
# 1 <-> 1
# 2 <-> 0, 3, 4
# 3 <-> 2, 4
# 4 <-> 2, 3, 6
# 5 <-> 6
# 6 <-> 4, 5""".split('\n')

graph_number = 0
graph_nodes = set()
global_graph_nodes = set()
def build_graph(current_node_number):
    graph_nodes.add(current_node_number)
    new_nodes = [int(x.rstrip(',')) for x in data_input[current_node_number].split(' ')[2:]]
    for a_new_node in new_nodes:
        if a_new_node not in graph_nodes:
            build_graph(a_new_node)

for node_number in range(len(data_input)):
    if node_number not in global_graph_nodes:
        graph_number += 1
        build_graph(node_number)
        if not global_graph_nodes.isdisjoint(graph_nodes):
            print("shit")
            input()
        global_graph_nodes.update(graph_nodes)
        graph_nodes = set()

print(graph_number)
