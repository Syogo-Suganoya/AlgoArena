N = int(input())

ans = 0
for i in range(1, N + 1):
    # 桁数を str(i) の長さで判定
    d = len(str(i))
    if d == 1 or d == 3 or d == 5:
        ans += 1

print(ans)
