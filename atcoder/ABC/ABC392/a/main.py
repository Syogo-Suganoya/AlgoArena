A1, A2, A3 = map(int, input().split())


def main():
    return (A1 * A2 == A3) or (A1 * A3 == A2) or (A2 * A3 == A1)


print("Yes" if main() else "No")
