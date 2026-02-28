import math

N, M = map(int, input().split())


def main():
    return math.ceil(N / 2) >= M


print("Yes" if main() else "No")
