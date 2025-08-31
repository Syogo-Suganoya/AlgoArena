N = int(input())
A = [input() for _ in range(N)]
X, Y = input().split()


def main():
    return A[int(X) - 1] == Y


print("Yes" if main() else "No")
