with open("input.txt") as f:
    lines = [line.strip().split() for line in f]

data = [[ord(a) - ord("A") + 1, ord(b) - ord("X") + 1] for a, b in lines]
print(sum(3 * ((b + 1 - a) % 3) for a, b in data) + sum(b for _, b in data))
print(sum((a + b) % 3 + 1 for a, b in data) + sum((b - 1) * 3 for _, b in data))
