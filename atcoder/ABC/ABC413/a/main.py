N, M = map(int, input().split())
A = list(map(int, input().split()))


def main():
    return M >= sum(A)


print("Yes" if main() else "No")
