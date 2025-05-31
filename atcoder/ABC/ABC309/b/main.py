n = int(input())
a = []

# 入力を 2 次元リストに変換
for _ in range(n):
    s = input()
    row = [int(c) for c in s]
    a.append(row)

# 出力用の 2 次元リストを用意（全要素 0）
ans = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n - 1 or j == n - 1:
            # 外周のときは 1 マス右にシフト（条件に応じて）
            if i == 0 and j < n - 1:
                ans[i][j + 1] = a[i][j]
            if i < n - 1 and j == n - 1:
                ans[i + 1][j] = a[i][j]
            if i == n - 1 and j > 0:
                ans[i][j - 1] = a[i][j]
            if i > 0 and j == 0:
                ans[i - 1][j] = a[i][j]
        else:
            # 内側のマスはそのままコピー
            ans[i][j] = a[i][j]

# 出力
for row in ans:
    print("".join(map(str, row)))
