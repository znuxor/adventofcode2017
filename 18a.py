#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict

with open('18a_data.txt', 'r') as f:
    input_data = f.read().split('\n')[:-1]

pipes = [[], []]

def snd(curr_inst, prog_id, regs, played, *values):
    if type(values[0]) is int:
        played[0] = values[0]
    else:
        played[0] = regs[values[0]]


def set_reg(curr_inst, prog_id, regs, played, *values):
    if type(values[1]) is int:
        regs[values[0]] = values[1]
    else:
        regs[values[0]] = regs[values[1]]


def add_reg(curr_inst, prog_id, regs, played, *values):
    if type(values[1]) is int:
        regs[values[0]] += values[1]
    else:
        regs[values[0]] += regs[values[1]]


def mul_reg(curr_inst, prog_id, regs, played, *values):
    if type(values[1]) is int:
        regs[values[0]] *= values[1]
    else:
        regs[values[0]] *= regs[values[1]]


def mod_reg(curr_inst, prog_id, regs, played, *values):
    if type(values[1]) is int:
        regs[values[0]] %= values[1]
    else:
        regs[values[0]] %= regs[values[1]]


def rcv(curr_inst, prog_id, regs, played, *values):
    if type(values[0]) is int:
        if values[0]:
            print(played)
            print('done!')
            raise Exception('done lol')
    else:
        if regs[values[0]]:
            print(played)
            print('done!')
            raise Exception('done lol')


def jump(curr_inst, prog_id, regs, played, *values):
    if type(values[0]) is int:
        if values[0] > 0:
            if type(values[1]) is int:
                curr_inst[0] += values[1]
            else:
                curr_inst[0] += regs[values[1]]

    else:
        if regs[values[0]] > 0:
            if type(values[1]) is int:
                curr_inst[0] += values[1] - 1
            else:
                curr_inst[0] += regs[values[1]] - 1



operations = {
    'snd': snd,
    'set': set_reg,
    'add': add_reg,
    'mul': mul_reg,
    'mod': mod_reg,
    'rcv': rcv,
    'jgz': jump
}

def program_launch(prog_id):
    curr_inst = [-1]
    regs = defaultdict(lambda: 0)
    played = [None]
    while curr_inst[0] >= -1 and curr_inst[0] < len(input_data):
        curr_inst[0] += 1
        # print(curr_inst, prog_id)
        # print(regs)
        # print(input_data[curr_inst])
        # print()
        #__import__('time').sleep(0.1)
        opcode, *rest_of_op = input_data[curr_inst[0]].split(' ')
        rest_of_op = list(int(i) if i.lstrip('-').isdigit() else i for i in rest_of_op)
        operations[opcode](curr_inst, prog_id, regs, played, *rest_of_op)

if __name__ == '__main__':
    program_launch(0)
