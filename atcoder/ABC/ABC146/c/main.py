A, B, X = map(int, input().split())


def cost(n):
    # n を買うために必要な金額
    return A * n + B * len(str(n))


lo, hi = 0, 10**9 + 1  # hi は「買えない」ことが確実な上限

while lo + 1 < hi:
    mid = (lo + hi) // 2
    if cost(mid) <= X:
        lo = mid
    else:
        hi = mid

print(lo)
