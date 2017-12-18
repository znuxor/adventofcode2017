#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections
from collections import defaultdict
import multiprocessing.pool
import time

with open('18a_data.txt', 'r') as f:
    input_data = f.read().split('\n')[:-1]

def snd(curr_inst, pull_queue, send_queue, prog_id, regs, played, *values):
    if type(values[0]) is int:
        send_queue.put(values[0])
    else:
        send_queue.put(regs[values[0]])
    send_number[prog_id] += 1


def set_reg(curr_inst, pull_queue, send_queue, prog_id, regs, played, *values):
    if type(values[1]) is int:
        regs[values[0]] = values[1]
    else:
        regs[values[0]] = regs[values[1]]


def add_reg(curr_inst, pull_queue, send_queue, prog_id, regs, played, *values):
    if type(values[1]) is int:
        regs[values[0]] += values[1]
    else:
        regs[values[0]] += regs[values[1]]


def mul_reg(curr_inst, pull_queue, send_queue, prog_id, regs, played, *values):
    if type(values[1]) is int:
        regs[values[0]] *= values[1]
    else:
        regs[values[0]] *= regs[values[1]]


def mod_reg(curr_inst, pull_queue, send_queue, prog_id, regs, played, *values):
    if type(values[1]) is int:
        regs[values[0]] %= values[1]
    else:
        regs[values[0]] %= regs[values[1]]

def rcv(curr_inst, pull_queue, send_queue, prog_id, regs, played, *values):
    regs[values[0]] = pull_queue.get()

def jump(curr_inst, pull_queue, send_queue, prog_id, regs, played, *values):
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

def program_launch(prog_id, recv_queue, send_queue):
    my_queue = recv_queue
    other_queue = send_queue
    curr_inst = [-1]
    regs = defaultdict(lambda: 0)
    regs['p'] = prog_id
    played = [None]
    while curr_inst[0] >= -1 and curr_inst[0] < len(input_data):
        curr_inst[0] += 1
        print(regs)
        opcode, *rest_of_op = input_data[curr_inst[0]].split(' ')
        rest_of_op = list(int(i) if i.lstrip('-').isdigit() else i for i in rest_of_op)
        operations[opcode](curr_inst, my_queue, other_queue, prog_id, regs, played, *rest_of_op)
        # print(regs)

# sciyoshi's code
def run(ident, inqueue, outqueue):
    regs = collections.defaultdict(int)
    regs['p'] = ident

    def val(v):
        try:
            return int(v)
        except ValueError:
            return regs[v]

    pc = 0
    count = 0
    played = None

    while 0 <= pc < len(input_data) - 1:
        cmd = input_data[pc].split()
        if cmd[0] == 'snd':
            played = val(cmd[1])
            if outqueue:
                outqueue.put(val(cmd[1]))
            count += 1
        elif cmd[0] == 'set':
            regs[cmd[1]] = val(cmd[2])
        elif cmd[0] == 'add':
            regs[cmd[1]] += val(cmd[2])
        elif cmd[0] == 'mul':
            regs[cmd[1]] *= val(cmd[2])
        elif cmd[0] == 'mod':
            regs[cmd[1]] %= val(cmd[2])
        elif cmd[0] == 'rcv':
            if inqueue:
                regs[cmd[1]] = inqueue.get()
            elif regs[cmd[1]] != 0:
                return played
        elif cmd[0] == 'jgz':
            if val(cmd[1]) > 0:
                pc += val(cmd[2])
                continue
        pc += 1

    return count

if __name__ == '__main__':
    send_number = [0, 0]
    pool = multiprocessing.pool.ThreadPool(processes=2)
    q1 = multiprocessing.Queue()
    q2 = multiprocessing.Queue()
    #res1 = pool.apply_async(program_launch, args=(0, q1, q2))
    #res2 = pool.apply_async(program_launch, args=(1, q2, q1))
    res0 = run(0, None, None)
    print(res0)
    res1 = pool.apply_async(run, args=(0, q1, q2))
    res2 = pool.apply_async(run, args=(1, q2, q1))
    res1.get()
    print(res2.get())

