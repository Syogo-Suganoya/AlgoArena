N, D = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(N)]

# 壁を右端でソート
LR.sort(key=lambda x: x[1])

ans = 0
last_punch_end = -1

for l, r in LR:
    if last_punch_end < l:
        ans += 1
        last_punch_end = r + D - 1

print(ans)
