#!/usr/bin/env python
# coding: utf-8
from pathlib import Path

debug = False
input_file = Path("input_small.txt")
# input_file = Path("input_big.txt")


with open(input_file, "r") as fh:
    lines = fh.readlines()
    lines = [x.strip() for x in lines]


def get_start_marker(line):
    for index in range(14, len(line)):
        buffer = line[index - 14 : index]
        if debug:
            print(buffer)
        if len(set(buffer)) == 4:
            return index


for line in lines:
    print(get_start_marker(line))
