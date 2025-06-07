N, K = map(int, input().split())
A = list(map(int, input().split()))


def can(t):
    return sum(t // a for a in A) >= K


lo, hi = 0, max(A) * K  # hi は安全マージン

while lo < hi:
    mid = (lo + hi) // 2
    if can(mid):
        hi = mid
    else:
        lo = mid + 1

print(lo)
