#! /usr/bin/env python3

import os
import sys

project_directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
scripts_directory = os.path.join(project_directory, 'scripts')

cmd = [
    'docker', 'run',
    '-it', '--rm',
    '-v', '{}:/scripts'.format(scripts_directory),
    '-p', '8089:8089',
    'locusts'
]

os.system(' '.join(cmd + sys.argv[1:]))
