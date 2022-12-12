#!/usr/bin/env python
# coding: utf-8
from pathlib import Path
from collections import deque


def pretty_print(data, limit):
    # print(data)
    for row in range(limit - 1, -1, -1):
        for column in range(len(data)):
            try:
                print(f"{list(data[column])[row][:-1]} ", end="")
            except:
                print(" -- ", end="")
        print("")
    print("")


debug = False
# inputfile = Path("input_small.txt")
inputfile = Path("input_big.txt")

fh = open(inputfile, "r")
data = fh.readlines()
fh.close()


split_index = data.index("\n")
towers = data[:split_index]
movement_text = data[split_index + 1 :]
# columns = towers[-1].split()
movement = [x.split() for x in movement_text]


data_stacks = []
for i in range(int((len(towers[-1]) + 1) / 4)):
    data_stacks.append(deque())

for row in range(len(towers) - 2, -1, -1):
    for column in range(int((len(towers[-1]) + 1) / 4)):
        entry = towers[row][3 * column + column : 4 * (column + 1)]
        if entry[:3] != " " * 3:
            data_stacks[column].append(entry)

# perform movement part A
for index, action in enumerate(movement):
    num_blocks = int(action[1])
    from_column = int(action[3]) - 1
    to_column = int(action[5]) - 1
    for block in range(num_blocks):
        if debug:
            print(f"Move {num_blocks} from {from_column} to {to_column}")
            pretty_print(data_stacks, split_index)
        try:
            current = data_stacks[from_column].pop()
            data_stacks[to_column].append(current)
        except Exception as e:
            print(f"Error on action index {index}")
            print(f"Move {num_blocks} from {from_column} to {to_column}")
            pretty_print(data_stacks, split_index)
            raise e
        if debug:
            pretty_print(data_stacks, split_index)

pretty_print(data_stacks, 32)
final_top = ""
for i in data_stacks:
    final_top += i.pop()[1]
print(f"\n{final_top}")

foo = list(range(10))

data_stacks = []
for i in range(int((len(towers[-1]) + 1) / 4)):
    data_stacks.append([])

for row in range(len(towers) - 2, -1, -1):
    for column in range(int((len(towers[-1]) + 1) / 4)):
        entry = towers[row][3 * column + column : 4 * (column + 1)]
        if entry[:3] != " " * 3:
            data_stacks[column].append(entry)

# perform movement part B
for index, action in enumerate(movement):
    num_blocks = int(action[1])
    from_column = int(action[3]) - 1
    to_column = int(action[5]) - 1
    if debug:
        print(f"Move {num_blocks} from {from_column} to {to_column}")
        pretty_print(data_stacks, split_index)
    try:
        # current=42
        current = data_stacks[from_column][-num_blocks:]
        data_stacks[from_column] = data_stacks[from_column][:-num_blocks]
        # print(current)
        # data_stacks[from_column]
        data_stacks[to_column].extend(current)
    except Exception as e:
        print(f"Error on action index {index}")
        print(f"Move {num_blocks} from {from_column} to {to_column}")
        pretty_print(data_stacks, split_index)
        raise e
    if debug:
        pretty_print(data_stacks, split_index)

pretty_print(data_stacks, 5)
final_top = ""
for i in data_stacks:
    final_top += i.pop()[1]
print(f"\n{final_top}")
