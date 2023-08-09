from typing import List


def calculate_priority(items: List) -> int:
    result = 0
    for i in items:
        if i[0].islower():
            result += ord(i[0]) - 96
        else:
            result += ord(i[0]) - 65 + 27
    return result


with open("./input.txt") as f:
    src = f.read()

rucksacks = [x for x in src.splitlines()]
items = [list(set(x[: len(x) // 2]) & set(x[len(x) // 2 :])) for x in rucksacks]

grouped_rucksacks = [rucksacks[3 * i : 3 * i + 3] for i in range(len(rucksacks) // 3)]
grouped_items = [list(set(x[0]) & set(x[1]) & set(x[2])) for x in grouped_rucksacks]

print("Part 1:", calculate_priority(items))
print("Part 2:", calculate_priority(grouped_items))
