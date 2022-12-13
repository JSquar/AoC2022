#!/usr/bin/env python
# coding: utf-8
from pathlib import Path
import numpy as np
import logging

logging.basicConfig()
logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)


def get_new_tail_pos(head, tail):
    diff_vec = tail - head
    # distance big enough?
    if np.max(np.abs(diff_vec)) <= 1:
        return tail
    assert np.max(np.abs(diff_vec)) <= 2
    signs = np.sign(diff_vec)
    logger.debug(f"diff_vec: {diff_vec}")
    # calc new tail if diff vec is at least 2 in one component, otherwise both vecs are still touching
    for index in [0, 1]:
        if abs(diff_vec[index]) > 1:
            diff_vec[index] = signs[index]
    logger.debug(f"diff_vec: {diff_vec}")
    return tail - diff_vec


if logging.root.level <= logging.DEBUG:
    assert np.array_equal(
        get_new_tail_pos(np.array([1, 2]), np.array([0, 0])), np.array([1, 1])
    )
    assert np.array_equal(
        get_new_tail_pos(np.array([2, 1]), np.array([0, 0])), np.array([1, 1])
    )
    assert np.array_equal(
        get_new_tail_pos(np.array([2, -1]), np.array([0, 0])), np.array([1, -1])
    )
    assert np.array_equal(
        get_new_tail_pos(np.array([1, -2]), np.array([0, 0])), np.array([1, -1])
    )
    assert np.array_equal(
        get_new_tail_pos(np.array([-1, -2]), np.array([0, 0])), np.array([-1, -1])
    )
    assert np.array_equal(
        get_new_tail_pos(np.array([-2, -1]), np.array([0, 0])), np.array([-1, -1])
    )
    assert np.array_equal(
        get_new_tail_pos(np.array([-2, 1]), np.array([0, 0])), np.array([-1, 1])
    )
    assert np.array_equal(
        get_new_tail_pos(np.array([-1, 2]), np.array([0, 0])), np.array([-1, 1])
    )


# num_knots = 2
num_knots = 10
# input_file=Path("input_small.txt")
# input_file=Path("input_medium.txt")
input_file = Path("input_big.txt")
assert input_file.exists()

with open(input_file, "r") as fh:
    lines = fh.readlines()


# ease handling of input data and replace direction letters with vectors
directions = []
for line in lines:
    direction, factor = line.strip().split()
    factor = int(factor)
    if direction == "R":
        direction = np.array([1, 0])
    elif direction == "L":
        direction = np.array([-1, 0])
    elif direction == "U":
        direction = np.array([0, 1])
    elif direction == "D":
        direction = np.array([0, -1])
    else:
        raise Exception(f"Could not identify direction {direction}")
    directions.append((direction, factor))


knots = [np.array([0, 0])]
for knot in range(num_knots - 1):
    knots.append(np.array([0, 0]))
visited_positions = [knots[-1][:]]

for direction in directions:
    for iteration in range(direction[1]):
        knots[0] = knots[0] + direction[0]
        logger.debug(f"Was:\nfirst knot{knots[0]}\nlast knot {knots[-1]}")
        for index in range(1, num_knots):
            knots[index] = get_new_tail_pos(knots[index - 1], knots[index])
        logger.debug(f"Now:\nfirst knot{knots[0]}\nlast knot {knots[-1]}\n")
        visited_positions.append(knots[-1][:])
logger.info(
    f"Visited positions: {len({tuple(position) for position in visited_positions})}"
)
