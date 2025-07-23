a, b, c = map(int, input().split())


def main():
    l = [a, b, c]
    l.sort()
    return b == l[1]


print("Yes" if main() else "No")
