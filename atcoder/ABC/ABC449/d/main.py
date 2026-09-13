L, R, D, U = map(int, input().split())


def intersect(x1, x2, y1, y2, a, b, c, d):
    w = max(0, min(x2, b) - max(x1, a) + 1)
    h = max(0, min(y2, d) - max(y1, c) + 1)
    return w * h


ans = 0

maxk = max(abs(L), abs(R), abs(D), abs(U))

for k in range(0, maxk + 1, 2):  # 偶数だけ
    outer = intersect(-k, k, -k, k, L, R, D, U)
    inner = intersect(-(k - 1), k - 1, -(k - 1), k - 1, L, R, D, U) if k > 0 else 0
    ans += outer - inner

print(ans)
