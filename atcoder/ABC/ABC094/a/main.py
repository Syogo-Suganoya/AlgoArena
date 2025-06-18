A, B, X = map(int, input().split())


def main():
    return A <= X <= A + B


print("YES" if main() else "NO")
