with open("./input.txt") as f:
    src = f.read().split("\n\n")
    calories = [sum(map(int, x.splitlines())) for x in src]
    calories.sort(reverse=True)
    print("Part 1: ", max(calories))
    print("Part 2: ", sum(calories[:3]))
