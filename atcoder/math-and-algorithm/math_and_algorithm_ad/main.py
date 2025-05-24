N, X = map(int, input().split())
A = list(map(int, input().split()))


def main():
    a = set(A)
    return X in a


print("Yes" if main() else "No")
