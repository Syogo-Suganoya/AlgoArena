n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
res = int(2e9)
for i in range(k + 1):
    # 最小値を全探索
    min_val = a[i]
    # その最小値の時に、取りうる最大値を取得
    max_val = a[i + (n - k) - 1]
    # 解を更新
    res = min(res, max_val - min_val)
print(res)
