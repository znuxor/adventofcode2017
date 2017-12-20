#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict

with open('20a_data.txt', 'r') as f:
    input_data = f.read().split('\n')[:-1]

# input_data = ['p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>', 'p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>']
# input_data = ['p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>', 'p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>', 'p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>', 'p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>']

particles = dict()

for i, line in enumerate(input_data):
    p, v, a = line.split(', ')
    p = p[2:].rstrip('>').lstrip('<')
    v = v[2:].rstrip('>').lstrip('<')
    a = a[2:].rstrip('>').lstrip('<')
    p = [int(i) for i in p.split(',')]
    v = [int(i) for i in v.split(',')]
    a = [int(i) for i in a.split(',')]
    particles[i] = ([p, v, a])

PARTB = True
for iteration in range(40):

    collision_dict = defaultdict(list)
    for particle_index in particles:
        collision_dict[tuple(particles[particle_index][0])].append(particle_index)

    for position in collision_dict:
        if len(collision_dict[position]) > 1:
            for a_particle_index in reversed(sorted(collision_dict[position])):
                if PARTB:
                    del particles[a_particle_index]
                    # print('boom {} left, I removed {} for position {}'.format(len(particles), a_particle_index, position))


    for particle in particles:
        particles[particle][1] = [sum(i) for i in list(zip(particles[particle][1], particles[particle][2]))]
        particles[particle][0] = [sum(i) for i in list(zip(particles[particle][0], particles[particle][1]))]
    print(len(particles))

if not PARTB:
    distances = []
    for k in range(len(particles)):
        x, y, z = particles[k][0]
        distances.append(abs(x)+abs(y)+abs(z))
    index_min = distances.index(min(distances))
    print(index_min)
else:
    print('{} particles remaining'.format(len(particles)))
