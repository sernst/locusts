#! /usr/bin/env python3
import argparse
import os
import sys


def parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('locust_io_version')
    return parser.parse_args()


def main(args: argparse.Namespace):
    print('PUSHING IMAGES')
    cmd = ['docker', 'push', 'swernst/locusts:latest']
    os.system(' '.join(cmd))

    cmd = ['docker', 'push', f'swernst/locusts:{args.locust_io_version}']
    os.system(' '.join(cmd))
    print('IMAGES PUSHED')


if __name__ == '__main__':
    main(parse())
