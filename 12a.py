#!/usr/bin/env python3
# -*- coding: utf-8 -*-



with open('12a_data.txt', 'r') as problem_input:
    data_input = problem_input.read().split('\n')
    del(data_input[-1])

graph_nodes = set()

def build_graph(current_node_number):
    graph_nodes.add(current_node_number)
    new_nodes = [int(x.rstrip(',')) for x in data_input[current_node_number].split(' ')[2:]]
    for a_new_node in new_nodes:
        if a_new_node not in graph_nodes:
            build_graph(a_new_node)


build_graph(0)
print(len(graph_nodes))
