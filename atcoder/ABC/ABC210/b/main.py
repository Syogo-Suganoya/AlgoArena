N = int(input())
S = input()


def main():
    a = S.index("1")
    return a % 2


print("Aoki" if main() else "Takahashi")
