from collections import Counter


def main():
    N = int(input())
    pairs = []
    names = []

    for _ in range(N):
        s, t = input().split()
        pairs.append((s, t))
        names.extend({s, t})

    name_counts = Counter(names)
    for s, t in pairs:
        if name_counts[s] >= 2 and name_counts[t] >= 2:
            return False
    return True


print("Yes" if main() else "No")
