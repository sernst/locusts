#! /usr/bin/env python3

import os

directory = os.path.realpath(os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '..'
))

cmd = [
    'docker',
    'build',
    '-t', 'swernst/locusts',
    '"{}"'.format(directory)
]

print('BUILDING CONTAINER IMAGE...')
os.system(' '.join(cmd))
print('IMAGE BUILT')
