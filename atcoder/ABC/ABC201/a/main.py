A = list(map(int, input().split()))


def main():
    A.sort()
    return A[1] - A[0] == A[2] - A[1]


print("Yes" if main() else "No")
