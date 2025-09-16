N, R = map(int, input().split())
A = list(map(int, input().split()))

# すでに全て1なら0を出力して終了
if all(v == 1 for v in A):
    print(0)
    exit()

# 左端の0を探す
l = A.index(0)
# 右端の0を探す
r = N - 1 - A[::-1].index(0)

ans = 0

# 左側の書き換え回数
for v in A[l:R]:
    ans += 1 if v == 0 else 2

# 右側の書き換え回数
for v in A[R : r + 1]:
    ans += 1 if v == 0 else 2

print(ans)
