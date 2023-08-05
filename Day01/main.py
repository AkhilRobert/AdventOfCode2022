def part_one(source: str) -> int:
    input_array = source.strip().split("\n")
    total_array = []
    total = 0

    for value in input_array:
        if value == "":
            total_array.append(total)
            total = 0
        else:
            total += int(value)
    return max(total_array)


def part_two(source: str) -> int:
    input_array = source.strip().split("\n")
    total_array = []
    total = 0

    for value in input_array:
        if value == "":
            total_array.append(total)
            total = 0
        else:
            total += int(value)

    # put the last total to the list
    if total != 0:
        total_array.append(total)

    total_array.sort(reverse=True)
    return sum(total_array[:3])


test_input = r"""1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

print("Test Part One: ", part_one(test_input))
print("Test Part Two: ", part_two(test_input))

print("=" * 30)

with open("./input.txt", "r") as f:
    source = str(f.read())
    print("Part One: ", part_one(source))
    print("Part Two: ", part_two(source))
