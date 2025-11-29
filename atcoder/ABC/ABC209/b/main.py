N, M = map(int, input().split())
A = list(map(int, input().split()))


def main():
    return sum(A) - (N // 2) <= M


print("Yes" if main() else "No")
