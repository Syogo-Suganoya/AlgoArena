N = int(input())
A = list(map(int, input().split()))
X = int(input())


def main():
    return X in A


print("Yes" if main() else "No")
