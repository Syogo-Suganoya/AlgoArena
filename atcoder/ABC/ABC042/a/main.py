S = list(map(int, input().split()))


def main():
    S.sort()
    return S == [5, 5, 7]


print("YES" if main() else "NO")
