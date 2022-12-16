#!/usr/bin/env python
# coding: utf-8

from pathlib import Path
import logging

# import numpy as np
import sys
import tqdm
import heapq

logger = logging.getLogger()
logger.setLevel(logging.WARNING)
logging.basicConfig()


# inputfile = Path("input_small.txt")
inputfile = Path("input_big.txt")
with open(inputfile, "r") as fh:
    lines = [line.strip() for line in fh.readlines()]

# arr = np.ndarray((len(lines),len(lines[0])))
arr = []
pos_starts = []
for index_row, row in enumerate(lines):
    arr.append([])
    for index_col, col in enumerate(row):
        if col == "S":
            pos_start = (index_row, index_col)
            arr[index_row].append(ord("a"))
            logger.debug(f"Start position: {pos_start}")
        elif col == "E":
            pos_end = (index_row, index_col)
            arr[index_row].append(ord("z"))
            logger.debug(f"End position: {pos_end}")
        else:
            if col == "a":
                pos_starts.append((index_row, index_col))
            arr[index_row].append(ord(col))


def make_step(current_position, direction):
    new_position = [
        current_position[0] + direction[0],
        current_position[1] + direction[1],
    ]
    logger.debug(
        f"Current position {current_position}, direction {direction} would result in new position {new_position}"
    )
    if new_position[0] < 0 or new_position[1] < 0:
        return None
    if new_position[0] >= len(arr) or new_position[1] >= len(arr[0]):
        return None
    if (
        arr[new_position[0]][new_position[1]]
        - arr[current_position[0]][current_position[1]]
        <= 1
    ):
        logger.debug(
            f"arr[new_position]: {arr[new_position[0]][new_position[1]]}, arr[current_position]: {arr[current_position[0]][current_position[1]]}"
        )
        return new_position


# Part A
def dijkstra(start_position):
    # try shortest path via Dijkstra
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    # queue collects nodes, which still need to be processed
    queue = []
    # dijkstra "grid" allows easy access on specific positions
    dijkstra = []
    for index_row in range(len(lines)):
        dijkstra.append([])
        for index_col in range(len(lines[0])):
            # tuple meaning:
            # first: weight alias distance
            # second: coordinates
            # third: coordinates of predecessor
            queue.append([sys.maxsize, (index_row, index_col), None])
            dijkstra[index_row].append(queue[-1])

    # set distance of start_position
    # queue[pos_start[0]][pos_start[1]] = 0
    dijkstra[start_position[0]][start_position[1]][0] = 0
    heapq.heapify(queue)

    while len(queue) > 0:
        current_node = heapq.heappop(queue)
        current_position = current_node[1]
        if current_position == pos_end:
            logger.debug(f"End position has been popped, dijkstra terminates")
            break
        logger.debug(f"New node from queue: {current_node}")
        #    visited.append(current_position)
        for direction in directions:
            new_position = make_step(current_position, direction)
            if new_position:
                neighbour = dijkstra[new_position[0]][new_position[1]]
                if neighbour in queue:
                    current_distance = current_node[0]
                    logger.debug(
                        f"Consider neighbour coordinates {new_position} which is in queue as {neighbour}"
                    )
                    # add arbitrary weight 0.001 to favour shorter pathes. Otherwise neighbours with weight 0 but many node jumps are equivalent worthy, but we focus on minimum node count
                    alternate_path_length = (
                        current_distance
                        + (
                            arr[new_position[0]][new_position[1]]
                            - arr[current_position[0]][current_position[1]]
                        )
                        + 0.001
                    )
                    logger.debug(
                        f"Alternative path lenght: {alternate_path_length}\tPrior path length: {neighbour[0]}"
                    )
                    if alternate_path_length < neighbour[0]:
                        neighbour[0] = alternate_path_length
                        neighbour[2] = current_position
                        logger.debug(f"Update neighbour to {neighbour}")
                        heapq.heapify(queue)
            logger.debug("")

    # after shortest path had been constructed, follow path from end position to start position and count visited nodes
    current_node = dijkstra[pos_end[0]][pos_end[1]]
    counter = 0
    try:
        while current_node[1] != start_position:
            counter += 1
            current_node = dijkstra[current_node[2][0]][current_node[2][1]]
            logger.debug(f"Current node: {current_node}")
        return counter
    except:
        logger.info(f"Error on start position {start_position}, skip path calculation")


shortest_path = sys.maxsize
for position in tqdm.tqdm([pos_start] + pos_starts):
    path = dijkstra(position)
    logger.info(path)
    try:
        if path < shortest_path:
            shortest_path = path
    except:
        logger.info(f"Skip run from start position {position}")
print(shortest_path)
