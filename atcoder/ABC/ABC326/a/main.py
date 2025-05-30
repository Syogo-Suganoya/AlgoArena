N, M = map(int, input().split())


def main():
    if N < M:
        t = abs(N - M)
        return t <= 2
    t = abs(N - M)
    return t <= 3


print("Yes" if main() else "No")
