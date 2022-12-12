#!/usr/bin/env python
# coding: utf-8
import heapq

input_file = "input_small.txt"
# input_file = "input.txt"
# if "INPUT" in os.environ:
#    input_file = os.environ["INPUT"]


# part 1
calories_sum = 0
max_calories = 0

with open(input_file) as fh:
    for current_line in fh:
        if current_line == "\n":
            if max_calories < calories_sum:
                max_calories = calories_sum
            calories_sum = 0
        else:
            calories_sum += int(current_line)
print(max_calories)


# part 2
calories_sum = 0
inventory = []
with open(input_file) as fh:
    for current_line in fh:
        if current_line == "\n":
            inventory.append(calories_sum)
            calories_sum = 0
        else:
            calories_sum += int(current_line)
print(inventory)
total_calories_3 = sum(heapq.nlargest(3, inventory))
print(heapq.nlargest(3, inventory))
print(total_calories_3)
