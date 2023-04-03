#! /usr/bin/env python3

import argparse
import cProfile
import functools
import typing
import sys

_DESCRIPTION='A tool to print the Fibonacci Sequence or evaluate a value at a specific index.'
def get_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog = sys.argv[0], description = _DESCRIPTION)
    parser.add_argument('index', type = int, help = 'the term number or index to print the value of')
    parser.add_argument('-p','--print', help = 'print every value up to the specified index', action=argparse.BooleanOptionalAction)
    parser.add_argument('-s','--slow', help = 'list it the slow way', action=argparse.BooleanOptionalAction)
    return parser

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def list_fibonacci_slow(n:int) -> list[int]:
    fib_list = []
    for i in range(n + 1):
        fib_list.append(fibonacci(i))
    return fib_list

def list_fibonacci(n:int) -> list[int]:
    fib_list = []
    f_0 = 0
    f_1 = 1

    f_next = f_0 # Next to append
    f_next1 = f_1 # Next in the sequence

    for i in range(n + 1):
        fib_list.append(f_next)
        f_next2 = f_next + f_next1 # Sum of previous two in sequence
        f_next = f_next1
        f_next1 = f_next2

    return fib_list

def main() -> int:
    parser = get_arg_parser()
    args = parser.parse_args()
    n = args.index

    if args.print:
        if args.slow:
            print(list_fibonacci_slow(n))
        else: 
            print(list_fibonacci(n))
    else:
        if args.slow:
            print(list_fibonacci_slow(n)[-1])
        else: 
            print(fibonacci(n))
    return 0

if __name__ == '__main__':
    sys.exit(main())