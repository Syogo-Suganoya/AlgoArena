S = input()


def main():
    return S == S[::-1]


print("Yes" if main() else "No")
