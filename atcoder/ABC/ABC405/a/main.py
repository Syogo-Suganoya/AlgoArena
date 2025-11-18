N, M = map(int, input().split())


def main():
    if M == 1:
        return 1600 <= N <= 2999

    if M == 2:
        return 1200 <= N <= 2399


print("Yes" if main() else "No")
