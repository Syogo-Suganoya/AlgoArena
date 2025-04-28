from collections import Counter


def main():
    A = list(map(int, input().split()))
    count = Counter(A)
    freqs = sorted(count.values(), reverse=True)
    return len(freqs) >= 2 and freqs[0] >= 3 and freqs[1] >= 2


print("Yes" if main() else "No")
