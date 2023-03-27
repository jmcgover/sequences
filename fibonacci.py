#! /usr/bin/env python3

import argparse
import cProfile
import functools
import typing
import sys


_DESCRIPTION='A tool to print the Fibonacci Sequence or evaluate a value at a specific index.'
def get_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog=sys.argv[0], description=_DESCRIPTION)
    parser.add_argument('index', type=int, help='the term number or index to print the value of')
    return parser

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def main() -> int:
    parser = get_arg_parser()
    args = parser.parse_args()
    print(fibonacci(args.index))
    return 0

if __name__ == '__main__':
    sys.exit(main())