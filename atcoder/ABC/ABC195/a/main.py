M, H = map(int, input().split())


def main():
    return H % M == 0


print("Yes" if main() else "No")
