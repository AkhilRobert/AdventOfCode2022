with open("input.txt", "r") as file:
    groups = file.read().split("\n\n")

sums = [sum(map(int, group.split())) for group in groups]
print(max(sums))
print(sum(sorted(sums, reverse=True)[:3]))
