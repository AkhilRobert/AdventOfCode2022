from typing import Tuple

with open("./input.txt") as f:
    src = f.read()


def section_split(section: str) -> Tuple[int, int, int, int]:
    first = section.split(",")[0]
    second = section.split(",")[1]
    a, b = map(int, first.split("-"))
    x, y = map(int, second.split("-"))
    return (a, b, x, y)


def part_one(section: str) -> bool:
    a, b, x, y = section_split(section)
    return (a <= x and b >= y) or (x <= a and y >= b)


def part_two(section: str) -> bool:
    a, b, x, y = section_split(section)
    return len(set(range(a, b + 1)) & set(range(x, y + 1))) > 0


sections = [x for x in src.splitlines()]

print("Part 1: ", len([x for x in sections if part_one(x)]))
print("Part 2: ", len([x for x in sections if part_two(x)]))
