import logging
from pathlib import Path
import re
import numpy as np
import math

logging.basicConfig(format="%(message)s")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# inputfile = Path("input_small.txt")
inputfile = Path("input_big.txt")
partB = True
with open(inputfile, "r") as fh:
    lines = [line.strip() for line in fh.readlines()]

assert (len(lines) + 1) % 4 == 0, f"len(lines) ({len(lines)}) must be divisible by 7"
rules = {}
regex = re.compile(
    r"Monkey (?P<Monkey_start>\d+): Starting items: (?P<items>(?:\d+,?\s?)+)Operation: new = (?P<operation>old (?:\+|\*|-|/) \w+) Test: divisible by (?P<divisor>\d+) If true: throw to monkey (?P<Monkey_target_true>\d+) If false: throw to monkey (?P<Monkey_target_false>\d+)"
)

for index in range(int((len(lines) + 1) / 7)):
    single_line = " ".join(lines[index * 7 : index * 7 + 6])
    matches = regex.match(single_line)
    assert matches, f"No match found on line {single_line}"

    rules[int(matches.group("Monkey_start"))] = {
        "items": [int(item.strip()) for item in matches.group("items").split(",")],
        "op": matches.group("operation"),
        "divisor": int(matches.group("divisor")),
        "targets": (
            int(matches.group("Monkey_target_true")),
            int(matches.group("Monkey_target_false")),
        ),
    }

    rules[int(matches.group("Monkey_start"))]["inspection_count"] = 0

# had to look for tips for stress relief, was inspired by this solution: https://www.reddit.com/r/adventofcode/comments/zifqmh/comment/j002ro0/?utm_source=share&utm_medium=web2x&context=3
stress_relief = math.prod([rules[monkey]["divisor"] for monkey in rules])
logger.debug(f"Stress relief factor is {stress_relief}")

end_range = 20 if not partB else 10000
for round in range(1, end_range + 1):
    for monkey in range(len(rules)):
        logger.debug(f"Monkey {monkey}")
        while len(rules[monkey]["items"]) > 0:
            # 1. inspect
            rules[monkey]["inspection_count"] += 1
            old = rules[monkey]["items"].pop(0)
            if not partB:
                logger.debug(f"  Monkey inspects an item with a worry level of {old}")

            # 2. Increase worry level

            summands = rules[monkey]["op"].split()
            if summands[2] == "old":
                summand2 = old
            else:
                summand2 = int(summands[2])
            new = (
                np.add(old, summand2)
                if summands[1] == "+"
                else np.multiply(old, summand2)
            )

            if not partB:
                logger.debug(f"  Worry level is changed to {new}")

            # 3. Decrease worry level (disable for part B)
            if not partB:
                new = int(new // 3)
                logger.debug(f"  Worry level is divided by 3 to {new}")
            else:
                new = new % stress_relief

            # 4. Pass item to different monkey
            if new % rules[monkey]["divisor"] == 0:
                target = rules[monkey]["targets"][0]
            else:
                target = rules[monkey]["targets"][1]
            rules[target]["items"].append(new)
            if not partB:
                logger.debug(f"  Item {new} is passed to monkey {target}")
            assert rules[target]["items"][-1] == new
    if round in [1, 20] + list(range(1000, 11000, 1000)):
        inspection_counts = [
            rules[index]["inspection_count"] for index in range(len(rules))
        ]
        logger.info(f"After {round} rounds")
        for index in range(len(rules)):
            logger.info(
                f"Monkey {index} inspected items {inspection_counts[index]} times."
            )


inspection_counts = [rules[index]["inspection_count"] for index in range(len(rules))]
inspection_counts.sort()
monkey_business = inspection_counts[-1] * inspection_counts[-2]
print(monkey_business)
