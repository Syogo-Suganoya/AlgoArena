n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())

# 出力用の空のグリッドを生成（'.'で埋める）
h = q - p + 1
w = s - r + 1
ans = [["."] * w for _ in range(h)]

# 条件1: (i, j) が a + k, b + k に一致（対角線）
x = max(p - a, r - b)
y = min(q - a, s - b)
for i in range(x, y + 1):
    row = a + i - p
    col = b + i - r
    ans[row][col] = "#"

# 条件2: (i, j) が a + k, b - k に一致（反対側の対角線）
x = max(p - a, b - s)
y = min(q - a, b - r)
for i in range(x, y + 1):
    row = a + i - p
    col = b - i - r
    ans[row][col] = "#"

# 出力
for row in ans:
    print("".join(row))
