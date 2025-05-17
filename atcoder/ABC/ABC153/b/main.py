H, N = map(int, input().split())
A = list(map(int, input().split()))


def main():
    return H <= sum(A)


print("Yes" if main() else "No")
