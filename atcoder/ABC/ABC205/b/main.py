N = int(input())
A = set(map(int, input().split()))


def main():
    return len(A) == N and min(A) == 1 and max(A) == N


print("Yes" if main() else "No")
