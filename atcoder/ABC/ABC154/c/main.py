N = int(input())
A = list(map(int, input().split()))


def main():
    a = set(A)
    return len(a) == N


print("YES" if main() else "NO")
