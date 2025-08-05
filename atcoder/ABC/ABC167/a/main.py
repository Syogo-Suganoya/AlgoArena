S = input()
T = input()


def main():
    return S == T[:-1]


print("Yes" if main() else "No")
