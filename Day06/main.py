with open("./input.txt") as f:
    src = f.read().strip()


def find_marker(char_size: int) -> int:
    for i in range(len(src)):
        x = src[i : i + char_size]
        if len(set(x)) == char_size:
            return i + char_size
    return -1  # This is should never be returned


print(find_marker(4))
print(find_marker(14))
