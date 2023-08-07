from typing import Dict


def part_one_score(shape: str) -> int:
    # score of outcome + score of shape
    strategy: Dict[str, int] = {
        "A X": 4,  # 3 + 1
        "A Y": 8,  # 6 + 2
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6,
    }
    return strategy[shape]


def part_two_score(shape: str) -> int:
    # score of shape + required outcome
    strategy: Dict[str, int] = {
        "A X": 3,  # choosing scissor as we have to lose, 3 + 0
        "A Y": 4,  # 3 + 1
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7,
    }
    return strategy[shape]


with open("input.txt") as f:
    src = f.read().splitlines()

print("Part one: ", sum(map(part_one_score, src)))
print("Part two: ", sum(map(part_two_score, src)))
