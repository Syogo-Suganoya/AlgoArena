from collections import Counter


def main():
    S = input()
    counter = Counter(S)

    for i in range(1, len(S) + 1):
        tmp = [char for char, count in counter.items() if count == i]
        if tmp and len(tmp) != 2:
            return False
    return True


print("Yes" if main() else "No")
