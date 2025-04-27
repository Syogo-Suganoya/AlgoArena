from sortedcontainers import SortedSet

N = int(input())
A = list(map(int, input().split()))


def main():
    sa = list(SortedSet(A))
    return A == sa


print("Yes" if main() else "No")
