import bisect

N, T, P = map(int, input().split())
L = list(map(int, input().split()))

# 必要な日数
l = [T - score for score in L]
l.sort()

# P 人以上いるなら
if bisect.bisect_right(l, 0) >= P:
    print(0)
else:
    print(l[P - 1])
