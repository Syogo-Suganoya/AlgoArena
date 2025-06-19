S = input()


def main():
    s = list(S)
    s.sort()
    return s == ["a", "b", "c"]


print("Yes" if main() else "No")
