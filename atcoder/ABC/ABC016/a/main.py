M, D = map(int, input().split())


def main():
    return M % D == 0


print("YES" if main() else "NO")
