N = int(input())
S = input()


def main():
    s = S.index("|") + 1
    e = S.rindex("|")

    return "*" in S[s:e]


print("in" if main() else "out")
