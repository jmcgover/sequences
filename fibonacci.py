#! /usr/bin/env python3

import functools
import typing

import sys
import argparse

_DESCRIPTION='A tool to print the Fibonacci Sequence or evaluate a value at a specific index.'
def get_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog=sys.argv[0], description=_DESCRIPTION)
    parser.add_argument('index', type=int, help='the term number or index to print the value of')
    return parser

class Memoized():
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if not isinstance(args, typing.Hashable):
            # Some objects, e.g. immutable ones like lists, are not hashable, so
            # we just return the executed function value.
            return self.func(*args)
        value = self.func(*args)
        self.cache[args] = value
        return value
    def __repr_(self):
        return self.func.__doc__
    def __get__(self, obj, objtype):
        return functools.partial(self.__call__, obj)


def fibonacci(n: int) -> int:
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