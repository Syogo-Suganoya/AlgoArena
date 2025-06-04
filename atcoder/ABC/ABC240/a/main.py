a, b = map(int, input().split())


def main():
    if (a == 1 and b == 10) or (a == 10 and b == 1):
        return True
    return abs(a - b) == 1


print("Yes" if main() else "No")
