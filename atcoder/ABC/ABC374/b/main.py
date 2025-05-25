S = input()
T = input()


def main():
    if S == T:
        return 0

    m = min(len(S), len(T))
    for i in range(m):
        if S[i] != T[i]:
            return i + 1
    return m + 1


print(main())
