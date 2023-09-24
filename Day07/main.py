import re
from sys import stdin
from typing import List, Self, Tuple

commands = list(map(lambda x: x.strip(), stdin.readlines()))


class File:
    name: str
    size: int

    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size


class Folder:
    name: str
    files: List[File]
    folders: List[Self]

    def __init__(self, name: str) -> None:
        self.name = name
        self.files = []
        self.folders = []

    def add_folder(self, folder: Self) -> None:
        self.folders.append(folder)

    def add_file(self, file: File) -> None:
        self.files.append(file)

    def calculate_file_size(self) -> int:
        result = 0
        for i in self.files:
            result += i.size
        return result


# Parsing the input
stack: List[Folder] = [Folder("/")]
for i in range(2, len(commands)):
    current = commands[i]
    if current == "$ ls" or "dir" in current:
        continue

    if "$ cd" in current:
        result = re.findall(r"^\$ cd (\w+|\/|..)", current)[0]
        if result == "..":
            stack.pop()
        else:
            parent = stack[-1]
            folder = Folder(result)
            parent.add_folder(folder)
            stack.append(folder)
    else:
        result = re.findall(r"(\d+) (\w+.\w+|\w+)", current)
        file = File(result[0][1], int(result[0][0]))
        folder = stack[-1]
        folder.add_file(file)


def calculate_total_size(parent: Folder) -> List[Tuple[str, int]]:
    result = []

    def recurse(parent: Folder) -> int:
        total = parent.calculate_file_size()

        if len(parent.folders) == 0:
            result.append((parent.name, total))
            return total

        for i in parent.folders:
            current = recurse(i)
            total += current

        result.append((parent.name, total))

        return total

    recurse(parent)
    return result


def part_one(parent: Folder) -> int:
    return sum([x for (_, x) in calculate_total_size(parent) if x <= 100000])


def part_two(parent: Folder):
    sizes = calculate_total_size(parent)
    free = 70000000 - sizes[-1][1]
    return min([x for (_, x) in sizes if free + x >= 30000000])


print("Part 1:", part_one(stack[0]))
print("Part 2:", part_two(stack[0]))
