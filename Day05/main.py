import re
from functools import reduce
from typing import List

with open("./input.txt") as f:
    src = f.read()


def transpose(l: List[List]) -> List[List]:
    t = []
    for i in range(len(l[0])):
        row = []
        for j in l:
            row.append(j[i])
        t.append(row)
    return t


tower, instructions = src.split("\n\n")

stacks = []
for i in tower.split("\n")[:-1]:
    stacks.append([x for i, x in enumerate(i) if i % 4 == 1])

stacks = list(
    map(
        lambda x: "".join(reversed(x)).strip(),
        map(
            lambda x: list(reversed(x)),
            transpose(stacks),
        ),
    )
)

stack_one = stacks.copy()
stack_two = stacks.copy()


def part_one(stack: List[str], instruction: str):
    count, start, end = map(
        int, re.findall(r"move (\d+) from (\d+) to (\d+)", instruction)[0]
    )
    poped = []
    for _ in range(count):
        poped += stack[start - 1][0]
        stack[start - 1] = stack[start - 1][1:]

    poped.reverse()
    stack[end - 1] = "".join(poped) + stack[end - 1]


def part_two(stack: List[str], instruction: str):
    count, start, end = map(
        int, re.findall(r"move (\d+) from (\d+) to (\d+)", instruction)[0]
    )
    poped = stack[start - 1][:count]
    stack[start - 1] = stack[start - 1][count:]
    stack[end - 1] = poped + stack[end - 1]


for instruction in instructions.splitlines():
    part_one(stack_one, instruction)
    part_two(stack_two, instruction)

print("Part 1: ", reduce(lambda acc, x: acc + x[0], stack_one, ""))
print("Part 2: ", reduce(lambda acc, x: acc + x[0], stack_two, ""))
