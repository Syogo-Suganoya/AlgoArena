n = int(input())
a = list(map(int, input().split()))

ans = 0

# l を左端に固定
for l in range(n):
    x = a[l]  # 区間の最小値を保持
    # r を右に伸ばしていく
    for r in range(l, n):
        x = min(x, a[r])  # 区間 [l, r] の最小値を更新
        ans = max(ans, x * (r - l + 1))  # 面積（最小値 × 幅）を更新

print(ans)
