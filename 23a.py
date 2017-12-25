#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict

with open('23a_data.txt', 'r') as f:
    input_data = f.read().split('\n')[:-1]

pipes = [[], []]


def set_reg(curr_inst, prog_id, regs, played, *values):
    if type(values[1]) is int:
        regs[values[0]] = values[1]
    else:
        regs[values[0]] = regs[values[1]]


def sub_reg(curr_inst, prog_id, regs, played, *values):
    if type(values[1]) is int:
        regs[values[0]] -= values[1]
    else:
        regs[values[0]] -= regs[values[1]]

mul_cnter = 0

def mul_reg(curr_inst, prog_id, regs, played, *values):
    global mul_cnter
    mul_cnter += 1
    if type(values[1]) is int:
        regs[values[0]] *= values[1]
    else:
        regs[values[0]] *= regs[values[1]]


def jnz(curr_inst, prog_id, regs, played, *values):
    if type(values[0]) is int and values[0]:
        curr_inst[0] += values[1]-1
    elif regs[values[0]]:
        curr_inst[0] += values[1]-1

operations = {
    'set': set_reg,
    'sub': sub_reg,
    'mul': mul_reg,
    'jnz': jnz
}

def program_launch(prog_id):
    curr_inst = [-1]
    regs = defaultdict(lambda: 0)
    played = [None]
    while curr_inst[0] >= -1 and curr_inst[0] < len(input_data)-1:
        curr_inst[0] += 1
        # print(curr_inst, prog_id)
        # print(regs)
        # print(input_data[curr_inst[0]])
        # print()
        #__import__('time').sleep(0.1)
        opcode, *rest_of_op = input_data[curr_inst[0]].split(' ')
        rest_of_op = list(int(i) if i.lstrip('-').isdigit() else i for i in rest_of_op)
        operations[opcode](curr_inst, prog_id, regs, played, *rest_of_op)
    print(mul_cnter)

if __name__ == '__main__':
    program_launch(0)
