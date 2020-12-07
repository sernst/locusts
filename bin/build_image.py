#! /usr/bin/env python3
import argparse
import os

directory = os.path.realpath(os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '..'
))


def parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('locust_io_version')
    return parser.parse_args()


def main(args: argparse.Namespace):
    cmd = [
        'docker',
        'build',
        '-t', 'swernst/locusts:latest',
        '-t', f'swernst/locusts:{args.locust_io_version}',
        '"{}"'.format(directory)
    ]

    print('BUILDING CONTAINER IMAGE...')
    os.system(' '.join(cmd))
    print('IMAGE BUILT')


if __name__ == '__main__':
    main(parse())
