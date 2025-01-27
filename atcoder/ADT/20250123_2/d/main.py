N = int(input())


def main():
    s = set()
    for _ in range(N):
        S = input()
        if S[0] not in "HDCS":
            return False
        if S[1] not in "A23456789TJQK":
            return False
        if S in s:
            return False
        s.add(S)

    return True


print("Yes" if main() else "No")
