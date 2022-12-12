#!/usr/bin/env python
# coding: utf-8
from pathlib import Path
import numpy as np


debug = False
# input_file = Path("input_small.txt")
input_file = Path("input_big.txt")

with open(input_file, "r") as fh:
    lines = fh.readlines()
    lines = [line.strip() for line in lines]


data = np.zeros((len(lines), len(lines)))
for index_line, line in enumerate(lines):
    for index_letter, letter in enumerate(line):
        data[index_line][index_letter] = int(letter)


def count_visible_trees(line, current_max_height=-1):
    indices = np.zeros((len(line),))
    for index, tree in enumerate(line):
        if current_max_height < tree:
            indices[index] = 1
            current_max_height = tree
    if debug:
        print(f"Indices {indices} for line {line}")
    return indices


# part A
visibility_matrix = np.zeros((len(lines), len(lines)))
for i in range(len(lines)):
    # left to right
    visibility_matrix[i, :] += count_visible_trees(data[i, :])
    # right to left
    visibility_matrix[i, ::-1] += count_visible_trees(data[i, ::-1])
    # top to bottom
    visibility_matrix[:, i] += count_visible_trees(data[:, i])
    # bottom to top
    visibility_matrix[::-1, i] += count_visible_trees(data[::-1, i])

if debug:
    print(f"Visibility matrix:")
    print(visibility_matrix)

visible_tree_count = np.sum(visibility_matrix > 0)
print(f"Total visible trees: {visible_tree_count}")

# part B
# iterate over every tree and check visibility lines for all four directions
# method omits trees, which are smaller than bigger trees before, but should nevertheless count into view distance. Therefore the first occurence of value "1" denotes viewing distance


def get_scenic_factor(bool_line):
    # 0 if len(bool_left) == 1 else np.argmax(bool_left[1:]) +1 if max(bool_left[1:]) > 0 else len(bool_left) - 1
    result = 0
    if len(bool_line) > 1:
        # some higher tree (not padding) was found
        if max(bool_line[1:]) > 0:
            result = np.argmax(bool_line[1:]) + 1
        # take distance to padding
        else:
            result = len(bool_line[1:])
    return result


scenic_score_max = 0
for row in range(len(lines)):
    for col in range(len(lines)):
        my_height = data[row, col]
        # add artifical border, so that at least one True value is given in height comparison, so that argmax does not return index of first False
        bool_left = data[row, col::-1] >= my_height
        bool_right = data[row, col:] >= my_height
        bool_below = data[row:, col] >= my_height
        bool_above = data[row::-1, col] >= my_height

        left = get_scenic_factor(bool_left)
        right = get_scenic_factor(bool_right)
        above = get_scenic_factor(bool_above)
        below = get_scenic_factor(bool_below)

        if debug:
            print(f"My height: {my_height}")
            print(f"left: {left}")
            print(f"right: {right}")
            print(f"below: {below}")
            print(f"above: {above}")
        scenic_score = left * right * above * below
        if scenic_score > scenic_score_max:
            scenic_score_max = scenic_score
print(scenic_score_max)
