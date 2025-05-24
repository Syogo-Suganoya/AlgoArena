N, K = map(int, input().split())
A = list(map(int, input().split()))


def main():
    total = sum(A)
    return K >= total and (K - total) % 2 == 0


print("Yes" if main() else "No")
