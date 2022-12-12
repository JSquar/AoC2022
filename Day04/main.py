#!/usr/bin/env python
# coding: utf-8
from pathlib import Path


debug = False
# inputfile = Path("input_small.txt")
inputfile = Path("input_big.txt")
with open(inputfile) as fh:
    lines = fh.readlines()


def is_included_complete(line):
    elf_a, elf_b = line.split(",")
    elf_a_limits = elf_a.split("-")
    elf_b_limits = elf_b.split("-")
    if elf_b_limits[1][-1] == "\n":
        elf_b_limits[1] = elf_b_limits[1][:-1]
        pass
    if debug:
        print(f"elf a: {elf_a_limits[0]} - {elf_a_limits[1]}")
        print(f"elf a: {elf_b_limits[0]} - {elf_b_limits[1]}")
    # elf a included in elf b?
    if int(elf_a_limits[0]) >= int(elf_b_limits[0]) and int(elf_a_limits[1]) <= int(
        elf_b_limits[1]
    ):
        if debug:
            print(f"elf a is included in elf b")
        return True
    if int(elf_b_limits[0]) >= int(elf_a_limits[0]) and int(elf_b_limits[1]) <= int(
        elf_a_limits[1]
    ):
        if debug:
            print("elf b is included in elf a")
        return True
    return False


def is_included_partially(line):
    elf_a, elf_b = line.split(",")
    elf_a_limits = elf_a.split("-")
    elf_b_limits = elf_b.split("-")
    if elf_b_limits[1][-1] == "\n":
        elf_b_limits[1] = elf_b_limits[1][:-1]
        pass
    if debug:
        print(f"elf a: {elf_a_limits[0]} - {elf_a_limits[1]}")
        print(f"elf a: {elf_b_limits[0]} - {elf_b_limits[1]}")
    # elf a included in elf b?
    return (
        len(
            set(range(int(elf_a_limits[0]), int(elf_a_limits[1]) + 1)).intersection(
                range(int(elf_b_limits[0]), int(elf_b_limits[1]) + 1)
            )
        )
        != 0
    )


sum_included = 0
for line in lines:
    sum_included += is_included_complete(line)
print(sum_included)


sum_included = 0
for line in lines:
    sum_included += is_included_partially(line)
print(sum_included)
