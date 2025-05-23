N, K = map(int, input().split())
S = input()


def main():
    c = S.count("1")

    a = abs(K - c)
    return a % 2 == 0


print("Yes" if main() else "No")
