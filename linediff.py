#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv as sys_argv
from sys import exit as sys_exit
import argparse

# colors
native = "\033[m"
red = "\033[31m"
green = "\033[32m"

# arg parser
parser = argparse.ArgumentParser(
    prog = 'LineDiff',
    description = 'Compare lines between two files'
)
parser.add_argument('file_1', help='File no.1', action='store', metavar='first_file')
parser.add_argument('file_2', help='File no.2', action='store', metavar='second_file')

args = vars(parser.parse_args(sys_argv[1:]))

printable = '{0}[{1}] {2}' + native

fn1 = args['file_1']
fn2 = args['file_2']
try:
    with open(fn1,'r',encoding='utf-8') as f1:
        lines_1 = f1.read().splitlines()
except FileNotFoundError:
    print('LineDiff: error: file no.1 not found')
    sys_exit()

try:
    with open(fn2,'r',encoding='utf-8') as f2:
        lines_2 = f2.read().splitlines()
except FileNotFoundError:
    print('LineDiff: error: file no.2 not found')
    sys_exit()

print('{0} >>> {1}'.format(fn1,fn2))
for line in lines_1:
    if line not in lines_2:
        print(printable.format(green,'+',line))
    else:
        lines_2.pop(lines_2.index(line))

print('{0} <<< {1}'.format(fn1,fn2))
for line in lines_2:
    print(printable.format(red,'-',line))
