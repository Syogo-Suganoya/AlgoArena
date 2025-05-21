S = list(map(int, input().split()))


def main():
    S.sort()
    return S[-1] == S[1] + S[0]


print("Yes" if main() else "No")
