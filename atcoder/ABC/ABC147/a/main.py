A = list(map(int, input().split()))


def main():
    return sum(A) >= 22


print("bust" if main() else "win")
