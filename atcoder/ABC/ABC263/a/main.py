from collections import Counter

S = list(map(int, input().split()))


def main():
    c = Counter(S)
    if len(c) != 2:
        return False
    return sorted(c.values()) == [2, 3]


print("Yes" if main() else "No")
