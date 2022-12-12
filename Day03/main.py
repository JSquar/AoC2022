#!/usr/bin/env python
# coding: utf-8
from pathlib import Path


debug = True
input = Path("input_small.txt")
# input=Path("input_big.txt")
assert input.exists()


def divide(line):
    part_a = line[: int(len(line) / 2)]
    part_b = line[int(len(line) / 2) : -1]
    if debug:
        print(f"part_a: {part_a}")
        print(f"part_b: {part_b}")
    part_a_sorted = sorted(part_a)
    part_b_sorted = sorted(part_b)
    if debug:
        print(f"part_a_sorted: {part_a_sorted}")
        print(f"part_b_sorted: {part_b_sorted}")
    return part_a_sorted, part_b_sorted


def get_duplicates(list_a, list_b):
    print(f"Input:")
    print(f"list_a: {list_a}")
    print(f"list_b: {list_b}")
    # iterate over both lists and check for duplicates
    index_a = 0
    index_b = 0
    duplicates = []
    while index_a < len(list_a) and index_b < len(list_b):
        last_a = list_a[index_a]
        last_b = list_b[index_b]
        if debug:
            if index_a + 1 < len(list_a):
                print(
                    f"index_a: {index_a}, last_a: {last_a}, next_a: {list_a[index_a+1]}"
                )
            else:
                print(f"index_a: {index_a}, last_a: {last_a}")
            if index_b + 1 < len(list_b):
                print(
                    f"index_b: {index_b}, last_b: {last_b}, next_b: {list_b[index_b+1]}"
                )
            else:
                print(f"index_b: {index_b}, last_b: {last_b}")
        if last_a == last_b:
            duplicates.append(last_a)
        if last_a < last_b:
            if debug:
                print("Increase index_a by one")
            index_a += 1
        else:
            if debug:
                print("Increase index_b by one")
            index_b += 1
    return duplicates


def get_priority(letter):
    prio = ord(letter) - ord("a") + 1
    if prio < 0:
        prio += 27 - (ord("A") - ord("a")) - 1
    return prio


# PART A
# divide and conquer and sort
priority_sum = 0
with open(input) as fh:
    line = fh.readline()
    while line:
        list_a, list_b = divide(line)
        letter = get_duplicates(list_a, list_b)
        priority = get_priority(letter[0])
        priority_sum += priority
        line = fh.readline()

print(priority_sum)


# PART B
# concat all lines with each other an get all three combinations: 1-2, 1-3, 2-3
# checking each combination may return several letters, which could be the badge
# but the real badge only appears in all three subsets, which can be found via an intersection
priority_sum = 0
with open(input) as fh:
    line_a = fh.readline()
    line_b = fh.readline()
    line_c = fh.readline()
    while line_a:
        letters_ab = get_duplicates(sorted(line_a[:-1]), sorted(line_b[:-1]))
        letters_ac = get_duplicates(sorted(line_a[:-1]), sorted(line_c[:-1]))
        letters_bc = get_duplicates(sorted(line_b[:-1]), sorted(line_c[:-1]))
        if debug:
            print(f"letters_ab: {letters_ab}")
            print(f"letters_ac: {letters_ac}")
            print(f"letters_bc: {letters_bc}")
        intersection_letter = list(set(letters_ab) & set(letters_ac) & set(letters_bc))[
            0
        ]
        priority_sum += get_priority(intersection_letter)

        line_a = fh.readline()
        line_b = fh.readline()
        line_c = fh.readline()
